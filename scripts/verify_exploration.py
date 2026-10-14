#!/usr/bin/env python3
"""Read-only integration checks through ASGI using real news data.

An in-process test principal replaces key/quota dependencies; no listener or
customer account is created and no account usage is changed. Cache refreshes
are allowed. Offline tests separately check real authentication and quota paths.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent / 'prism-business-news-api'))
from fastapi.testclient import TestClient
from prism_news_api import auth, ch, config, quota
from prism_business_api.features.aggregates import AMOUNT_SQL, funding_totals
from prism_news_api.main import create_app
from prism_news_api.routers import metered, unmetered
from prism_business_api.main import create_app as business_app


def main():
    principal = auth.Principal(user_id='0' * 24, key_id='1' * 24, key_prefix='verification',
        key_name='in-process verification', email=None, plan='free', plan_cfg=config.plan_cfg('free'),
        source='verification', expired=False, expires=None, account_flag=None)
    def caller():
        return principal
    apps = {'news': create_app(), 'business': business_app()}
    for app in apps.values():
        app.dependency_overrides[metered] = caller
        app.dependency_overrides[unmetered] = caller
    clients = {name: TestClient(app, raise_server_exceptions=False) for name, app in apps.items()}
    cases = []
    # Two usable amounts have a median of 15; unknown values must not turn into zero amounts.
    row = ch.one(f"SELECT {AMOUNT_SQL} FROM (SELECT arrayJoin([10.,20.,0.,-5.,toFloat64('nan')]) AS amount_usd)")
    totals = funding_totals(row)
    assert totals["deals"] == 5 and totals["deals_with_amount"] == 2
    assert totals["sum_amount_usd"] == 30 and totals["median_amount_usd"] == 15
    cases.append({"case":"funding median and unknown amounts", "passed":True})
    def check(service, method, path, params=None, expected=200):
        t0 = time.monotonic()
        kwargs = {'params': params} if method == 'GET' else {'json': params}
        r = clients[service].request(method, path, **kwargs)
        try: data = r.json()
        except ValueError: data = {}
        item = {'service':service,'method':method,'path':path,'status':r.status_code,
                'seconds':round(time.monotonic()-t0,3),'passed':r.status_code == expected}
        if data.get('error'): item['error'] = data['error']
        if isinstance(data.get('data'),dict):
            item['window'] = data.get('window')
            for name in ('matched','count','articles','returned','limit','total_estimate'):
                if name in data['data']: item[name] = data['data'][name]
        cases.append(item)
        print(json.dumps(item),flush=True)
        if r.status_code != expected:
            raise AssertionError(item)
        return data
    common = {'q':'electric vehicle','since':'2026-04-01','until':'2026-04-30'}
    with patch.object(quota,'record_daily',lambda *a,**k:None), \
         patch.object(quota,'reserve_exports',lambda user,key,n,limit:n), \
         patch.object(quota,'refund_exports',lambda *a,**k:None), \
         patch.object(quota,'exports_remaining',lambda *a,**k:100):
        check('news','GET','/healthz')
        check('business','GET','/healthz')
        for name in clients:
            check(name,'GET','/v1/openapi.json')
            check(name,'GET','/v1/classes',{'q':'venture'})
            check(name,'GET','/v1/classes',expected=400)
        for method in ('GET','POST'):
            check('news',method,'/v1/themes',{},400)
            d=check('news',method,'/v1/themes',common)
            assert 1 <= d['data']['returned'] <= 5 and d['data']['total_estimate'] is None
        for path in ('overview','coverage','geography'):
            check('news','GET','/v1/'+path,common)
        check('news','POST','/v1/compare',{'queries':[
            {'name':'Electric vehicles','filters':common},
            {'name':'Solar energy','filters':{**common,'q':'solar energy'}}]})
        d=check('news','GET','/v1/headlines',common)
        assert d['data']['limit']==100 and len(d['data']['items']) <=100
        assert all('themes' not in i for i in d['data']['items'])
        aid=d['data']['items'][0]['id']
        check('news','GET',f'/v1/articles/{aid}/related',common)
        d=check('news','POST','/v1/export',common)
        assert d['data']['limit']==100 and 0 < d['data']['returned'] <=100
        assert all('themes' not in i and 'body' in i for i in d['data']['items'])
        for path in ('themes','overview'):
            check('business','GET','/v1/business/'+path,{**common,'q':'technology'})
        check('business','GET','/v1/business/themes',{},400)
        check('business','GET','/v1/business/event-trends',{'since':'2026-04-01','until':'2026-04-30','company':'amazon.com'})
        check('business','GET','/v1/business/funding/summary',{'since':'2026-04-01','until':'2026-04-30'})
    out=ROOT/'internal'/'verification.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'cases':cases,'passed':len(cases),'verification':'ASGI requests with real data and in-process identity; no customer usage writes'},indent=2))
    print(f'PASS {len(cases)} integration cases',flush=True)


if __name__ == '__main__': main()
