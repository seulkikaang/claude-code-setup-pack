# 🚀 Claude Code 셋업 팩

> Claude Code에 **'프로 개발자 모드'** 를 한 번에 입혀주는 설정 팩이에요. ☁️
> zip 하나를 풀고 설치 스크립트만 돌리면, 87개 스킬 + 80+개 에이전트 + 45개 슬래시 명령어 + 5개 자동 훅이 자동으로 깔립니다.

비개발자도 따라할 수 있도록 가능한 한 쉽게 풀어 썼습니다. 🙌

---

## 📦 이 레포에 들어있는 것

| 파일 | 용도 |
|---|---|
| `claude-config-pack-mac.zip` | 🍎 macOS / Linux 사용자용 설정 팩 |
| `claude-config-pack-windows.zip` | 🪟 Windows 사용자용 설정 팩 |
| `README.md` | 지금 보고 있는 이 문서 |

각 zip 안에는:
- `dot-claude/` - `~/.claude/` 폴더에 들어갈 설정 묶음 (CLAUDE.md, skills, agents, commands, rules, scripts, settings.json)
- `install.sh` (Mac/Linux) 또는 `install.ps1` (Windows) - 설치 자동화 스크립트

---

## 🤔 이게 뭔가요? (1분 요약)

Claude Code는 그냥 쓰면 '아주 똑똑한 비서'에요.
이 설정 팩을 깔면, Claude Code가 **'시니어 개발팀'** 처럼 동작합니다. 👨‍💻👩‍💻

- 📝 **스킬(Skill)** = "이 작업은 이렇게 해라" 레시피북 (87개)
- 🤖 **에이전트(Agent)** = 특정 역할 전문가 분신 (80+개, 예: 코드 리뷰어, 보안 전문가, 디자이너)
- ⚡ **슬래시 명령어(/command)** = 한 번에 실행되는 워크플로우 (45개, 예: `/code-review`, `/tdd`)
- 🔔 **훅(Hook)** = 특정 이벤트에 자동 실행되는 스크립트 (예: 세션 시작 시 git 상태 자동 표시)

---

## ⚡ 설치하기 (가장 쉬운 방법)

### 🍏 Mac / Linux

1. 이 레포에서 `claude-config-pack-mac.zip` 다운로드 ([여기 클릭](./claude-config-pack-mac.zip))
2. 다운로드 폴더에 zip 파일이 들어왔는지 확인 (압축 풀지 마세요!)
3. Claude Code 앱(터미널)을 열고, **아래 프롬프트를 그대로 복붙**:

> 💡 **TIP**: `@` 키를 누르면 파일을 첨부할 수 있어요. zip 파일을 끌어다 넣어도 됩니다.

```
~/Downloads/claude-config-pack-mac.zip 이 파일에 들어있는
Claude Code 글로벌 설정을 내 ~/.claude/에 적용해줘.

zip을 압축 해제하고, 그 안의 install.sh를 실행한 후,
실행 결과를 보여줘.

그 다음 안내에 나오는 플러그인들도 설치해줘.
```

4. Claude가 알아서 압축 해제 → 백업 → 설치까지 다 해줍니다. ✨
5. 끝나면 Claude Code를 한 번 재시작 해주세요.

---

### 🪟 Windows

1. 이 레포에서 `claude-config-pack-windows.zip` 다운로드 ([여기 클릭](./claude-config-pack-windows.zip))
2. 다운로드 폴더에 zip 파일이 들어왔는지 확인
3. Claude Code 앱을 열고, 아래 프롬프트를 그대로 복붙:

```
%USERPROFILE%\Downloads\claude-config-pack-windows.zip 이 파일에 들어있는
Claude Code 글로벌 설정을 내 %USERPROFILE%\.claude\ 폴더에 적용해줘.

zip을 압축 해제하고, 그 안의 install.ps1을
powershell -ExecutionPolicy Bypass -File install.ps1 명령으로 실행한 후,
실행 결과를 보여줘.

그 다음 안내에 나오는 플러그인들도 설치해줘.
```

4. 끝나면 Claude Code를 재시작 해주세요. 🎉

---

## 🛟 안전장치

설치 스크립트는 **기존 `~/.claude/` 폴더를 자동 백업**합니다.
- 백업 위치: `~/.claude-backup-날짜시간/`
- 문제가 생기면 백업 폴더를 그대로 원래 위치로 복원하면 끝.

---

## 🔑 (선택) Gemini API 키 설정

AI 이미지 생성 기능을 쓰려면 Gemini API 키가 필요합니다. 없어도 다른 기능은 다 동작해요.

1. [Google AI Studio](https://aistudio.google.com) 접속 → 구글 로그인
2. 좌측 메뉴 `API keys` → `Create API key` 클릭
3. 키 복사 후, `~/.claude/settings.json` (Mac) 또는 `%USERPROFILE%\.claude\settings.json` (Windows) 열기
4. `"GEMINI_API_KEY": ""` 따옴표 사이에 키 붙여넣기

또는 Claude에게 그냥 부탁:
```
~/.claude/settings.json 열어서 GEMINI_API_KEY에 이 키 넣어줘: [키 붙여넣기]
```

---

## 📚 설치되는 것들

### 🎨 스킬 87개 — '이 작업은 이렇게 해라' 레시피북

| 분야 | 대표 스킬 |
|---|---|
| 🧠 **개발 방법론** | brainstorming, tdd-workflow, systematic-debugging, verification-loop, writing-plans, executing-plans, search-first |
| 🖥️ **프론트엔드** | frontend-design, frontend-patterns, frontend-slides, taste-skill, soft-skill, redesign-skill, output-skill |
| ⚙️ **백엔드 & API** | backend-patterns, api-design, postgres-patterns, database-migrations |
| 🐍 **Python** | python-patterns, python-testing, django-patterns, django-security, django-tdd |
| 🐹 **Go** | golang-patterns, golang-testing |
| ☕ **Java/Spring** | springboot-patterns, springboot-security, springboot-tdd, jpa-patterns |
| 🍎 **Swift/Apple** | swiftui-patterns, swift-concurrency-6-2, liquid-glass-design, foundation-models-on-device |
| 🔐 **보안** | security-review, security-scan |
| 🚢 **배포** | deployment-patterns, docker-patterns |
| 🧪 **E2E 테스트** | e2e-testing |
| 🤖 **에이전트 자동화** | agentic-engineering, autonomous-loops, eval-harness, cost-aware-llm-pipeline |
| 📈 **콘텐츠/마케팅** | content-engine, article-writing, market-research, investor-materials |
| 🛠️ **유틸리티** | pptx, pptx-to-markdown, find-skills, plankton-code-quality, remotion-best-practices |

전체 목록은 설치 후 `~/.claude/skills/` 폴더에서 확인할 수 있어요.

### 🧑‍💼 에이전트 80+개 — 역할별 전문가 분신

| 분야 | 대표 에이전트 |
|---|---|
| 🏗️ **코어 엔지니어링** | architect, planner, code-reviewer, build-error-resolver, security-reviewer, tdd-guide, e2e-runner |
| 💻 **풀스택** | engineering-backend-architect, engineering-frontend-developer, engineering-mobile-app-builder, engineering-ai-engineer, engineering-devops-automator |
| 🍏 **Apple/공간컴퓨팅** | macos-spatial-metal-engineer, visionos-spatial-engineer |
| 🎨 **디자인** | design-ui-designer, design-ux-architect, design-brand-guardian, design-image-prompt-engineer |
| 📣 **마케팅** | marketing-content-creator, marketing-instagram-curator, marketing-tiktok-strategist, marketing-growth-hacker |
| ✅ **테스팅/품질** | testing-api-tester, testing-evidence-collector, testing-reality-checker, testing-accessibility-auditor |
| 📊 **프로젝트 관리** | project-manager-senior, project-management-experiment-tracker |
| 💼 **비즈니스 지원** | chief-of-staff, support-executive-summary-generator, support-finance-tracker |
| 🔄 **오케스트레이션** | agents-orchestrator, loop-operator, harness-optimizer |

### ⚡ 슬래시 명령어 45개

| 명령어 | 용도 |
|---|---|
| `/plan` | 구현 계획 수립 (복잡한 작업 전 필수) |
| `/dev-docs` `/dev-docs-update` | 작업 문서 생성/갱신 (컨텍스트 손실 방지) |
| `/tdd` | 테스트 주도 개발 강제 |
| `/code-review` | 코드 리뷰 (보안, 품질, 일관성) |
| `/build-fix` | 빌드 에러 자동 수정 |
| `/verify` | 구현 검증 |
| `/e2e` | E2E 테스트 생성/실행 |
| `/brainstorm` | 창의적 작업 전 아이디어 탐색 |
| `/refactor-clean` | 데드 코드 정리 |
| `/learn` | 세션에서 재사용 패턴 추출 |
| `/checkpoint` | 진행상황 저장 |
| `/orchestrate` `/multi-*` | 멀티 에이전트 협업 |
| `/go-build` `/go-test` `/go-review` `/python-review` | 언어별 워크플로우 |

### 🔔 자동 훅 5개

| 훅 | 타이밍 | 하는 일 |
|---|---|---|
| `SessionStart` | 세션 시작 시 | git 브랜치/변경 파일/진행 중 태스크 자동 표시 |
| `UserPromptSubmit` | 프롬프트 입력 시 | 키워드 기반 스킬 자동 추천 |
| `PostToolUse` | 파일 편집 후 | 편집 파일 추적/로깅 |
| `Stop` | 세션 종료 시 | (비어있음 - 필요시 `/build-fix` 수동 실행) |
| `PreCompact` | 컨텍스트 압축 전 | 대화 내용 자동 백업 |

---

## 🌱 스킬/에이전트 출처

이 팩에 들어간 스킬과 에이전트는 다음 오픈소스 프로젝트에서 가져왔거나 영감을 받았습니다. 모든 원본 저작자들께 감사드립니다. 🙏

| 출처 | 가져온 항목 |
|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) (Anthropic 공식) | `frontend-design`, `pptx`, `pptx-to-markdown`, `skill-creator`, `brainstorming`, `using-superpowers`, `writing-skills`, `using-git-worktrees`, `requesting-code-review`, `receiving-code-review`, `verification-before-completion`, `systematic-debugging`, `dispatching-parallel-agents`, `subagent-driven-development`, `executing-plans`, `writing-plans`, `finishing-a-development-branch`, `test-driven-development` 등 (superpowers 계열) |
| [ECC (Everything Claude Code)](https://github.com/anthropics/skills) | `tdd-workflow`, `verification-loop`, `coding-standards`, `python-patterns`, `python-testing`, `golang-patterns`, `golang-testing`, `springboot-patterns`, `springboot-security`, `springboot-tdd`, `springboot-verification`, `django-patterns`, `django-security`, `django-tdd`, `django-verification`, `java-coding-standards`, `jpa-patterns`, `cpp-coding-standards`, `cpp-testing`, `swiftui-patterns`, `swift-concurrency-6-2`, `swift-actor-persistence`, `swift-protocol-di-testing`, `liquid-glass-design`, `foundation-models-on-device`, `frontend-patterns`, `backend-patterns`, `api-design`, `postgres-patterns`, `database-migrations`, `clickhouse-io`, `docker-patterns`, `deployment-patterns`, `e2e-testing`, `security-review`, `agentic-engineering`, `ai-first-engineering`, `autonomous-loops`, `continuous-agent-loop`, `agent-harness-construction`, `eval-harness`, `enterprise-agent-ops`, `cost-aware-llm-pipeline`, `nanoclaw-repl`, `ralphinho-rfc-pipeline`, `configure-ecc`, `continuous-learning`, `continuous-learning-v2`, `skill-stocktake`, `find-skills`, 그 외 다수 |
| [obra/superpowers](https://github.com/obra/superpowers) | superpowers 시리즈 일부 |
| 커뮤니티 (Awesome Claude Code) | `taste-skill`, `soft-skill`, `redesign-skill`, `output-skill`, `security-scan` (AgentShield), `plankton-code-quality` (Plankton) |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | `remotion-best-practices` (Remotion 팀 공식) |
| [Nutrient](https://www.nutrient.io/) | `nutrient-document-processing` (DWS API) |
| 콘텐츠/마케팅 시리즈 | `content-engine`, `article-writing`, `market-research`, `investor-outreach`, `investor-materials` |
| 에이전트 카탈로그 | 80+개 에이전트는 contains-studio/awesome-claude-agents 등 다양한 큐레이션 컬렉션에서 모음 |

> 📝 각 스킬/에이전트 파일 안의 `name`/`description`/`license` 필드를 직접 열어보면 원본 출처와 라이선스를 더 정확히 확인할 수 있어요.

---

## 🔌 추천 MCP (Model Context Protocol) 서버

MCP = Claude Code에 외부 서비스를 끼우는 '플러그'. 이 팩에 자동 포함되진 않고, 각자 API 키가 필요해서 직접 설치합니다.

Claude Code에 그대로 입력하면 됩니다:

```
Google Calendar MCP를 설치해줘. /install-mcp google-calendar
PostHog MCP를 설치해줘. /install-mcp posthog
Gmail MCP를 설치해줘. /install-mcp gmail
```

이미 포함된 플러그인: **Notion**, **Playwright** (API 키만 설정하면 동작)

---

## 🎯 실전 워크플로우

### 🆕 새 기능 개발할 때
```
/plan → /dev-docs → /tdd → 구현 → /code-review → /verify
```

### 🐛 버그 수정할 때
```
버그 설명 → 자동 분석 → 근본 원인 → 테스트 추가 → /verify
```

### 🌙 세션 마무리할 때
```
/dev-docs-update → /learn → (다음 세션) "dev/active/ 에서 이어서 진행해줘"
```

---

## ⌨️ 키보드 단축키 (터미널)

| 단축키 | 기능 |
|---|---|
| `Return` | 줄바꿈 (전송 아님) |
| `Option/Alt + Return` | 메시지 전송 |
| `Esc` | 응답 중단 |
| `Option/Alt + ↑/↓` | 이전/다음 프롬프트 |
| `Option/Alt + T` | 확장 사고 모드 토글 |
| `Ctrl + O` | 사고 과정 표시 토글 |
| `Option/Alt + X` | 자동 수락 모드 토글 |
| `@` | 파일/URL/디렉토리 첨부 |
| `!` | Bash 결과를 컨텍스트에 추가 |
| `#` | 파일 내용을 프롬프트에 삽입 |
| `/compact` | 대화 압축 |
| `/clear` | 대화 초기화 |
| `/model` | 모델 변경 |
| `/fast` | 빠른 모드 |
| `/cost` | 비용 확인 |

---

## 💡 꿀팁

### 프로젝트별 CLAUDE.md 만들기
```
이 프로젝트에 맞는 CLAUDE.md를 만들어줘.
기술 스택, 디렉토리 구조, 빌드/테스트 명령어를 포함해줘.
```

### Claude에게 규칙 기억시키기
```
앞으로 이 프로젝트에서는 [규칙]을 지켜줘. CLAUDE.md에 추가해줘.
```

### 컨텍스트 윈도우 관리
- 큰 작업 시작 → `/dev-docs` 로 문서화
- 컨텍스트 줄어들면 → `/dev-docs-update`
- 다음 세션 → `dev/active/ 에서 진행 중인 태스크를 이어해줘`

---

## 🆘 문제가 생기면

- 설치가 꼬였다? → 백업 폴더(`~/.claude-backup-YYYYMMDD-HHMMSS`)를 원래 위치로 복원
- 스킬이 안 나타난다? → Claude Code 재시작
- `jq` 관련 에러 (Mac/Linux) → `brew install jq` 또는 `sudo apt-get install jq`
- Windows PowerShell 실행정책 에러 → 위 안내의 `-ExecutionPolicy Bypass` 옵션 그대로 사용

---

## 📜 라이선스

이 팩 안의 스킬/에이전트는 각각의 원본 저작자가 정한 라이선스를 따릅니다.
대부분 MIT 또는 Apache 2.0 이며, 일부 Anthropic 공식 스킬은 별도 LICENSE.txt 동봉.

이 README와 설치 스크립트는 자유롭게 가져다 쓰셔도 됩니다. 🤝

---

> 만든 이: @marketer.ai.seulki ✨
> 강의에서 만나요! 🙌
