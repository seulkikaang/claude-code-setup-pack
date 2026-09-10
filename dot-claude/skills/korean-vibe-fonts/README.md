# Korean Vibe Fonts ✨

Pick Korean webfonts by mood, not by guesswork.

This package helps an AI coding assistant choose Korean fonts that:

- feel right for the vibe you want
- are safe to use commercially
- come with paste-ready code you can use right away

It is especially useful for:

- landing pages
- portfolios
- dashboards
- editorial pages
- campaign pages
- developer tools

## 🌐 Live showcase

Browse the visual font showcase here:

- [https://seulkikaang.github.io/korean-vibe-fonts/](https://seulkikaang.github.io/korean-vibe-fonts/)

The page shows 464 commercially oriented Korean webfont entries, grouped by situation and vibe. It includes 17 situation presets such as dense dashboards, soft fintech onboarding, Baemin local campaigns, retro posters, editorial stories, kids education, and public notices.

## 🆕 Latest update

- Added a 35-font curated catalog covering practical UI sans, editorial serifs, Baemin-style display fonts, handwriting accents, and code typography.
- Added a broad [fonts-archive](https://github.com/fonts-archive) sweep: 564 repositories scanned, 429 included with webfont CSS and commercial-use/open-license signals, 135 excluded for unclear, conditional, personal-only, noncommercial, or purchase-only signals.
- Added [references/font_decision_guide.json](./references/font_decision_guide.json) with 17 situation-first presets for choosing body, heading, and code fonts.
- Published the static showcase through GitHub Pages and added `index.html` so the repository root opens the showcase directly.

## 💡 What it does

Instead of asking:

> "Which Korean font should I use?"

you can ask for something like:

> "Make this feel like an AI SaaS landing page"
> "I want a warm editorial mood"
> "Make it cute and playful"

The assistant will recommend:

- a body font
- a heading font
- a code font if needed
- ready-to-paste stylesheet tags
- ready-to-paste CSS

There is also one important consistency rule:

- even when screens or slides change, the same text role should keep the same font family

For example:

- titles keep the heading font
- paragraphs, captions, labels, and table text keep the body font
- code and terminal snippets keep the code font

## 🧑‍💻 Do I need to be a developer?

Not really.

If you already use tools like Codex or Claude Code, this package gives those tools better Korean font taste and safer defaults.

Even if you do not want to edit code deeply, you can still use it by copying the suggested font tags and CSS into your project or handing the package to someone on your team.

## 📦 What is inside

- [SKILL.md](./SKILL.md): the main Codex skill
- [README.ko.md](./README.ko.md): Korean guide
- [references/font_catalog.json](./references/font_catalog.json): verified font list
- [references/font_decision_guide.json](./references/font_decision_guide.json): situation-based guide for when to choose which font
- [references/fonts_archive_commercial.json](./references/fonts_archive_commercial.json): broad fonts-archive index filtered for webfont CSS and commercial-use/open-license signals
- [references/vibe_presets.md](./references/vibe_presets.md): quick mood presets
- [scripts/recommend_font.py](./scripts/recommend_font.py): font recommender
- [scripts/build_showcase.py](./scripts/build_showcase.py): showcase and GitHub Pages index HTML builder
- [scripts/render_claude_agent.py](./scripts/render_claude_agent.py): Claude Code adapter generator
- [adapters/claude-code-agent.template.md](./adapters/claude-code-agent.template.md): Claude Code template
- [adapters/generic-system-prompt.md](./adapters/generic-system-prompt.md): adapter for other agent tools

## 🚀 The easiest install flow

The simplest way to think about installation is:

1. put this package somewhere on your computer
2. connect it to the AI tool you use

### Step 1. Get the package onto your machine

If this lives in a GitHub repo, that usually means:

```bash
git clone <repo-url>
cd korean-vibe-fonts
```

If you already have the folder, you can skip this step.

### Step 2. Connect it to your AI tool

### If you use Codex

Codex follows the usual skill-folder pattern: the folder should live under `~/.codex/skills/`.

You can either copy the folder there or keep it where it is and create a symlink.

Example:

```bash
ln -s /path/to/korean-vibe-fonts ~/.codex/skills/korean-vibe-fonts
```

Or copy it directly:

```bash
cp -R /path/to/korean-vibe-fonts ~/.codex/skills/korean-vibe-fonts
```

Codex will then discover it automatically.

### If you use Claude Code

This part looks different because Claude Code uses a different normal pattern.

Instead of installing a Codex-style skill folder directly, Claude Code typically uses Markdown subagent files inside `~/.claude/agents/` or `.claude/agents/`.

So this package includes a helper script that generates the Claude-compatible file for you.

For a user-wide install:

```bash
python3 /path/to/korean-vibe-fonts/scripts/render_claude_agent.py \
  --output ~/.claude/agents/korean-vibe-fonts.md
```

For a project-local install:

```bash
mkdir -p .claude/agents
python3 /path/to/korean-vibe-fonts/scripts/render_claude_agent.py \
  --output .claude/agents/korean-vibe-fonts.md
```

So the difference is intentional:

- Codex normal pattern: place a folder in `~/.codex/skills/`
- Claude Code normal pattern: create a Markdown subagent in `.claude/agents/`

Claude Code docs:

- [Claude Code subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

### If you use another AI tool

Use [adapters/generic-system-prompt.md](./adapters/generic-system-prompt.md) as your starting prompt.

If that tool can also read files, give it access to:

- `references/font_catalog.json`
- `references/font_decision_guide.json`
- `references/fonts_archive_commercial.json`
- `references/vibe_presets.md`
- `scripts/recommend_font.py`

## 🎯 What you can ask for

Examples:

- "Make this feel like an AI startup"
- "Which font should I use for a dense Korean dashboard?"
- "Give me a font set for a soft fintech onboarding flow"
- "Recommend a font for a Korean editorial portfolio"
- "I want a premium brand story vibe"
- "Make the page feel playful and friendly"
- "Pick a Korean font set for a developer portfolio"

## ⚡ Quick test

You can run the recommender directly:

```bash
python3 scripts/recommend_font.py --theme "AI SaaS landing page"
python3 scripts/recommend_font.py --theme "warm editorial portfolio"
python3 scripts/recommend_font.py --theme "cute community app"
```

It will return:

- a recommended font set
- a short explanation
- stylesheet tags
- CSS variables
- a few alternatives

## 🔤 Full font list

These are the fonts currently included in the package.

The live page combines:

- 35 curated fonts in [references/font_catalog.json](./references/font_catalog.json)
- 429 fonts-archive entries in [references/fonts_archive_commercial.json](./references/fonts_archive_commercial.json)

### Great for body text and headings

- `Pretendard Variable`: the safest modern default for product UI, landing pages, and portfolios.
- `Wanted Sans Variable`: no-brainer modern UI sans. If you install it without overthinking, the page usually lands at least in the middle.
- `SUIT Variable`: narrow, tidy, and made for UI body text. Great when the screen needs to hold a lot without feeling messy.
- `NanumSquare Neo`: bold, straight, and brand-forward. Strong for hero headlines and cards.
- `NanumSquare`: clean and friendly. Good for startup, community, and mobile-first UI.
- `NanumGothic`: familiar and stable for body copy, support pages, and documentation-style layouts.
- `Gmarket Sans`: stylish and tidy with strong brand energy. Great for commerce, startup landing pages, and mobile promos.
- `Spoqa Han Sans Neo`: especially strong for UI/UX and numeric readability. Great for product surfaces and dashboards.
- `Goorm Sans`: balanced Korean and Latin rhythm. A nice fit for developer products, tech landing pages, and clean service UI.
- `IBM Plex Sans KR`: technical and calm. Great for B2B, developer tools, and data products.
- `LINE Seed Sans KR`: rounded and friendly. Useful when a stiff business category needs to feel softer.
- `Noto Sans KR`: a neutral multilingual default that works well in global products.
- `MaruBuri`: warm serif energy for brand stories and longer reading.
- `Hahmlet`: literary and elegant. Great for premium editorial direction.
- `Noto Serif KR`: tidy and trustworthy. Strong for institutional or credibility-focused pages.
- `Gowun Dodum`: soft and gentle. Nice for wellness, lifestyle, and cozy community products.
- `Gowun Batang`: poetic and spacious. Good for essays, journals, and calm portfolios.
- `NanumSquareRound`: rounded and cheerful. Good for education, family-friendly, and casual community products.

### Especially strong for headings

- `Black Han Sans`: high-impact display font for posters, events, and campaign heroes.
- `Do Hyeon`: compact Baemin headline energy. Strong for banners, gaming, and commerce promotion.
- `Yeon Sung`: warm Baemin handwriting mood. Good for food brands, local shops, and friendly review moments.
- `Kirang Haerang`: playful Baemin handwriting. Good for casual food events and bright campaign accents.
- `BM Kkubulim`: wavy, freeform Baemin display face. Good for playful food events and oddball one-line accents.
- `BM Hanna 11yrs`: classic bold Baemin title energy. Good for food campaigns, local shop posters, and lifestyle brand headlines.
- `BM Hanna Air`: lighter Baemin companion face. Useful when you want friendly copy without making every line shout.
- `BM Hanna Pro`: clean, punchy Baemin headline style for short brand, menu, and offer copy.
- `BM Euljiro`: retro signboard energy from old Euljiro shop lettering. Strong for local food and culture campaigns.
- `BM Euljiro 10 Years Later`: rougher, weathered Baemin display tone for one-line retro titles and posters.
- `여기어때 잘난체 (yg-jalnan)`: a high-attention headline font that works well for travel, hospitality, and lifestyle promos.
- `Jua`: cheerful Baemin headline style. Works well for food, family, and bright casual products.
- `SUITE Variable`: narrow, geometric, and tidy for UI headlines. Pairs naturally with `SUIT Variable`.

### For code and terminal UI

- `NanumGothicCoding (D2Coding)`: the most stable option for code blocks and terminal-style UI.

### Accent and handwriting options

- `NanumPen`: good for short notes, testimonials, and single-line emphasis.
- `Gaegu`: doodle-like and playful. Good for experimental accents.
- `Single Day`: tidy handwritten tone for diary-like notes and warm brand moments.

For curated metadata, official source links, and stylesheet URLs, see [references/font_catalog.json](./references/font_catalog.json).

For the broader fonts-archive sweep, see [references/fonts_archive_commercial.json](./references/fonts_archive_commercial.json). It currently includes 429 repositories with webfont CSS and explicit commercial-use/open-license signals, and excludes 135 repositories with unclear, conditional, personal-only, noncommercial, or purchase-only signals.

## 🔎 Font sources

The catalog points back to the source page and license page for each curated font. Main sources used in this update:

| Source | Fonts / scope | Links |
| --- | --- | --- |
| Pretendard | `Pretendard Variable` | [source](https://github.com/orioncactus/pretendard), [license](https://github.com/orioncactus/pretendard/blob/main/LICENSE) |
| Wanted Lab | `Wanted Sans Variable` | [source](https://github.com/wanteddev/wanted-sans), [license](https://github.com/wanteddev/wanted-sans/blob/main/OFL.txt) |
| SUNN | `SUIT Variable`, `SUITE Variable` | [SUIT](https://github.com/sun-typeface/SUIT), [SUITE](https://github.com/sun-typeface/SUITE) |
| NAVER Hangul | `NanumSquare Neo`, `NanumSquare`, `NanumGothic`, `NanumSquareRound`, `NanumGothicCoding`, `NanumPen`, `MaruBuri` | [source and license](https://hangeul.naver.com/font) |
| Google Fonts | `IBM Plex Sans KR`, `Noto Sans KR`, `Noto Serif KR`, `Hahmlet`, `Gowun Dodum`, `Gowun Batang`, `Black Han Sans`, `Gaegu`, `Single Day`, plus selected Baemin fonts hosted on Google Fonts | [Google Fonts](https://fonts.google.com/), [FAQ / license guidance](https://developers.google.com/fonts/faq) |
| Woowa Brothers Baemin fonts | `BM Kkubulim`, `BM Hanna 11yrs`, `BM Hanna Air`, `BM Hanna Pro`, `BM Euljiro`, `BM Euljiro 10 Years Later`, `Do Hyeon`, `Yeon Sung`, `Kirang Haerang`, `Jua` | [source](https://www.woowahan.com/fonts), [license](https://www.woowahan.com/fonts/license) |
| fonts-archive | 429 additional repositories with webfont CSS and commercial-use/open-license signals, including broader Baemin and public/institutional font archives | [organization](https://github.com/fonts-archive), [filtered catalog](./references/fonts_archive_commercial.json) |
| Spoqa | `Spoqa Han Sans Neo` | [source and license](https://spoqa.github.io/spoqa-han-sans/) |
| goorm | `Goorm Sans` | [source and license](https://goorm-sans.goorm.io/) |
| LINE | `LINE Seed Sans KR` | [source](https://seed.line.me/), [license](https://github.com/line/seed/blob/main/OFL.txt) |
| Gmarket | `Gmarket Sans` | [source and license](https://corp.gmarket.com/fonts/) |
| 여기어때 | `여기어때 잘난체` | [source](https://www.goodchoice.kr/font/mobile), [license PDF](https://image.goodchoice.kr/images/jalnan_font/jalnan-font-190124ver.pdf) |

License note: this package records commercial-use/open-license signals for recommendation purposes. Before redistributing font files or shipping a high-stakes production brand system, re-check the upstream license page linked in the catalog.

## ❤️ Why this is different

Many design skills say things like:

- "pick a beautiful font"
- "avoid generic typography"

This package goes further:

- it focuses on Korean webfonts
- it checks commercial-use safety
- it connects mood to font choice
- it gives you code you can paste immediately

## 🔒 Font safety

The bundled curated catalog only includes fonts checked from official source and license pages. The fonts-archive extension is broader: it includes repositories only when the README or license text has a clear commercial-use/open-license signal and a usable webfont CSS path.

If you add new fonts later, check the official license and the official stylesheet, CDN source, or self-hosting guidance first.

## 🌿 Good first workflow

If you want the simplest setup:

1. Install the folder in Codex or generate the Claude Code agent file.
2. Ask for the mood you want.
3. Copy the suggested tags and CSS into your project.

That is the whole flow.

## 📚 More help

If you are more comfortable in Korean, read:

- [README.ko.md](./README.ko.md)
