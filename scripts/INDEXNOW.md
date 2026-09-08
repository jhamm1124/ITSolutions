# IndexNow

Lets Bing, Yandex, Seznam, and Naver know instantly when a page changes,
instead of waiting for their crawler to notice on its own. Google does not
support IndexNow — this has no effect on Google indexing.

## What's here

- `/d287a7da7d4b467c6cd1342134100a24.txt` (site root) — the verification key.
  Must contain **only** the key, nothing else — the protocol checks this file's
  contents against the key you submit, and most validators reject anything
  extra (comments included), so don't edit it.
- `scripts/indexnow-submit.py` — submits URLs to the IndexNow API.

## One-time setup

1. Deploy the site (key file included) to production.
2. Confirm it's publicly reachable:
   `https://hammsolutions.com/d287a7da7d4b467c6cd1342134100a24.txt`
   should return a page containing exactly the key, nothing else.

## Using it

After deploying any content change, run one of:

```
# Submit every URL listed in sitemap.xml
python scripts/indexnow-submit.py

# Submit just the page(s) you changed
python scripts/indexnow-submit.py https://hammsolutions.com/networking.html
```

Output confirms the HTTP status and lists which URLs were submitted.

## Adding a new page later

1. Add the new page's URL to `sitemap.xml`.
2. Deploy.
3. Run `python scripts/indexnow-submit.py` (no arguments) so it's picked up
   from the updated sitemap, or pass the new URL directly.
