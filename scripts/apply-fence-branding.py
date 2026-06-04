#!/usr/bin/env python3
"""Apply A1 Fence logo and domain. Phones stay on original lines for mock-up."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

REPLACEMENTS = [
    ("A1_fence_logo.svg", "A1_fence_logo.jpg"),
    ("a1fencepro.com", "A1FencePro.com"),
    ("https://a1fencepro.com", "https://A1FencePro.com"),
]


def main() -> None:
    targets = list(PUBLIC.glob("**/*")) + [ROOT / "README.md", ROOT / "scripts" / "sync-site-nav.py"]
    for path in targets:
        if not path.is_file() or path.suffix not in {".html", ".css", ".md", ".py", ".js"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
