#!/usr/bin/env python3
"""
OCR slide images using Tesseract.
Extracts text from each slide image and prints it with slide markers.

Usage:
    python ocr_slides.py slide-01.jpg slide-02.jpg ... [--lang kor+eng]
    python ocr_slides.py /path/to/slide-*.jpg --lang eng
"""

import argparse
import sys
import re
from pathlib import Path

try:
    import pytesseract
    from PIL import Image
except ImportError:
    print("Error: Install dependencies first: pip install pytesseract pillow --break-system-packages", file=sys.stderr)
    sys.exit(1)


def natural_sort_key(path: Path):
    """Sort filenames naturally (slide-2 before slide-10)."""
    parts = re.split(r'(\d+)', path.stem)
    return [int(p) if p.isdigit() else p.lower() for p in parts]


def ocr_image(image_path: str, lang: str = "eng") -> str:
    """Run Tesseract OCR on a single image and return extracted text."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang)
        return text.strip()
    except Exception as e:
        return f"[OCR Error: {e}]"


def main():
    parser = argparse.ArgumentParser(description="OCR slide images")
    parser.add_argument("images", nargs="+", help="Slide image files (e.g., slide-01.jpg)")
    parser.add_argument("--lang", default="eng", help="Tesseract language(s), e.g., 'kor+eng' (default: eng)")
    args = parser.parse_args()

    # Sort images naturally
    image_paths = sorted([Path(p) for p in args.images], key=natural_sort_key)

    for i, img_path in enumerate(image_paths, 1):
        if not img_path.exists():
            print(f"--- Slide {i}: {img_path.name} ---", file=sys.stderr)
            print(f"[File not found: {img_path}]", file=sys.stderr)
            continue

        text = ocr_image(str(img_path), lang=args.lang)
        print(f"--- Slide {i}: {img_path.name} ---")
        if text:
            print(text)
        else:
            print("[No text detected]")
        print()


if __name__ == "__main__":
    main()
