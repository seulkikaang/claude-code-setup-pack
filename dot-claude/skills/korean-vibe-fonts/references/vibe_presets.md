---
name: Korean Vibe Font Presets
description: Ready-made Korean webfont pairings for common vibe-coding themes.
---

# Korean Vibe Font Presets

Use this file when the user gives only a loose mood such as "AI SaaS", "quiet editorial", or "cute community app" and you want a fast, opinionated starting point before fine-tuning.

For finer "when should I choose which font?" guidance, use `references/font_decision_guide.json`. It breaks recommendations down by concrete product situations and includes body, heading, code, avoid notes, and candidate font IDs.

## Quick presets

| Theme | Body | Heading | Code | Why |
| --- | --- | --- | --- | --- |
| AI SaaS landing | Wanted Sans Variable | SUITE Variable | NanumGothicCoding | 고민 없이 쓰기 좋은 제품형 조합. 현대적이고 화면 밀도가 좋다. |
| B2B dashboard | IBM Plex Sans KR | IBM Plex Sans KR | NanumGothicCoding | 구조적이고 기술 친화적이다. |
| Developer portfolio | Wanted Sans Variable | SUITE Variable | NanumGothicCoding | UI는 세련되게, 코드 블록은 선명하게 유지한다. |
| Dense SaaS UI | SUIT Variable | SUITE Variable | NanumGothicCoding | 폭이 단정해서 작은 화면에 정보를 깔끔하게 넣기 좋다. |
| Friendly fintech onboarding | LINE Seed Sans KR | LINE Seed Sans KR | - | 딱딱한 업종을 둥글고 부드럽게 보이게 한다. |
| Quiet editorial portfolio | MaruBuri | Hahmlet | - | 브랜드 스토리와 긴 글에 온기와 개성을 준다. |
| Premium journal | Noto Serif KR | Hahmlet | - | 공신력과 우아함을 같이 가져간다. |
| Cozy lifestyle brand | Gowun Dodum | Single Day | - | 부드러운 본문 위에 따뜻한 손글씨 포인트를 얹는다. |
| Youthful community app | NanumSquareRound | Jua | - | 접근성이 높고 활기차다. |
| Friendly food brand | Noto Sans KR | Yeon Sung | - | 본문은 읽기 쉽게 두고, 배민 손글씨 계열로 따뜻한 식감만 준다. |
| Baemin local food campaign | BM Hanna Air | BM Hanna 11yrs | - | 본문도 배민 계열로 맞추되 Air로 숨을 주고, 제목은 한나체로 바로 알아보이게 한다. |
| Retro alley poster | Wanted Sans Variable | BM Euljiro | - | 기본 설명은 읽기 쉽게 유지하고 을지로 간판 무드로 현장감을 만든다. |
| Bold campaign or event page | Pretendard Variable | Black Han Sans | - | 본문은 깔끔하게, 타이틀은 강하게 밀어준다. |
| Commerce sale banner | Noto Sans KR | Do Hyeon | - | 본문은 무난하게 유지하고 타이틀만 공격적으로 세운다. |

## Pairing rules

- Keep the page to at most 3 families: body, heading, code.
- Prefer a readable body font even when the vibe is playful. Use display or handwriting fonts for headings and accent lines, not paragraph text.
- Add `NanumGothicCoding` whenever the page contains code blocks, terminal UI, CLI examples, or a hacker/devtool vibe.
- For long-form reading, favor `MaruBuri`, `Hahmlet`, `Noto Serif KR`, or `Gowun Batang`.
- For product UIs, default to `Wanted Sans Variable`, `SUIT Variable`, `Pretendard Variable`, `IBM Plex Sans KR`, or `Noto Sans KR`.

## Escalation hints

- If the user asks for "retro", "street", "campaign", "local food", or "strong poster energy", favor `BM Euljiro`, `BM Euljiro 10 Years Later`, `Black Han Sans`, or `Do Hyeon` for headings.
- If the user asks for "cozy", "handmade", or "diary", keep body text readable with `Gowun Dodum` or `NanumSquareRound` and use `Single Day`, `NanumPen`, `Yeon Sung`, `Kirang Haerang`, or `Gaegu` only as accents.
- If the user asks for "luxury", "editorial", "literary", or "brand story", start from `MaruBuri`, `Hahmlet`, or `Noto Serif KR`.
