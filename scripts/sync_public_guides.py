#!/usr/bin/env python3
"""Copy canonical user guides into both packages before building them."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
for repo, package in ((root, 'prism_news_api'), (root.parent / 'prism-business-news-api', 'prism_business_api')):
    source = repo / 'docs' / 'USER_GUIDE.md'
    target = repo / package / 'data' / 'user_guide.md'
    target.parent.mkdir(exist_ok=True)
    shutil.copyfile(source, target)
    print(f'{repo.name}: public guide synchronized')
