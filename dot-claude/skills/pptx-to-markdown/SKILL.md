---
name: pptx-to-markdown
description: "Convert PowerPoint (.pptx) presentations to Markdown with full image OCR support. Use this skill whenever the user asks to convert a PPT/PPTX to Markdown, extract text from slides including images, diagrams, charts, or any visual content. Also triggers when the user says 'PPT를 마크다운으로', 'slides to markdown', 'extract all text from presentation', or wants a text-based summary of a slide deck that includes image contents. This skill goes beyond basic text extraction — it recognizes text inside images, charts, diagrams, and screenshots embedded in slides."
---

# PPTX to Markdown Converter (with Image OCR)

Converts a `.pptx` file into a single Markdown document. Unlike basic text extraction, this skill also converts each slide to an image and performs OCR + visual analysis on embedded images, diagrams, and charts so that **no information is lost**.

## Workflow

```
1. Extract text via markitdown          → base markdown
2. Convert slides to images             → slide-01.jpg, slide-02.jpg, ...
3. For each slide image, use Claude's   → image descriptions + OCR text
   vision to describe visual content
4. Merge text + visual descriptions     → final markdown output
```

## Step-by-Step Instructions

### 1. Setup & Dependencies

```bash
pip install "markitdown[pptx]" pytesseract pillow pdf2image --break-system-packages -q
# Install Korean + English tessdata if not present
apt-get update -qq && apt-get install -y -qq tesseract-ocr-kor 2>/dev/null || true
```

### 2. Extract Base Text

```bash
python -m markitdown /path/to/input.pptx > /home/claude/base_text.md
```

This gives you the raw text content from all slides. Review it — this is your starting skeleton.

### 3. Convert Slides to Images

```bash
python /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf /path/to/input.pptx
pdftoppm -jpeg -r 200 /home/claude/input.pdf /home/claude/slide
```

This produces `slide-01.jpg`, `slide-02.jpg`, etc.

### 4. OCR + Visual Analysis

For each slide image, do two things:

#### a) Tesseract OCR (catches text in images/diagrams)

Run the `scripts/ocr_slides.py` script:

```bash
python /path/to/skill/scripts/ocr_slides.py /home/claude/slide-*.jpg --lang kor+eng
```

This outputs OCR text per slide to stdout.

#### b) Claude Vision Analysis (catches meaning of charts, diagrams, layouts)

Use the `view` tool to look at each slide image. For each slide, describe:
- What visual elements are present (charts, diagrams, tables, screenshots, icons)
- Any text visible in images that markitdown may have missed
- The meaning/data conveyed by charts or diagrams
- Layout context (e.g., "left column shows X, right column shows Y")

### 5. Merge into Final Markdown

Combine all sources into a single `.md` file with this structure:

```markdown
# [Presentation Title]

---

## Slide 1: [Slide Title]

[Text content from markitdown]

### Visual Content
[Description of images, charts, diagrams from Claude vision analysis]
[Any additional OCR text not captured by markitdown]

---

## Slide 2: [Slide Title]
...
```

**Merging rules:**
- Use markitdown text as the primary content
- Add a `### Visual Content` subsection ONLY if the slide has images/charts/diagrams with meaningful content
- Do NOT duplicate text that markitdown already captured
- For charts/graphs: describe the data, trends, and key takeaways
- For diagrams/flowcharts: describe the structure and relationships
- For screenshots: transcribe visible text and describe the UI context
- For decorative images (stock photos, backgrounds): skip or mention briefly

### 6. Output

Save the final merged markdown to `/mnt/user-data/outputs/[presentation_name].md` and present it to the user.

## Tips

- If the presentation is in Korean, use `--lang kor+eng` for OCR
- If OCR quality is poor, rely more on Claude's vision analysis
- For very large presentations (30+ slides), process in batches of 10
- Always cross-reference OCR output with markitdown output to avoid duplication
