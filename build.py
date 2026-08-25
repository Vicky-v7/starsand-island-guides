#!/usr/bin/env python3
"""Starsand Island Guides — static site builder.
Reads page definitions from src/pages.json + content fragments from src/content/*.html,
wraps them in the shared layout, emits site/ with sitemap.xml + robots.txt.
"""
import json, pathlib, datetime

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "site"
BASE_URL = "https://starsand.vickyv7.com"
TODAY = datetime.date.today().isoformat()

LAYOUT = (SRC / "layout.html").read_text()
pages = json.loads((SRC / "pages.json").read_text())

def nav_html(active):
    items = [("Home", "/"), ("Guides", "/guides/"), ("Characters", "/guides/characters/"),
             ("Codes", "/guides/gift-codes/"), ("Review", "/guides/review/")]
    out = []
    for label, href in items:
        cls = ' class="active"' if href == active else ""
        out.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n      ".join(out)

def breadcrumb(page):
    if page["url"] == "/":
        return ""
    crumbs = ['<a href="/">Home</a>']
    if page["url"] != "/guides/":
        crumbs.append('<a href="/guides/">Guides</a>')
    crumbs.append(f'<span>{page["crumb"]}</span>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + " › ".join(crumbs) + "</nav>"

OUT.mkdir(exist_ok=True)
urls = []
for page in pages:
    body = (SRC / "content" / page["fragment"]).read_text()
    html = (LAYOUT
            .replace("{{TITLE}}", page["title"])
            .replace("{{DESCRIPTION}}", page["description"])
            .replace("{{CANONICAL}}", BASE_URL + page["url"])
            .replace("{{NAV}}", nav_html(page["url"]))
            .replace("{{BREADCRUMB}}", breadcrumb(page))
            .replace("{{CONTENT}}", body)
            .replace("{{UPDATED}}", TODAY))
    dest = OUT / page["url"].lstrip("/") / "index.html" if page["url"] != "/" else OUT / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)
    urls.append(page["url"])
    # SEO 自检：title/description 长度
    tl, dl = len(page["title"]), len(page["description"])
    flag = "" if 30 <= tl <= 65 and 120 <= dl <= 165 else "  ⚠️ 长度检查"
    print(f"built {page['url']}  (title {tl}ch, desc {dl}ch){flag}")

sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sitemap.append(f"  <url><loc>{BASE_URL}{u}</loc><lastmod>{TODAY}</lastmod></url>")
sitemap.append("</urlset>")
(OUT / "sitemap.xml").write_text("\n".join(sitemap))
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")
print(f"\n{len(urls)} pages + sitemap.xml + robots.txt → site/")
