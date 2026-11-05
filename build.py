"""index.html(원본)에서 배포용 파일 두 개를 만든다.

  python3 build.py

- 11st-gnb-tabbar-prototype.html : 이미지를 base64로 넣은 단일 파일 (서버 없이 어디서든 열림)
- share.html             : claude.ai Artifact 재배포용 (doctype/head/body 태그 제거 + 안내 문구)
"""
import base64
import re
from pathlib import Path

ROOT = Path(__file__).parent
src = (ROOT / "index.html").read_text(encoding="utf-8")

# 1) 단일 파일
def inline(m):
    data = (ROOT / m.group(0)).read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode()

single = re.sub(r"img/[A-Za-z0-9_./-]+\.png", inline, src)
(ROOT / "11st-gnb-tabbar-prototype.html").write_text(single, encoding="utf-8")

# 2) Artifact용
share = src
for tag in [
    r"<!doctype html>\n", r'<html lang="ko">\n', r"<head>\n", r'<meta charset="utf-8">\n',
    r'<meta name="viewport"[^>]*>\n', r"</head>\n", r"<body>\n", r"</body>\n", r"</html>\n?",
]:
    share = re.sub(tag, "", share, count=1)
share = share.replace(
    '<div class="hint"><kbd>H</kbd>',
    '<div class="hint">GNB·탭바 아이디에이션 프로토타입 · 탭바 <b>나의11번가</b> → 가운데 <b>비비고 배너</b> → PDP<br><kbd>H</kbd>',
)
(ROOT / "share.html").write_text(share, encoding="utf-8")

print(f"11st-gnb-tabbar-prototype.html {len(single)/1e6:.1f}MB, share.html {len(share)/1e3:.0f}KB")
