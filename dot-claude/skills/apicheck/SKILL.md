---
name: apicheck
description: "Analyze and report the current API integration status of the project. Use this skill whenever the user runs /apicheck, asks about API connections, wants to know what's integrated vs placeholder, or checks backend readiness. Also trigger when the user asks things like 'what APIs are connected', 'is the backend ready', 'integration status', or 'what needs API work'."
---

# API Integration Status Check

When invoked, scan the current project and produce a concise Korean-language report on API integration status.

## What to scan

1. **Data layer**: How is data currently stored? (localStorage, Zustand, API calls, etc.)
2. **External service references**: Look for imports/references to external SDKs or APIs (Braze, Appsflyer, Naver Commerce API, ad platform APIs, etc.)
3. **API routes**: Check `src/app/api/` for any Next.js API routes
4. **Environment variables**: Check `.env*` files and `process.env` references for API keys/endpoints
5. **Fetch/axios calls**: Search for `fetch(`, `axios.`, or other HTTP client usage in the codebase
6. **Store actions**: Look at the Zustand store for any async actions or API-calling patterns
7. **Mock/sample data**: Identify files that use hardcoded sample data instead of real API responses
8. **Tool outputs**: Check if the tools system (`toolOutputs`) has any API integration points

## How to scan

Use these commands to gather data quickly:

```bash
# API routes
find src/app/api -type f 2>/dev/null || echo "No API routes directory"

# External fetch calls
grep -rn "fetch(" src/ --include="*.ts" --include="*.tsx" | grep -v node_modules | grep -v ".next" | head -20

# Axios usage
grep -rn "axios" src/ --include="*.ts" --include="*.tsx" | head -10

# Environment variables
cat .env .env.local .env.development 2>/dev/null || echo "No .env files"
grep -rn "process.env" src/ --include="*.ts" --include="*.tsx" | head -10

# SDK imports (Braze, Appsflyer, etc.)
grep -rn "from.*braze\|from.*appsflyer\|from.*@naver" src/ --include="*.ts" --include="*.tsx" | head -10

# Store async patterns
grep -n "async\|await\|fetch\|axios" src/lib/store.ts | head -10

# Sample/mock data files
ls src/data/ 2>/dev/null
```

## Report format

Output the report in this exact structure (Korean):

```
## API 연동 현황 리포트

### 현재 상태: [emoji] [한줄 요약]

### 데이터 레이어
- **저장 방식**: [localStorage / API / hybrid]
- **상태 관리**: [Zustand / Redux / etc.]
- **영속화**: [localStorage persist / 서버 동기화 / 없음]

### 외부 서비스 연동

| 서비스 | 상태 | 비고 |
|--------|------|------|
| Braze (CRM) | [emoji] 미연동 / 연동 완료 / 부분 연동 | [상세] |
| Appsflyer (어트리뷰션) | [emoji] | [상세] |
| 네이버 커머스 API | [emoji] | [상세] |
| 광고 플랫폼 (네이버/메타/구글) | [emoji] | [상세] |

### API 엔드포인트
- **Next.js API Routes**: [N개 / 없음]
- **외부 API 호출**: [N개 / 없음]
- **환경 변수**: [N개 설정됨 / 미설정]

### 샘플 데이터 의존성
[하드코딩된 샘플 데이터를 사용하는 파일 목록]

### API 연동 시 필요한 작업
[우선순위별 TODO 리스트 — 실제 API로 전환하려면 무엇을 해야 하는지]

### 연동 준비도 점수: [N/10]
[점수에 대한 간단한 설명]
```

## Status emojis
- Connected/ready: `✅`
- Partially connected: `🔶`  
- Not connected (placeholder/mock): `❌`
- Unknown/needs investigation: `❓`

## Important notes
- Be factual — only report what you actually find in the code
- Don't guess about integrations that aren't evidenced in the codebase
- The "필요한 작업" section should be actionable and specific to this project
- Keep the report concise — no longer than what fits on one screen
