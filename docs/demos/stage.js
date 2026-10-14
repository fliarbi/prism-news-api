/* Deterministic, source-qualified animation frames. No network requests.
   Every story in demo-data.js carries two data-driven views (overview, detail);
   this file only knows how to draw the view types, never the numbers. */
(() => {
  const h = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const clamp = n => Math.max(0, Math.min(1, n));
  const ease = n => 1 - (1 - clamp(n)) ** 3;
  const palette = ['#3b4fd8','#0f8b8d','#8a4fbf','#cf7a1d','#c0453b','#5b6b7d','#2e9d5a','#a8841a'];
  const tones = {negative:'#c0453b', neutral:'#8a99a8', positive:'#2e9d5a'};
  const color = (s, i) => tones[s.tone] || s.color || palette[i % palette.length];
  const svg = (body, w, ht, cls='chart') => `<svg class="${cls}" viewBox="0 0 ${w} ${ht}" role="img">${body}</svg>`;
  const text = (x,y,value,cls='',anchor='start') => `<text x="${x}" y="${y}" class="${cls}" text-anchor="${anchor}">${h(value)}</text>`;
  const line = (x1,y1,x2,y2,cls='gridline') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="${cls}"/>`;
  const pill = (value,tone='') => `<span class="tag ${h(tone)}">${h(value)}</span>`;
  const note = value => value ? `<div class="view-note">${h(value)}</div>` : '';
  const compact = n => n >= 1e9 ? `${+(n/1e9).toFixed(1)}B` : n >= 1e6 ? `${+(n/1e6).toFixed(1)}M` : n >= 1e4 ? `${+(n/1e3).toFixed(1)}k` : n.toLocaleString('en-US');
  const niceMax = n => { const p = 10 ** Math.floor(Math.log10(Math.max(n,1))); return Math.ceil(n / p * 1.0001) * p; };
  const stats = list => list && list.length ? `<div class="stat-strip">${list.map(s=>`<div><strong>${h(s.value)}</strong><span>${h(s.label)}</span></div>`).join('')}</div>` : '';
  const legend = (series, extra='') => `<div class="legend">${series.map((s,i)=>`<span><i style="background:${color(s,i)}"></i>${h(s.name)}</span>`).join('')}${extra?`<span class="legend-right">${h(extra)}</span>`:''}</div>`;
  const cell = c => {
    if (c == null) return '<span class="missing">Not returned</span>';
    if (typeof c !== 'object') return h(c);
    if (c.missing) return `<span class="missing">${h(c.missing)}</span>`;
    let out = '';
    if (c.tag) out += pill(c.tag, c.tone);
    if (c.num != null) out += `<span class="number ${h(c.tone||'')}">${h(c.num)}</span>`;
    if (c.main != null) out += `<strong class="${h(c.tone||'')}">${h(c.main)}</strong>`;
    if (c.sub) out += `<small>${h(c.sub)}</small>`;
    return out;
  };
  const table = v => `<table class="results-table"><colgroup>${(v.widths||[]).map(w=>`<col style="width:${w}%">`).join('')}</colgroup><thead><tr>${v.headers.map(x=>`<th>${h(x)}</th>`).join('')}</tr></thead><tbody>${v.rows.map(row=>`<tr>${row.map(c=>`<td>${cell(c)}</td>`).join('')}</tr>`).join('')}</tbody></table>`;

  const views = {
    bars(v, p) {
      const max = niceMax(Math.max(...v.rows.map(r => r.value)));
      const rowH = v.rows.length > 7 ? 40 : v.rows.length > 5 ? 46 : 54, top = 8, x0 = v.labelWidth || 330, span = 1040 - x0;
      let chart = '';
      for (const f of [0, .25, .5, .75, 1]) { const x = x0 + f*span; chart += line(x, 0, x, top + v.rows.length*rowH) + text(x, top + v.rows.length*rowH + 26, (v.prefix||'') + compact(f*max), 'axis', 'middle'); }
      v.rows.forEach((r, i) => {
        const y = top + i*rowH + rowH/2, w = Math.max(3, r.value/max*span*p);
        chart += text(0, y - (r.sub ? 4 : -7), r.label, 'bar-label') + (r.sub ? text(0, y + 18, r.sub, 'axis') : '');
        chart += `<rect x="${x0}" y="${y-14}" width="${w}" height="28" rx="4" fill="${r.highlight===false?'#b9c4f0':color(r, v.colorIndex ?? 0)}"/>`;
        chart += `<g opacity="${clamp((p-.5)/.5)}">` + text(x0 + w + 12, y + 8, r.display, 'value') + '</g>';
      });
      const ht = top + v.rows.length*rowH + 36;
      return `${v.axisLabel?`<div class="legend"><span class="legend-right">${h(v.axisLabel)}</span></div>`:''}${svg(chart, 1176, ht)}${stats(v.stats)}${note(v.note)}`;
    },
    columns(v, p) {
      const n = v.labels.length, H = v.height || 300, x0 = 70, span = 1100, slot = span / n;
      const totals = v.labels.map((_, i) => v.stacked ? v.series.reduce((s, se) => s + se.values[i], 0) : Math.max(...v.series.map(se => se.values[i])));
      const max = niceMax(Math.max(...totals)), y = val => H - val/max*H;
      let chart = '';
      for (const f of [0, .25, .5, .75, 1]) chart += line(x0, y(f*max), x0+span, y(f*max)) + text(x0-12, y(f*max)+6, compact(f*max), 'axis', 'end');
      v.labels.forEach((label, i) => {
        const cx = x0 + slot*i + slot/2;
        if (v.stacked) {
          let base = 0, bw = Math.min(64, slot*.62);
          v.series.forEach((se, k) => { const hgt = se.values[i]/max*H*p; chart += `<rect x="${cx-bw/2}" y="${y(base)-hgt}" width="${bw}" height="${hgt}" fill="${color(se,k)}"/>`; base += se.values[i]*p; });
          chart += `<g opacity="${clamp((p-.6)/.4)}">` + text(cx, y(totals[i]*p) - 10, compact(totals[i]), 'col-value', 'middle') + '</g>';
        } else {
          const k = v.series.length, bw = Math.min(54, slot*.78/k);
          v.series.forEach((se, j) => { const hgt = se.values[i]/max*H*p, bx = cx - (k*bw)/2 + j*bw; chart += `<rect x="${bx+2}" y="${H-hgt}" width="${bw-4}" height="${hgt}" rx="2" fill="${color(se,j)}"/>`; if (k === 1) chart += `<g opacity="${clamp((p-.6)/.4)}">` + text(cx, H-hgt-10, compact(se.values[i]), 'col-value', 'middle') + '</g>'; });
        }
        chart += text(cx, H + 30, label, 'axis', 'middle');
        if (v.sublabels) chart += text(cx, H + 52, v.sublabels[i], 'axis faint', 'middle');
      });
      return `${legend(v.series, v.unit)}${svg(chart, 1176, H + (v.sublabels ? 60 : 40))}${stats(v.stats)}${note(v.note)}`;
    },
    lines(v, p) {
      const n = v.labels.length, H = v.height || 300, x0 = 70, span = 1080;
      const max = niceMax(Math.max(...v.series.flatMap(s => s.values))), X = i => x0 + i*span/(n-1), Y = val => H - val/max*H;
      let chart = '';
      for (const f of [0, .25, .5, .75, 1]) chart += line(x0, Y(f*max), x0+span, Y(f*max)) + text(x0-12, Y(f*max)+6, compact(f*max), 'axis', 'end');
      v.labels.forEach((label, i) => { chart += text(X(i), H + 30, label, 'axis', 'middle'); });
      v.series.forEach((s, k) => {
        const d = s.values.map((val, i) => `${i ? 'L' : 'M'}${X(i).toFixed(1)},${Y(val).toFixed(1)}`).join(' ');
        chart += `<path d="${d}" fill="none" stroke="${color(s,k)}" stroke-width="5" stroke-linejoin="round" stroke-dasharray="3000" stroke-dashoffset="${3000*(1-p)}"/>`;
        s.values.forEach((val, i) => { if (i/(n-1) <= p + .001) chart += `<circle cx="${X(i)}" cy="${Y(val)}" r="6" fill="${color(s,k)}"/>`; });
        const last = s.values[n-1];
        chart += `<g opacity="${clamp((p-.7)/.3)}">` + text(X(n-1) - 8, Y(last) - 14, compact(last), 'col-value', 'end') + '</g>';
      });
      return `${legend(v.series, v.unit)}${svg(chart, 1176, H + 40)}${stats(v.stats)}${note(v.note)}`;
    },
    donut(v, p) {
      const total = v.segments.reduce((s, x) => s + x.value, 0), R = 150, C = 2*Math.PI*R;
      let ring = '', acc = 0;
      v.segments.forEach((s, i) => { const len = s.value/total*C; ring += `<circle cx="210" cy="210" r="${R}" fill="none" stroke="${color(s,i)}" stroke-width="56" stroke-dasharray="${Math.max(0,len*p-3)} ${C}" stroke-dashoffset="${-acc*p}" transform="rotate(-90 210 210)"/>`; acc += len; });
      ring += text(210, 214, v.centerValue, 'donut-total', 'middle') + text(210, 256, v.centerLabel, 'axis', 'middle');
      const items = v.segments.map((s, i) => `<div><i style="background:${color(s,i)}"></i><strong>${h(compact(s.value))}</strong><span>${h(s.label)}</span><em>${(s.value/total*100).toFixed(1)}%</em></div>`).join('');
      return `<div class="donut-view">${svg(ring, 420, 430)}<section class="donut-legend">${items}${v.side?`<p>${h(v.side)}</p>`:''}</section></div>${note(v.note)}`;
    },
    tree(v, p) {
      const shown = Math.ceil(v.groups.reduce((s, g) => s + g.items.length, 0) * clamp(p*1.15));
      let k = 0;
      const groups = v.groups.map(g => `<section class="tree-group"><h3>q = “${h(g.query)}”</h3>${g.items.map(it => { const vis = k++ < shown; const parts = it.path.split('/').filter(Boolean); return `<div class="tree-row" style="opacity:${vis?1:0}"><span class="code-chip">${h(it.code)}</span><span class="tree-path">${parts.slice(0,-1).map(x=>`<span>${h(x)}</span>`).join('<b>›</b>')}<b>›</b><strong>${h(parts.at(-1))}</strong></span></div>`; }).join('')}</section>`).join('');
      return `<div class="tree-view">${groups}</div>${note(v.note)}`;
    },
    table(v) { return table(v) + stats(v.stats) + note(v.note); },
    cards(v) {
      return `<div class="card-list">${v.items.map(it => `<article class="news-card"><h3>${h(it.headline)}</h3><p>${h(it.meta)}</p><div>${(it.tags||[]).map(t=>pill(t.text, t.tone)).join('')}</div></article>`).join('')}</div>${note(v.note)}`;
    },
    sheet(v) {
      return `<div class="sheet-heading"><span class="sheet-symbol">${h(v.symbol||'CSV')}</span><b>${h(v.filename)}</b><span>${h(v.status||'')}</span></div>${table(v)}${stats(v.stats)}${note(v.note)}`;
    },
  };

  let story = window.PRISM_DEMOS.find(s => s.id === new URLSearchParams(location.search).get('demo')) || window.PRISM_DEMOS[0];
  function render(t) {
    const s = story, time = Math.max(0, Math.min(s.duration, t));
    const exit = ease((time-6.4)/1.1), enter = ease((time-6.8)/.9);
    const detail = time >= 18.5, change = ease((time-18.5)/.75);
    const reveal = detail ? change : enter;
    const progress = ease((time-(detail?19:7.5))/1.4);
    const v = detail ? s.detail : s.overview;
    const body = views[v.type](v, progress);
    const typed = s.prompt.slice(0, Math.floor(s.prompt.length*clamp((time-.65)/4.2)));
    const phase = time < 6.4 ? 'Prompt' : detail ? 'Details' : 'Results';
    document.getElementById('stage').innerHTML = `<header class="film-top"><div class="brand"><span class="prism-mark"></span><b>${h(s.brand)}</b><span>${h(s.client)} + API</span></div><span class="provenance ${h(s.kind)}">${h(s.badge)}</span></header><section class="search-scene" aria-hidden="${exit===1}" style="transform:translateX(${-1450*exit}px);opacity:${1-exit}"><div class="search-caption">Ask a question. Explore the coverage.</div><h1>${h(s.heading)}</h1><div class="search-box"><span class="search-icon"></span><div class="prompt-text">${typed?h(typed):'<span class="placeholder">Describe your research…</span>'}<span class="type-cursor" style="opacity:${time<5.2?(Math.floor(time*2.5)%2?0:1):0}"></span></div><div class="submit-arrow">↵</div></div><div class="search-hint">${time<4.9?'One prompt, a filtered news archive.':'Turn the request into a full research view.'}</div></section><section class="result-scene" aria-hidden="${time<6.8}" style="transform:translateX(${(1-enter)*1280}px);opacity:${enter}"><div class="result-heading"><div><h2>${h(v.title)}</h2><p>${h(v.subtitle)}</p></div><span class="view-count">${detail?'2 / 2':'1 / 2'}</span></div><div class="full-result" style="opacity:${reveal};transform:translateY(${detail?(1-change)*24:0}px)">${body}</div><div class="source-footer">${h(s.footnote)}</div></section><footer class="film-bottom"><span>Concept UI · ${s.kind==='captured'?'saved API responses':'illustrative data'} · no live requests</span><span>${phase}</span><div class="film-progress" style="width:${time/s.duration*100}%"></div></footer>`;
    document.documentElement.dataset.demo = s.id;
    document.documentElement.dataset.frameTime = time;
    document.documentElement.dataset.phase = time < 6.4 ? 'prompt' : time < 7.7 ? 'transition' : detail ? 'detail' : 'overview';
  }
  window.setDemo = id => { story = window.PRISM_DEMOS.find(s => s.id === id); if (!story) throw new Error('Unknown demo'); render(0); };
  window.renderFrame = render;
  window.getDemo = () => story;
  render(Number(new URLSearchParams(location.search).get('t') || 0));
})();
