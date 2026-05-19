#!/bin/bash
# skill-activator.sh - UserPromptSubmit 훅
# 프롬프트 키워드 기반으로 관련 스킬 및 에이전트 활성화 힌트를 제공

INPUT=$(cat)

# jq가 없으면 종료
if ! command -v jq &> /dev/null; then
  exit 0
fi

PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty')

if [ -z "$PROMPT" ]; then
  exit 0
fi

SUGGESTIONS=""

# 프론트엔드/UI 관련 키워드
if echo "$PROMPT" | grep -qi -E '(react|component|frontend|프론트|UI|UX|css|layout|tailwind|nextjs|디자인|스타일|애니메이션|animation|responsive|반응형|페이지|화면)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] taste-skill, soft-skill, frontend-design, frontend-patterns"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] Frontend Developer, UX Architect"
fi

# UI 개선/리디자인 키워드
if echo "$PROMPT" | grep -qi -E '(리디자인|redesign|개선|리팩토링.*UI|리뉴얼|업그레이드.*디자인|더 예쁘|더 깔끔)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] redesign-skill, taste-skill"
fi

# 백엔드 관련 키워드
if echo "$PROMPT" | grep -qi -E '(backend|api|controller|service|route|endpoint|백엔드|서버|REST|graphql|middleware)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] backend-patterns, api-design"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] Backend Architect"
fi

# 데이터베이스 관련 키워드
if echo "$PROMPT" | grep -qi -E '(database|db|migration|schema|query|postgres|prisma|sql|디비|supabase|테이블)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] postgres-patterns, database-migrations"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] database-reviewer"
fi

# 테스트 관련 키워드
if echo "$PROMPT" | grep -qi -E '(test|tdd|e2e|playwright|jest|pytest|테스트|검증|커버리지)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] tdd-workflow, test-driven-development, e2e-testing"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] tdd-guide, e2e-runner"
fi

# Python 관련 키워드
if echo "$PROMPT" | grep -qi -E '(python|django|fastapi|flask|파이썬|pip|pytest|\.py)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] python-patterns, python-testing"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] python-reviewer"
fi

# Go 관련 키워드
if echo "$PROMPT" | grep -qi -E '(golang|go test|go build|\.go|고랭)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] golang-patterns, golang-testing"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] go-reviewer, go-build-resolver"
fi

# 보안 관련 키워드
if echo "$PROMPT" | grep -qi -E '(security|보안|취약점|auth|인증|xss|csrf|injection|secret|토큰|token)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] security-review"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] security-reviewer, Security Engineer"
fi

# 배포/인프라 관련 키워드
if echo "$PROMPT" | grep -qi -E '(deploy|docker|ci.?cd|배포|컨테이너|kubernetes|vercel|인프라|infrastructure)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] deployment-patterns, docker-patterns"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] DevOps Automator, Infrastructure Maintainer"
fi

# 디버깅 관련 키워드
if echo "$PROMPT" | grep -qi -E '(debug|bug|error|디버그|버그|에러|오류|안 되|작동.*안|실패)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] systematic-debugging"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] build-error-resolver"
fi

# 계획/설계 관련 키워드
if echo "$PROMPT" | grep -qi -E '(계획|plan|설계|architect|아키텍처|구조|design.*system)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] writing-plans, brainstorming"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] planner, architect"
fi

# 새 기능 구현 키워드
if echo "$PROMPT" | grep -qi -E '(만들어|구현|implement|build|개발|feature|기능.*추가|새.*기능)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] tdd-workflow, test-driven-development"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] planner, tdd-guide"
fi

# 코드 리뷰/정리 키워드
if echo "$PROMPT" | grep -qi -E '(리뷰|review|코드.*확인|정리|cleanup|리팩토링|refactor|dead.*code)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] requesting-code-review"
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] code-reviewer, refactor-cleaner"
fi

# 비디오/Remotion 키워드
if echo "$PROMPT" | grep -qi -E '(remotion|비디오|video|영상|애니메이션.*react)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] remotion-best-practices"
fi

# PPTX/프레젠테이션 키워드
if echo "$PROMPT" | grep -qi -E '(pptx|파워포인트|프레젠테이션|슬라이드|교안|강의.*자료)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [스킬] pptx, pptx-to-markdown"
fi

# 문서 관련 키워드
if echo "$PROMPT" | grep -qi -E '(문서|document|readme|docs|기술.*문서|가이드)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] Technical Writer, doc-updater"
fi

# 성능 관련 키워드
if echo "$PROMPT" | grep -qi -E '(성능|performance|느려|속도|최적화|optimization|benchmark)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] Performance Benchmarker"
fi

# 접근성 관련 키워드
if echo "$PROMPT" | grep -qi -E '(접근성|accessibility|wcag|a11y|스크린.*리더|screen.*reader)'; then
  SUGGESTIONS="$SUGGESTIONS\n- [에이전트] Accessibility Auditor"
fi

# 중복 제거
if [ -n "$SUGGESTIONS" ]; then
  echo -e "관련 스킬/에이전트 힌트:$SUGGESTIONS"
fi
