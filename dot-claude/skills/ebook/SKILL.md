---
name: ebook
description: Create Kindle-ready EPUB ebooks from source materials (Notion HTML exports, PPTX, PDF, Markdown). Handles content extraction, translation, image processing, chapter structuring, and iterative review cycles. Use when the user wants to create or update an ebook.
origin: custom
---

# Ebook Creation & Review Workflow

End-to-end pipeline for creating Kindle-ready EPUB ebooks from source materials.

## When to Activate

- Creating ebooks from Notion exports, PPTX, PDF, or Markdown sources
- Translating Korean course materials into English ebooks
- Reviewing and fixing existing EPUB content (images, text ordering, gaps)
- Rebuilding EPUB after corrections

## Directory Structure

```
output/kindle/{book-name}/
├── frontmatter.md          # Title, subtitle, author, about
├── ch01.md                 # Chapter 1
├── ch02.md                 # Chapter 2
├── ...
├── images/                 # All images referenced in chapters
│   ├── ch01_img001.png
│   ├── ch02_video_demo1.png  # Video frame grids
│   └── ...
└── ...

output/kindle/
├── kindle-style.css        # Shared Kindle CSS
└── {Book-Name}-v{N}.epub   # Versioned EPUB output
```

## Phase 1: Source Analysis

1. **Identify source files** in the source directory
   - HTML (Notion exports): Parse `<img>`, `<h1-6>`, `<p>`, `<code>` tags
   - PPTX: Use `markitdown` or `python-pptx` for extraction
   - PDF: Use Claude Vision for image-heavy pages

2. **Map source structure** to chapter outline
   - Each week/module = one chapter
   - Identify sections, subsections, images, videos, code blocks, prompts

3. **Identify content types**:
   - Text descriptions and explanations
   - Prompts (must go in ` ```text ``` ` code blocks)
   - Images (screenshots, diagrams, photos)
   - Videos (convert to frame grids)
   - Tables (model comparisons, feature lists)

## Phase 2: Content Extraction & Translation

### Text Content
- Extract all text from source, preserving structure
- Translate Korean → English naturally (not literal)
- Adapt Korean-specific examples to global equivalents
- Exclude specified sections (e.g., 우수과제/best assignments)
- **Prompts in code blocks**: Always preserve full prompt text inside ` ```text ``` ` blocks

### Image Processing

**Korean → English image translation** (via Gemini API):
```bash
# Script: /tmp/translate_image.py
# Uses gemini-3-pro-image-preview model
# Base64 encode source image → API call with translation prompt → decode response
GEMINI_API_KEY=<key>
GEMINI_MODEL=gemini-3-pro-image-preview
GEMINI_API_URL=https://generativelanguage.googleapis.com/v1beta/models
```

**Image categorization**:
- Read each image with the Read tool to visually inspect
- Korean text present → translate via Gemini API
- No Korean text → copy directly
- Content-filtered by API → keep original with note

**Video → Frame Grid conversion**:
```bash
# Extract 4 frames at calculated intervals
DURATION=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$VIDEO")
INTERVAL=$(echo "$DURATION / 5" | bc -l)

for i in 1 2 3 4; do
  TIMESTAMP=$(echo "$INTERVAL * $i" | bc -l)
  ffmpeg -ss "$TIMESTAMP" -i "$VIDEO" -frames:v 1 -q:v 2 "frame_${i}.png"
done

# Combine into 2x2 grid
magick montage frame_1.png frame_2.png frame_3.png frame_4.png \
  -tile 2x2 -geometry +4+4 -background white output.png
```

## Phase 3: Chapter Assembly

### Markdown Format
```markdown
## Chapter N: Title

### Day/Section 1: Subtitle

Text description before images.

![Alt text describing what the image shows](images/chNN_imgNNN.png)

#### Subsection

> **Tip:** Callout boxes for tips and warnings

` ` `text
Prompt content goes here in code blocks
` ` `

| Column 1 | Column 2 |
|----------|----------|
| Data     | Data     |
```

### Critical Rules
1. **Text BEFORE images** — Always provide context before showing screenshots
2. **Image alt text** — Describe what the image shows for accessibility
3. **Prompt preservation** — Never truncate or summarize prompts; include full text
4. **Image naming convention**: `ch{NN}_img{NNN}.png`, `ch{NN}_video_{name}.png`
5. **No orphaned images** — Every image must have surrounding context

## Phase 4: EPUB Build

```bash
BOOK="output/kindle/{book-name}"
STYLE="output/kindle/kindle-style.css"
OUT="output/kindle/{Book-Name}-v{N}.epub"

pandoc \
  "$BOOK/frontmatter.md" \
  "$BOOK/ch01.md" \
  "$BOOK/ch02.md" \
  "$BOOK/ch03.md" \
  "$BOOK/ch04.md" \
  -o "$OUT" \
  --css="$STYLE" \
  --toc \
  --toc-depth=3 \
  --resource-path="$BOOK" \
  --split-level=2 \
  --metadata title="Title" \
  --metadata author="Author" \
  --metadata lang=en
```

After building:
```bash
open "$OUT"          # Open in ebook reader
open -R "$OUT"       # Reveal in Finder
```

## Phase 5: Review & Iteration

### Gap Analysis (parallel agents)
Launch parallel agents comparing source HTML against each chapter:
- **Source agent**: Read source HTML, extract all sections/images/text
- **Ebook agent**: Read chapter markdown, list all content
- **Diff agent**: Identify missing text, wrong images, ordering issues

### Common Issues Checklist
| Issue | Detection | Fix |
|-------|-----------|-----|
| Wrong image placement | Read image with Read tool, verify content matches context | Move/remove image reference |
| Korean text in image | Visually inspect with Read tool | Re-translate via Gemini or remove |
| Missing text description | Compare source sections vs ebook | Add translated text before images |
| Text-image ordering | Text appears after images | Move text block before image references |
| Misplaced images from other sections | Image content doesn't match section topic | Remove from wrong section, add to correct one |
| Missing prompts | Source has prompt text, ebook has none | Add full prompt in code block |
| Wrong video frame grid | Frame content doesn't match section | Re-extract from correct video file |

### Review Workflow
1. User reviews EPUB, provides page-by-page feedback
2. Map EPUB page numbers → markdown line numbers
3. Visually inspect flagged images with Read tool
4. Make targeted edits (never rewrite entire chapters)
5. Rebuild EPUB with incremented version number
6. Repeat until user approves

### Sections to Delete
When user requests section deletion:
- Remove ALL lines from section header to next section header
- Remove associated image files if no longer referenced
- Verify no dangling references remain

## Frontmatter Template

```yaml
---
title: "Book Title"
subtitle: "Subtitle"
author: "Author Name"
lang: en
---

# Book Title

### Subtitle
### Tagline

**By Author Name**

---

## About This Book

Description paragraph.

## What You Will Learn

- Bullet points of learning outcomes

---
```

## Kindle CSS (kindle-style.css)

Key styles for Kindle rendering:
- Body: `font-family: Georgia, serif; line-height: 1.6`
- Code blocks: `background: #f4f4f4; font-size: 0.85em; overflow-wrap: break-word`
- Images: `max-width: 100%; height: auto`
- Tables: `border-collapse: collapse; width: 100%`
- Blockquotes: `border-left: 3px solid #ccc; padding-left: 1em`

## Error Handling

| Error | Solution |
|-------|----------|
| Gemini content filtering | Keep original image, add note |
| ImageMagick font warning | Cosmetic only, ignore |
| macOS grep -P not supported | Use `grep -o` instead |
| Pandoc --epub-chapter-level deprecated | Use `--split-level` |
| Large EPUB (>100MB) | Compress images with `magick convert -quality 80` |
| Subshell variable loss | Re-declare variables in each Bash call |
