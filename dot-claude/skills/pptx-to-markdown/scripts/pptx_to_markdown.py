#!/usr/bin/env python3
"""
pptx_to_markdown.py — Full pipeline: PPTX → Text + Slide Images + OCR → Merged Markdown

Usage:
    python pptx_to_markdown.py input.pptx -o output.md [--lang kor+eng]

Steps:
    1. markitdown: extract base text
    2. soffice + pdftoppm: convert slides to images
    3. tesseract: OCR each slide image
    4. Output: base text + OCR results + image paths for Claude vision

The final merge with Claude vision analysis should be done by the calling agent.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd, **kwargs):
    """Run a shell command and return stdout."""
    result = subprocess.run(cmd, capture_output=True, text=True, **kwargs)
    if result.returncode != 0:
        print(f"[WARN] Command failed: {' '.join(cmd)}", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
    return result.stdout.strip()


def extract_text(pptx_path: str) -> str:
    """Extract text using markitdown."""
    return run([sys.executable, "-m", "markitdown", pptx_path])


def convert_to_images(pptx_path: str, output_dir: str, dpi: int = 200) -> list:
    """Convert PPTX to slide images via PDF intermediate."""
    pptx_name = Path(pptx_path).stem

    # Convert to PDF using soffice helper
    soffice_script = "/mnt/skills/public/pptx/scripts/office/soffice.py"
    if Path(soffice_script).exists():
        run([sys.executable, soffice_script, "--headless", "--convert-to", "pdf",
             "--outdir", output_dir, pptx_path])
    else:
        run(["libreoffice", "--headless", "--convert-to", "pdf",
             "--outdir", output_dir, pptx_path])

    pdf_path = os.path.join(output_dir, f"{pptx_name}.pdf")
    if not os.path.exists(pdf_path):
        print(f"[ERROR] PDF not created at {pdf_path}", file=sys.stderr)
        return []

    # Convert PDF to images
    slide_prefix = os.path.join(output_dir, "slide")
    run(["pdftoppm", "-jpeg", "-r", str(dpi), pdf_path, slide_prefix])

    # Collect slide images
    images = sorted(Path(output_dir).glob("slide-*.jpg"),
                    key=lambda p: int(re.search(r'(\d+)', p.stem).group()))
    return [str(img) for img in images]


def ocr_images(image_paths: list, lang: str = "eng") -> dict:
    """Run OCR on each slide image."""
    try:
        import pytesseract
        from PIL import Image
    except ImportError:
        return {p: "[pytesseract not installed]" for p in image_paths}

    results = {}
    for img_path in image_paths:
        try:
            img = Image.open(img_path)
            text = pytesseract.image_to_string(img, lang=lang).strip()
            results[img_path] = text if text else "[No text detected]"
        except Exception as e:
            results[img_path] = f"[OCR Error: {e}]"
    return results


def main():
    parser = argparse.ArgumentParser(description="PPTX to Markdown pipeline")
    parser.add_argument("input", help="Input .pptx file")
    parser.add_argument("-o", "--output", help="Output directory for intermediate files",
                        default="/home/claude/pptx_convert")
    parser.add_argument("--lang", default="eng", help="OCR language (e.g., kor+eng)")
    parser.add_argument("--dpi", type=int, default=200, help="Slide image DPI")
    args = parser.parse_args()

    pptx_path = os.path.abspath(args.input)
    output_dir = os.path.abspath(args.output)
    os.makedirs(output_dir, exist_ok=True)

    print(f"=== PPTX to Markdown Pipeline ===", file=sys.stderr)
    print(f"Input:  {pptx_path}", file=sys.stderr)
    print(f"Output: {output_dir}", file=sys.stderr)

    # Step 1: Extract text
    print("\n[1/3] Extracting text with markitdown...", file=sys.stderr)
    base_text = extract_text(pptx_path)
    text_path = os.path.join(output_dir, "base_text.md")
    with open(text_path, "w") as f:
        f.write(base_text)
    print(f"  → Saved to {text_path}", file=sys.stderr)

    # Step 2: Convert to images
    print("\n[2/3] Converting slides to images...", file=sys.stderr)
    images = convert_to_images(pptx_path, output_dir, dpi=args.dpi)
    print(f"  → {len(images)} slide images created", file=sys.stderr)

    # Step 3: OCR
    print("\n[3/3] Running OCR on slide images...", file=sys.stderr)
    ocr_results = ocr_images(images, lang=args.lang)
    ocr_path = os.path.join(output_dir, "ocr_results.json")
    with open(ocr_path, "w") as f:
        json.dump(ocr_results, f, ensure_ascii=False, indent=2)
    print(f"  → Saved to {ocr_path}", file=sys.stderr)

    # Summary output
    summary = {
        "base_text_path": text_path,
        "slide_images": images,
        "ocr_results_path": ocr_path,
        "slide_count": len(images),
    }
    summary_path = os.path.join(output_dir, "pipeline_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n=== Done! ===", file=sys.stderr)
    print(f"Summary: {summary_path}", file=sys.stderr)
    print(f"\nNext steps:", file=sys.stderr)
    print(f"  1. View slide images with Claude vision for chart/diagram analysis", file=sys.stderr)
    print(f"  2. Merge base_text.md + OCR + vision analysis into final markdown", file=sys.stderr)

    # Print summary to stdout for the calling agent
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
