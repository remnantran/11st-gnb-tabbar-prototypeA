# 11번가 GNB·탭바 아이디에이션 프로토타입

**보기:** https://remnantran.github.io/11st-gnb-tabbar-prototype/

홈 → 탭바 **나의11번가** → 가운데 **비비고 배너** → PDP. 화면 스크롤, GNB 버튼 ease-in-out 모핑, glass 탭바(굴절 효과는 Chrome 전용).
키보드: `H` 핫스팟 보기, `←`/`Esc` 뒤로.

Figma: [K03Ye6qjq9vaqKREhSuN9o](https://www.figma.com/design/K03Ye6qjq9vaqKREhSuN9o/) — 홈 55:28520, 나의11번가 55:28728, PDP 55:29101

## 파일

| 파일 | 설명 |
|---|---|
| `index.html` | 원본. 수정은 여기서만. GitHub Pages도 이 파일을 보여줌 |
| `img/` | Figma 2x 내보내기 (CONTENTS, GNB 아이콘, `tab/` 탭바 아이콘). `_orig/`는 배경 키아웃 전 원본 |
| `build.py` | 아래 두 파일 생성 |
| `11st_tabbar_proto.html` | 이미지 내장 단일 파일 — 메일·메신저로 보내 더블클릭으로 열기 |
| `share.html` | claude.ai Artifact 재배포용 |

## 수정 후 반영

```bash
python3 -m http.server 8765   # 로컬 확인: http://localhost:8765
python3 build.py
git add -A && git commit -m "..." && git push   # 1~2분 뒤 Pages 반영
```
