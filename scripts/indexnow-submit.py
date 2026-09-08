"""
Notify IndexNow (Bing, Yandex, Seznam, Naver) that pages have changed.

Usage:
  python scripts/indexnow-submit.py                 # submit every URL in sitemap.xml
  python scripts/indexnow-submit.py https://hammsolutions.com/networking.html [more-urls...]
"""
import sys
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HOST = "hammsolutions.com"
KEY = "d287a7da7d4b467c6cd1342134100a24"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
SITEMAP = Path(__file__).resolve().parent.parent / "sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"


def urls_from_sitemap():
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse(SITEMAP).getroot()
    return [loc.text.strip() for loc in root.findall(".//s:loc", ns)]


def main():
    url_list = sys.argv[1:] or urls_from_sitemap()
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": url_list,
    }).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT, data=payload, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"Submitted {len(url_list)} URL(s) -> HTTP {resp.status}")
    except urllib.error.HTTPError as e:
        print(f"Submitted {len(url_list)} URL(s) -> HTTP {e.code} {e.reason}")
        print(e.read().decode(errors="replace"))

    for u in url_list:
        print(f"  - {u}")


if __name__ == "__main__":
    main()
