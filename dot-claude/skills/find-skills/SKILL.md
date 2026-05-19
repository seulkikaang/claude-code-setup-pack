---
name: find-skills
description: 프로젝트에 필요한 Agent Skills를 검색하고 설치하는 메타 스킬. 새로운 기능 구현 전에 항상 이 스킬을 먼저 사용하여 관련 커뮤니티 스킬이 있는지 확인할 것. 'install skill', 'find skill', 'browse skills', '스킬 찾기', '스킬 설치', 또는 새 기능 구현 시작 시 자동 트리거.
---

# Find & Install Skills

기능 구현 전 반드시 관련 커뮤니티 스킬을 탐색하여 고퀄리티 구현을 보장한다.

## 스킬 검색 방법

### 방법 1: npx add-skill (추천)
```bash
# 공식 anthropics/skills에서 검색
npx add-skill anthropics/skills --list

# 특정 스킬 설치
npx add-skill anthropics/skills --skill frontend-design
npx add-skill anthropics/skills --skill skill-creator

# 커뮤니티 레포에서 설치
npx add-skill VoltAgent/awesome-agent-skills --list
npx add-skill affaan-m/everything-claude-code --list
```

### 방법 2: openskills CLI
```bash
npx openskills install anthropics/skills --skill frontend-design
npx openskills install remotion-dev/remotion
npx openskills list
```

### 방법 3: claude install-skill (Claude Code 내장)
```bash
claude install-skill https://github.com/anthropics/skills/tree/main/skills/frontend-design
claude install-skill https://github.com/remotion-dev/remotion/tree/main/packages/skills
```

### 방법 4: Plugin Marketplace
```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

## OSMU 프로젝트용 추천 스킬 맵

### 카드뉴스 생성 시
- `anthropics/skills - frontend-design` (HTML 디자인 퀄리티)
- `anthropics/skills - canvas-design` (비주얼 디자인)
- `op7418/NanoBanana-PPT-Skills` (이미지 생성 참고)

### 블로그/글쓰기 시
- `affaan-m/everything-claude-code - article-writing` (글쓰기 패턴)
- `affaan-m/everything-claude-code - content-engine` (컨텐츠 엔진)
- `AgriciDaniel/claude-seo` (SEO 최적화)
- `blader/humanizer` (AI 티 제거)

### 자동 발행 시
- `Playwright Browser Automation skill` (웹 자동화)
- `wshuyi/x-article-publisher-skill` (SNS 발행 패턴)

### 숏폼 영상 시
- `remotion-dev/remotion skills` (공식 Remotion 스킬)
- `google-labs-code/stitch-skills/remotion` (워크플로 참고)

### 대시보드 구축 시
- `anthropics/skills - frontend-design` (UI 디자인)
- `vercel-labs/next-best-practices` (Next.js 패턴)
- `vercel-labs/react-best-practices` (React 패턴)

### 스킬 직접 만들 때
- `anthropics/skills - skill-creator` (스킬 생성 도우미)
- `anthropics/skills - mcp-builder` (MCP 서버 구축)

## 워크플로

새 기능 구현 시작 시:
1. 이 스킬의 추천 맵에서 관련 스킬 확인
2. 설치되지 않은 스킬이 있으면 설치
3. 설치된 스킬의 패턴과 best practice를 참고하여 구현
4. 커뮤니티에 없는 기능만 커스텀 스킬로 작성

## 스킬 설치 위치
- 프로젝트 스킬: `.claude/skills/` (이 프로젝트 전용)
- 글로벌 스킬: `~/.claude/skills/` (모든 프로젝트 공유)
