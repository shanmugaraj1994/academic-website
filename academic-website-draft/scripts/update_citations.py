"""Refresh the static profile and CV from SerpApi; keep the prior values on failure."""
import datetime
import json
import os
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
AUTHOR_ID = 'tuuSnYMAAAAJ'

def citation_total(data):
    if data.get('error'):
        raise ValueError('Provider returned an error')
    name = data.get('author', {}).get('name', '').casefold()
    if 'shanmugaraj' not in name or 'senthilnathan' not in name:
        raise ValueError('Response does not match the expected author')
    for item in data.get('cited_by', {}).get('table', []):
        if 'citations' in item:
            raw = item['citations'].get('all')
            if isinstance(raw, bool):
                break
            value = str(raw).replace(',', '')
            if value.isdigit() and 0 <= int(value) <= 100_000_000:
                return int(value)
            break
    raise ValueError('Missing or invalid all-time citation count')

def update_pages(total, today):
    edits = []
    for filename in ('index.html', 'cv.html'):
        path = ROOT / filename
        content = path.read_text(encoding='utf-8')
        content, n = re.subn(r'(<span data-citation-count>)\d+(</span>)',
                             lambda m: m[1] + str(total) + m[2], content)
        if n != 1:
            raise ValueError('Expected exactly one count in ' + filename)
        date = f'{today.day} {today:%B %Y}'
        content, n = re.subn(r'<time data-citation-date datetime="[^"]+">[^<]+</time>',
                             f'<time data-citation-date datetime="{today.isoformat()}">{date}</time>', content)
        if n != 1:
            raise ValueError('Expected exactly one date in ' + filename)
        edits.append((path, content))
    # Complete response and both templates are validated before modifying either page.
    for path, content in edits:
        path.write_text(content, encoding='utf-8')

def main():
    key = os.environ.get('SERPAPI_API_KEY', '').strip()
    if not key:
        print('SERPAPI_API_KEY is not configured. Existing count preserved.', file=sys.stderr)
        return 1
    query = urllib.parse.urlencode({'engine': 'google_scholar_author',
                                    'author_id': AUTHOR_ID, 'hl': 'en', 'api_key': key})
    try:
        with urllib.request.urlopen('https://serpapi.com/search.json?' + query, timeout=60) as response:
            data = json.load(response)
        total = citation_total(data)
        update_pages(total, datetime.datetime.now(datetime.timezone.utc).date())
    except Exception:
        # Do not log exceptions or request URLs, which could contain the API key.
        print('Citation refresh failed; existing count and date preserved. Check provider status and configuration.', file=sys.stderr)
        return 1
    print(f'Updated both pages to {total} citations.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
