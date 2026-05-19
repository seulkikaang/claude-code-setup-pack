# Global CLAUDE.md

## 언어
- 사용자와의 대화: 한국어
- 코드, 커밋 메시지, 변수명: 영어

## 작업 스타일
- 간결하게 답변, 불필요한 요약 생략
- 큰 작업은 plan mode 먼저
- 디자인 결정은 시각적 비교로 확인 받기

## 작업 원칙
- **막히면 재계획**: 진행이 꼬이면 즉시 멈추고 plan mode로 돌아가기
- **자율적 버그 수정**: 버그 리포트 받으면 로그/에러/테스트 확인 후 직접 해결. 사용자에게 되묻지 않기
- **우아함 자문**: 비자명한 변경은 "더 나은 방법이 있나?" 한 번 자문. 단순한 수정은 과잉 설계 금지
- **완료 전 증명**: 태스크 완료 선언 전 반드시 동작 증명 (테스트 통과, 로그 확인, 데모)
- **근본 원인 해결**: 임시 수정 금지. 원인을 찾아 제대로 고치기
- **최소 변경 범위**: 필요한 코드만 수정. 부수적 리팩토링/정리는 요청 시에만

## Dev Docs 시스템
대규모 태스크(3단계 이상) 시작 시 dev docs를 생성하여 컨텍스트 손실을 방지한다.

시작할 때:
1. `dev/active/[task-name]/` 디렉토리 생성
2. 세 파일 생성:
   - `[task-name]-plan.md` - 승인된 계획 전문
   - `[task-name]-context.md` - 핵심 파일, 의사결정, 의존성
   - `[task-name]-tasks.md` - 단계별 체크리스트
3. context 파일에 'Last Updated' 타임스탬프 포함

이어서 진행할 때:
- `dev/active/` 에서 기존 태스크 확인 후 세 파일 모두 읽고 진행
- 컨텍스트 15% 이하 시 `/dev-docs-update` 실행

## 스킬/에이전트 자동 활용
- 설치된 스킬과 에이전트를 **사용자가 명시적으로 언급하지 않아도** 작업 유형에 따라 적극 활용한다
- 없는 스킬이 필요하면: `find-skill` 스킬로 검색 → 웹 검색 → `skill-creator`로 생성
- 복잡한 작업은 서브에이전트에 위임, 병렬 가능하면 git worktree 활용

### 작업→스킬/에이전트 자동 매핑 (반드시 따른다)
| 작업 유형 | 자동 활성화 스킬 | 자동 활성화 에이전트 |
|-----------|-----------------|---------------------|
| 프론트엔드/UI 개발 | taste-skill, soft-skill, frontend-design, frontend-patterns | Frontend Developer, UX Architect |
| UI 리디자인/개선 | redesign-skill, taste-skill | UX Architect, Accessibility Auditor |
| 새 기능 구현 | tdd-workflow, test-driven-development | planner, tdd-guide |
| 버그 수정 | systematic-debugging | tdd-guide |
| 코드 완료 후 | requesting-code-review | code-reviewer |
| API 설계/개발 | api-design, backend-patterns | Backend Architect, API Tester |
| 데이터베이스 | postgres-patterns, database-migrations | database-reviewer |
| 보안 관련 | security-review | security-reviewer |
| Python 코드 | python-patterns, python-testing | python-reviewer |
| Go 코드 | golang-patterns, golang-testing | go-reviewer |
| 배포/인프라 | deployment-patterns, docker-patterns | DevOps Automator |
| 비디오/Remotion | remotion-best-practices | - |
| PPTX/프레젠테이션 | pptx, frontend-slides | - |
| 계획/설계 | writing-plans, brainstorming | planner, architect |
| 코드 정리 | - | refactor-cleaner |
| 빌드 에러 | - | build-error-resolver |

### 자동 활성화 원칙
- 1%라도 관련 스킬이 있을 수 있으면 **반드시** Skill 도구로 활성화한다
- 에이전트는 작업 복잡도에 따라 적극적으로 서브에이전트로 위임한다
- 사용자가 "만들어줘", "고쳐줘", "리뷰해줘" 등 행동 동사를 쓰면 해당 워크플로우 스킬을 자동 활성화
- 코드를 작성하면 반드시 code-reviewer 에이전트 실행

## 금지 사항
- 기존 패턴 무시하고 새 패턴 도입 금지
- 빌드 에러 남긴 채 작업 완료 금지
- 'unrelated errors'라며 에러 무시 금지
- dev docs 없이 대규모 태스크 시작 금지

## 상황별 워크플로우 참조
| 상황 | 실행 순서 |
|------|-----------|
| 새 기능 개발 | plan mode → dev-docs → TDD → 구현 |
| 버그 수정 | 로그/에러 확인 → 근본 원인 → 수정 → 검증 |
| 코드 리뷰 | /code-review → /verify |
| 대규모 리팩토링 | plan mode → 서브에이전트 병렬 → 검증 |
| 세션 마무리 | /dev-docs-update → /learn |

## 규칙 참조
상세 코딩/테스트/보안/워크플로 규칙은 `~/.claude/rules/` 참조.
