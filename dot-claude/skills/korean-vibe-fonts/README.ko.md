# Korean Vibe Fonts ✨

한글 웹폰트를 "뭘 쓰지?" 고민하지 않고, 원하는 분위기에 맞게 추천받는 패키지입니다.

## 📣 더 배우고 싶다면

클로드코드를 비개발자의 시각으로 쉽게 배우고 싶다면 아래 강의를 확인해보세요.

👉 [강의 보러 가기](https://inf.run/BgjkJ)

`퇴근후AI (afterworkai.club)`는 퇴근 후에도 AI를 쉽고 재미있게 익히고 싶은 분들을 위한 커뮤니티입니다.

👉 [퇴근후AI 소개 보기](https://afterworkai.club)
👉 [퇴근후AI 단톡방 참여하기](https://open.kakao.com/o/gzdwHNQh)

이 패키지는 AI 도구가:

- 분위기에 맞는 한글 폰트를 고르고
- 상업적으로 써도 비교적 안전한 폰트를 우선 추천하고
- 바로 붙여 넣을 수 있는 코드까지 같이 내주도록 도와줍니다.

## 🌐 소개 페이지

폰트를 실제 모양으로 비교할 수 있는 소개 페이지를 배포했습니다.

- [https://seulkikaang.github.io/korean-vibe-fonts/](https://seulkikaang.github.io/korean-vibe-fonts/)

현재 464개 한글 웹폰트 항목을 상황별/느낌별로 볼 수 있습니다. 정보 많은 대시보드, 부드러운 금융/헬스케어, 배민 로컬 캠페인, 레트로 포스터, 브랜드 스토리, 키즈 교육, 공공 안내처럼 17개 상황 프리셋도 함께 넣었습니다.

## 🆕 최근 업데이트

- 실전에서 바로 고르기 좋은 큐레이션 폰트 35개를 정리했습니다.
- [fonts-archive](https://github.com/fonts-archive)를 넓게 훑어, 564개 repo 중 웹폰트 CSS와 상업 사용/open-license 신호가 함께 확인된 429개를 추가했습니다.
- 조건부/비상업/불명확/개인용/구매 필요 신호가 있는 135개 repo는 제외했습니다.
- [references/font_decision_guide.json](./references/font_decision_guide.json)에 17개 상황별 선택 기준을 추가했습니다.
- GitHub Pages용 [index.html](./index.html)을 추가해 저장소 루트 페이지가 바로 소개 페이지로 열리게 했습니다.

## 🙋 이건 누가 쓰면 좋나요?

이런 분께 특히 잘 맞습니다.

- 랜딩 페이지를 빠르게 만들고 싶은 사람
- 포트폴리오 분위기를 한 번에 잡고 싶은 사람
- "좀 더 세련되게", "좀 더 따뜻하게" 같은 감성 요청을 자주 하는 사람
- Codex, Claude Code 같은 AI 코딩 도구를 쓰는 사람
- 개발을 깊게 몰라도 AI에게 폰트 선택을 잘 시키고 싶은 사람

## 💡 이걸 쓰면 뭐가 좋아요?

예전에는 이렇게 막연했을 수 있어요.

> "한글 폰트 뭐 쓰지?"

이제는 이렇게 말하면 됩니다.

> "AI SaaS 느낌으로 해줘"
> "차분한 에디토리얼 무드로 해줘"
> "귀엽고 발랄하게 보여줘"
> "개발자 포트폴리오 느낌으로 추천해줘"

그러면 도구가 보통 아래를 같이 알려줍니다.

- 본문용 폰트
- 제목용 폰트
- 필요하면 코드용 폰트
- 바로 붙여 넣는 `<link>` 태그
- 바로 붙여 넣는 CSS
- 비슷한 대안 폰트

추가로 중요한 원칙이 하나 있습니다.

- 화면이나 장표 구성이 달라져도, 같은 역할의 텍스트는 같은 폰트 계열을 유지합니다.

예를 들면:

- 제목은 계속 제목용 폰트
- 본문, 설명, 캡션, 표 텍스트는 계속 본문용 폰트
- 코드나 터미널은 계속 코드용 폰트

그래야 결과물이 바뀌어도 전체 인상은 한 팀이 만든 것처럼 정리됩니다.

## 🧸 비개발자도 쓸 수 있나요?

네, 충분히 가능합니다.

직접 프로그램을 많이 만지지 않더라도:

- AI 도구에 이 패키지를 붙여 두고
- 원하는 분위기를 말한 뒤
- 나온 코드만 복사해서 쓰거나
- 개발자에게 그대로 전달하면 됩니다.

즉, "폰트를 고르는 기준"과 "적용 코드"를 한 번에 받는 도우미라고 생각하시면 됩니다.

## 📦 안에 들어 있는 것

- [SKILL.md](./SKILL.md): Codex에서 읽는 핵심 스킬 파일
- [agents/openai.yaml](./agents/openai.yaml): Codex 메타데이터
- [references/font_catalog.json](./references/font_catalog.json): 검증된 폰트 목록
- [references/font_decision_guide.json](./references/font_decision_guide.json): 어떤 상황에 어떤 폰트를 고를지 정리한 세부 선택표
- [references/fonts_archive_commercial.json](./references/fonts_archive_commercial.json): fonts-archive에서 웹폰트 CSS와 상업 사용/open-license 신호가 확인된 확장 목록
- [references/vibe_presets.md](./references/vibe_presets.md): 자주 쓰는 분위기 프리셋
- [scripts/recommend_font.py](./scripts/recommend_font.py): 폰트 추천기
- [scripts/build_showcase.py](./scripts/build_showcase.py): 소개 HTML과 GitHub Pages용 index 생성기
- [scripts/render_claude_agent.py](./scripts/render_claude_agent.py): Claude Code용 파일 생성기
- [adapters/claude-code-agent.template.md](./adapters/claude-code-agent.template.md): Claude Code용 템플릿
- [adapters/generic-system-prompt.md](./adapters/generic-system-prompt.md): 다른 AI 도구용 기본 프롬프트

## 🚀 설치는 이렇게 생각하면 쉬워요

이 부분이 헷갈릴 수 있는데, 핵심은 이겁니다.

- 먼저 이 패키지 폴더를 내 컴퓨터에 둡니다.
- 그 다음 내가 쓰는 AI 도구에 맞게 "연결"만 해주면 됩니다.

즉, 설치는 보통 2단계입니다.

### 1단계. 이 패키지를 내 컴퓨터에 받기

GitHub 저장소라면 보통 이렇게 받습니다.

```bash
git clone <repo-url>
cd korean-vibe-fonts
```

이미 폴더를 받은 상태라면 이 단계는 건너뛰면 됩니다.

### 2단계. 내가 쓰는 도구에 연결하기

#### Codex를 쓴다면

Codex에서는 일반적인 스킬 설치 방식대로, 이 폴더가 `~/.codex/skills/` 아래에 있으면 됩니다.

방법은 2가지입니다.

1. 폴더를 그대로 복사하기
2. 원래 위치를 유지하고 링크만 걸기

예시:

```bash
ln -s /path/to/korean-vibe-fonts ~/.codex/skills/korean-vibe-fonts
```

또는 직접 복사:

```bash
cp -R /path/to/korean-vibe-fonts ~/.codex/skills/korean-vibe-fonts
```

이렇게 두면 Codex가 자동으로 읽습니다.

#### Claude Code를 쓴다면

여기가 Codex와 다른 부분입니다.

하지만 이 패키지가 이상한 게 아니라, **Claude Code의 일반적인 방식 자체가 Codex와 다르기 때문**입니다.

Claude Code는 보통 Codex처럼 "스킬 폴더를 직접 설치"하지 않고, `~/.claude/agents/` 또는 `.claude/agents/` 안에 **서브에이전트 Markdown 파일**을 등록해서 씁니다.

그래서 이 패키지에서는 그 방식에 맞춰, Claude Code용 파일을 자동으로 만들어주는 스크립트를 함께 넣었습니다.

전역으로 쓰고 싶다면:

```bash
python3 /path/to/korean-vibe-fonts/scripts/render_claude_agent.py \
  --output ~/.claude/agents/korean-vibe-fonts.md
```

현재 프로젝트에서만 쓰고 싶다면:

```bash
mkdir -p .claude/agents
python3 /path/to/korean-vibe-fonts/scripts/render_claude_agent.py \
  --output .claude/agents/korean-vibe-fonts.md
```

즉:

- Codex의 일반 방식: `~/.codex/skills/` 안에 폴더 두기
- Claude Code의 일반 방식: `.claude/agents/*.md` 파일 만들기

이 패키지는 두 방식 모두 지원하도록 만든 것입니다.

참고 문서:

- [Claude Code subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

#### 다른 AI 도구를 쓴다면

그 도구가 Codex 스킬이나 Claude Code 서브에이전트를 바로 지원하지 않아도 괜찮습니다.

이 파일부터 시작하면 됩니다.

- [adapters/generic-system-prompt.md](./adapters/generic-system-prompt.md)

가능하면 아래 파일도 같이 보여주면 추천 품질이 더 좋아집니다.

- `references/font_catalog.json`
- `references/font_decision_guide.json`
- `references/fonts_archive_commercial.json`
- `references/vibe_presets.md`
- `scripts/recommend_font.py`

## 🎨 어떤 상황에 잘 맞나요?

예를 들면:

- AI SaaS 랜딩 페이지
- 정보가 많은 대시보드
- 부드러운 금융/헬스케어 온보딩
- 배민 느낌의 로컬 캠페인
- 개발자 포트폴리오
- 프리미엄 브랜드 소개 페이지
- 차분한 에디토리얼 페이지
- 귀엽고 밝은 커뮤니티 서비스
- 강한 이벤트 / 캠페인 페이지

## 🗣️ 이렇게 말하면 됩니다

AI에게 아래처럼 요청해보세요.

- "한글 웹폰트 추천해줘. AI 스타트업 랜딩 느낌이야."
- "정보 많은 관리자 화면에는 어떤 폰트 조합이 좋아?"
- "딱딱한 핀테크를 좀 부드럽게 보이게 하는 폰트 골라줘."
- "브랜드 스토리 페이지에 어울리는 폰트 골라줘."
- "귀엽고 친근한 커뮤니티 앱 느낌으로 추천해줘."
- "개발자 포트폴리오에 맞는 한글 폰트 조합 줘."
- "상업적으로 써도 괜찮은 한글 웹폰트로 골라줘."

## ⚡ 바로 테스트해보고 싶다면

터미널에서 아래처럼 실행할 수 있습니다.

```bash
python3 scripts/recommend_font.py --theme "AI SaaS 랜딩 페이지"
python3 scripts/recommend_font.py --theme "차분한 에디토리얼 포트폴리오"
python3 scripts/recommend_font.py --theme "귀엽고 발랄한 커뮤니티 앱"
```

그러면 보통 이런 결과가 나옵니다.

- 추천 폰트 조합
- 왜 잘 맞는지 짧은 설명
- `<link>` 태그
- CSS 변수
- 대안 폰트 1~3개

## 🔤 전체 폰트 리스트

현재 이 패키지에 들어 있는 전체 폰트는 아래와 같습니다.

소개 페이지에는 아래 두 목록을 합쳐 표시합니다.

- [references/font_catalog.json](./references/font_catalog.json)의 큐레이션 폰트 35개
- [references/fonts_archive_commercial.json](./references/fonts_archive_commercial.json)의 fonts-archive 확장 폰트 429개

### 본문과 제목에 두루 쓰기 좋은 폰트

- `Pretendard Variable`: 가장 무난한 현대적 기본값. 제품형 UI, 랜딩, 포트폴리오에 잘 맞습니다.
- `Wanted Sans Variable`: 고민 없이 깔면 중간 이상은 가는 현대적 UI 산스입니다.
- `SUIT Variable`: 이름값 하는 UI 본문용 폰트입니다. 폭이 단정해서 화면에 정보를 깔끔하게 넣기 좋습니다.
- `NanumSquare Neo`: 직선적이고 브랜드 힘이 강합니다. 메인 타이틀과 카드 UI에 특히 좋습니다.
- `NanumSquare`: 반듯하고 친근합니다. 스타트업, 커뮤니티, 모바일 화면에 잘 어울립니다.
- `NanumGothic`: 익숙하고 안정적인 본문용입니다. 공지, 고객지원, 문서형 페이지에 안전합니다.
- `Gmarket Sans`: 세련되고 깔끔한 브랜드 인상입니다. 이커머스, 모바일 프로모션, 스타트업 랜딩에 잘 맞습니다.
- `Spoqa Han Sans Neo`: UI/UX에 특히 강합니다. 숫자와 정보 가독성이 좋아 제품형 서비스와 대시보드에 잘 맞습니다.
- `Goorm Sans`: 한글과 영문의 균형이 좋습니다. 개발자 제품, 테크 랜딩, 깔끔한 서비스 UI에 잘 어울립니다.
- `IBM Plex Sans KR`: 공학적이고 차분합니다. B2B, 개발자 도구, 데이터 제품에 잘 맞습니다.
- `LINE Seed Sans KR`: 둥근 느낌이 좋습니다. 딱딱한 업종에 쓰면 화면이 한결 부드러워 보입니다.
- `Noto Sans KR`: 글로벌 서비스에 쓰기 좋은 중립적 기본값입니다. 다국어 환경에서도 안정적입니다.
- `MaruBuri`: 부드럽고 온기 있는 부리체입니다. 브랜드 스토리와 장문 콘텐츠에 좋습니다.
- `Hahmlet`: 문학적이고 우아합니다. 프리미엄 에디토리얼이나 전시형 페이지에 잘 맞습니다.
- `Noto Serif KR`: 정갈하고 공신력 있는 부리체입니다. 기관형, 정책형, 신뢰형 페이지에 좋습니다.
- `Gowun Dodum`: 부드럽고 잔잔합니다. 웰니스, 라이프스타일, 커뮤니티에 잘 어울립니다.
- `Gowun Batang`: 시적인 여백감이 있습니다. 에세이, 감성 브랜드 저널, 차분한 포트폴리오에 좋습니다.
- `NanumSquareRound`: 동글고 경쾌합니다. 교육, 가족형 서비스, 캐주얼 커뮤니티에 잘 맞습니다.

### 제목용으로 특히 강한 폰트

- `Black Han Sans`: 존재감이 강한 타이틀용 폰트입니다. 포스터, 이벤트, 캠페인 히어로에 좋습니다.
- `Do Hyeon`: 배민 계열의 좁고 단단한 제목용 폰트입니다. 배너, 게임, 이커머스 프로모션에 강합니다.
- `Yeon Sung`: 배민 연성체 계열의 따뜻한 손글씨 무드입니다. 음식 브랜드, 동네 가게, 친근한 후기 섹션에 좋습니다.
- `Kirang Haerang`: 배민 기랑해랑체 계열의 장난스러운 손글씨입니다. 캐주얼한 푸드 이벤트와 밝은 캠페인 포인트에 좋습니다.
- `BM Kkubulim`: 배민 꾸불림체 계열의 물결치는 제목용 폰트입니다. 장난스러운 푸드 이벤트와 엉뚱한 한 줄 포인트에 좋습니다.
- `BM Hanna 11yrs`: 배민 한나체 계열의 대표적인 굵은 제목용 폰트입니다. 푸드 캠페인, 동네 가게, 생활형 브랜드 타이틀에 좋습니다.
- `BM Hanna Air`: 한나체의 가벼운 본문/제목 짝입니다. 배민다운 온도는 살리되 과하게 소리치지 않는 설명문에 좋습니다.
- `BM Hanna Pro`: 더 또렷하게 다듬은 배민 제목용 폰트입니다. 브랜드 타이틀, 메뉴판, 짧은 혜택 카피에 힘이 있습니다.
- `BM Euljiro`: 을지로 간판에서 온 레트로 붓글씨 무드입니다. 골목, 로컬 푸드, 문화 캠페인에 강합니다.
- `BM Euljiro 10 Years Later`: 오래된 간판처럼 거친 질감이 있는 배민 디스플레이 폰트입니다. 한 줄 레트로 타이틀에 좋습니다.
- `여기어때 잘난체`: 주목도가 높은 제목용 폰트입니다. 여행, 숙박, 생활형 프로모션 타이틀에 특히 잘 붙습니다.
- `Jua`: 배민 주아체 계열의 명랑하고 친근한 제목용 폰트입니다. 음식, 가족형, 밝은 커뮤니티 서비스에 잘 어울립니다.
- `SUITE Variable`: 좁고 기하학적인 제목용 폰트입니다. `SUIT Variable`과 같이 쓰면 화면이 정돈돼 보입니다.

### 코드용 폰트

- `NanumGothicCoding (D2Coding)`: 코드 블록과 터미널에 가장 안정적입니다. 한글, 영문, 기호 구분이 좋습니다.

### 포인트용 손글씨/개성 폰트

- `NanumPen`: 메모, 후기, 짧은 강조 문구에 잘 맞습니다.
- `Gaegu`: 낙서 같은 자유로움이 있어서 실험적이고 장난스러운 포인트용으로 좋습니다.
- `Single Day`: 정돈된 손글씨 느낌으로 일기, 후기, 작은 브랜드 메모 섹션에 잘 어울립니다.

큐레이션된 메타데이터와 공식 링크는 [references/font_catalog.json](./references/font_catalog.json)에서 볼 수 있습니다.

fonts-archive 전체 스윕 결과는 [references/fonts_archive_commercial.json](./references/fonts_archive_commercial.json)에 따로 정리했습니다. 현재 웹폰트 CSS와 상업 사용/open-license 신호가 같이 확인된 429개 repo를 포함하고, 조건부/비상업/불명확/구매 필요 신호가 있는 135개 repo는 제외했습니다.

## 🔎 추가된 폰트 출처

큐레이션 폰트는 각 항목마다 원본 페이지와 라이선스 페이지를 기록해두었습니다. 이번 업데이트에서 사용한 주요 출처는 아래와 같습니다.

| 출처 | 포함 폰트 / 범위 | 링크 |
| --- | --- | --- |
| Pretendard | `Pretendard Variable` | [원본](https://github.com/orioncactus/pretendard), [라이선스](https://github.com/orioncactus/pretendard/blob/main/LICENSE) |
| Wanted Lab | `Wanted Sans Variable` | [원본](https://github.com/wanteddev/wanted-sans), [라이선스](https://github.com/wanteddev/wanted-sans/blob/main/OFL.txt) |
| SUNN | `SUIT Variable`, `SUITE Variable` | [SUIT](https://github.com/sun-typeface/SUIT), [SUITE](https://github.com/sun-typeface/SUITE) |
| NAVER 한글한글 아름답게 | `NanumSquare Neo`, `NanumSquare`, `NanumGothic`, `NanumSquareRound`, `NanumGothicCoding`, `NanumPen`, `MaruBuri` | [원본/라이선스](https://hangeul.naver.com/font) |
| Google Fonts | `IBM Plex Sans KR`, `Noto Sans KR`, `Noto Serif KR`, `Hahmlet`, `Gowun Dodum`, `Gowun Batang`, `Black Han Sans`, `Gaegu`, `Single Day`, 일부 배민 계열 Google Fonts 호스팅 폰트 | [Google Fonts](https://fonts.google.com/), [라이선스 안내](https://developers.google.com/fonts/faq) |
| 우아한형제들 배달의민족 글꼴 | `BM Kkubulim`, `BM Hanna 11yrs`, `BM Hanna Air`, `BM Hanna Pro`, `BM Euljiro`, `BM Euljiro 10 Years Later`, `Do Hyeon`, `Yeon Sung`, `Kirang Haerang`, `Jua` | [원본](https://www.woowahan.com/fonts), [라이선스](https://www.woowahan.com/fonts/license) |
| fonts-archive | 웹폰트 CSS와 상업 사용/open-license 신호가 확인된 429개 repo. 배민 계열, 학교안심, 조선일보명조 등 확장 폰트 포함 | [organization](https://github.com/fonts-archive), [필터링된 카탈로그](./references/fonts_archive_commercial.json) |
| Spoqa | `Spoqa Han Sans Neo` | [원본/라이선스](https://spoqa.github.io/spoqa-han-sans/) |
| goorm | `Goorm Sans` | [원본/라이선스](https://goorm-sans.goorm.io/) |
| LINE | `LINE Seed Sans KR` | [원본](https://seed.line.me/), [라이선스](https://github.com/line/seed/blob/main/OFL.txt) |
| Gmarket | `Gmarket Sans` | [원본/라이선스](https://corp.gmarket.com/fonts/) |
| 여기어때 | `여기어때 잘난체` | [원본](https://www.goodchoice.kr/font/mobile), [라이선스 PDF](https://image.goodchoice.kr/images/jalnan_font/jalnan-font-190124ver.pdf) |

주의: 이 패키지는 추천을 위해 상업 사용/open-license 신호를 기록합니다. 폰트 파일 자체를 재배포하거나 중요한 상용 브랜드 시스템에 넣기 전에는 각 카탈로그 항목의 원본 라이선스 페이지를 다시 확인하세요.

## ❤️ 이 패키지가 다른 디자인 스킬과 다른 점

일반적인 디자인 스킬은 보통 이렇게 말합니다.

- "예쁜 폰트를 골라라"
- "너무 흔한 폰트는 피하라"

이 패키지는 거기서 한 걸음 더 갑니다.

- 한글 웹폰트에 집중하고
- 상업용 사용 가능성을 직접 체크하고
- 분위기와 폰트를 연결해주고
- 바로 붙여 넣을 코드까지 같이 줍니다.

## 🔒 폰트는 아무거나 넣지 않았어요

큐레이션 목록은 공식 출처와 라이선스 페이지를 기준으로 확인한 폰트만 넣었습니다. fonts-archive 확장 목록은 README 또는 라이선스 문구에서 상업 사용/open-license 신호가 명확하고, 실제 웹폰트 CSS 경로가 있는 repo만 포함했습니다.

새 폰트를 추가하고 싶다면 꼭 확인하세요.

- 공식 라이선스 문서
- 실제로 적용 가능한 공식 stylesheet URL, CDN 경로, 또는 공식 셀프호스팅 안내

## 🌱 가장 추천하는 시작 방법

가장 쉽게 쓰려면 이렇게 하세요.

1. Codex 또는 Claude Code에 이 패키지를 연결합니다.
2. 원하는 분위기를 한 문장으로 말합니다.
3. 나온 폰트 추천과 코드를 그대로 사용합니다.

정말 이 3단계면 충분합니다.

## 📍 한 줄 요약

이 패키지는 "한글 폰트 감각 좋은 AI 도우미"입니다.  
분위기를 말하면, 어울리는 상업용 한글 웹폰트와 적용 코드까지 같이 줍니다 ✨
