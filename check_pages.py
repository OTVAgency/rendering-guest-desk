"""Validate packaged links and keep recordings/local paths out of the site."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
import json

ROOT=Path(__file__).resolve().parent
DIST=ROOT
class Links(HTMLParser):
    def __init__(self):super().__init__();self.values=[]
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key in ['src','href'] and value:self.values.append(value)

assert (DIST/'index.html').is_file()
for file in DIST.rglob('*'):
    if not file.is_file() or file.name=='check_pages.py':continue
    assert file.suffix.lower() not in ['.mp4','.mov','.mp3','.wav','.zip'],file
    if file.suffix.lower() in ['.html','.js','.css','.json','.srt','.txt']:
        text=file.read_text()
        assert not any(term in text for term in ['/Users/','127.0.0.1','localhost:','file://','OAI-Sites-Authorization']),file
    if file.suffix=='.html':
        parser=Links();parser.feed(file.read_text())
        for value in parser.values:
            parts=urlsplit(value)
            if parts.scheme or parts.netloc or not parts.path:continue
            target=(file.parent/unquote(parts.path)).resolve()
            assert target.is_relative_to(DIST.resolve()),(file,value)
            assert target.is_file(),(file,value)
page=(DIST/'episodes/pilot-michael-turner/index.html').read_text()
assert '1OnrMRfTenwppdl2ZTRVAe_KIzTCMK-QW/view' in page
assert not any(DIST.rglob('*.srt'))
assert 'chatgpt.site' not in page
assert '1y5Y9A15PogLP5_isJTW3E-k_5SCTuDr1/view' in page
assert '<iframe' not in page and 'video-launch' in page
assert 'review.js' in page and 'AI-assisted' in page
print('GitHub Pages links and restricted-media checks passed')
