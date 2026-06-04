#!/usr/bin/env python3
"""Apply A1 Fence logo, phone, and domain from official branding."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

REPLACEMENTS = [
    ("A1_fence_logo.svg", "A1_fence_logo.jpg"),
    ("tel:13149495660", "tel:18882233797"),
    ("sms:13149495660", "sms:18882233797"),
    ("(314) 949-5660", "(888) 223-3797"),
    ("13149495660", "18882233797"),
    ("tel:16189293301", "tel:18882233797"),
    ("(618) 929-3301", "(888) 223-3797"),
    ("16189293301", "18882233797"),
    ("(314) 356-1142", "(888) 223-3797"),
    ("a1fencepro.com", "A1FencePro.com"),
    ("https://a1fencepro.com", "https://A1FencePro.com"),
]

# Office footer blocks: simplify to single toll-free where duplicated
OFFICE_SNIPPET_OLD = """      <div style="margin-bottom:14px;color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">IL.</strong> Lebanon, IL 62254<br/>(888) 223-3797</div>
      <div style="margin-bottom:14px;color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">MO.</strong> Maryland Heights, MO<br/>(888) 223-3797</div>
      <div style="color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">MO.</strong> St. Peters, MO<br/>(888) 223-3797</div>"""

OFFICE_SNIPPET_NEW = """      <div style="margin-bottom:14px;color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">Call</strong><br/><a href="tel:18882233797" style="color:#fff;text-decoration:none;">(888) 223-3797</a></div>
      <div style="color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">Web</strong><br/><a href="https://A1FencePro.com" style="color:var(--yellow);text-decoration:none;">A1FencePro.com</a></div>"""


def main() -> None:
    targets = list(PUBLIC.glob("**/*")) + [ROOT / "README.md", ROOT / "scripts" / "sync-site-nav.py"]
    for path in targets:
        if not path.is_file() or path.suffix not in {".html", ".css", ".md", ".py", ".js"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if OFFICE_SNIPPET_OLD in text:
            text = text.replace(OFFICE_SNIPPET_OLD, OFFICE_SNIPPET_NEW)
        # index footer contact rows
        text = text.replace(
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Local</strong><span>(888) 223-3797</span>',
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Phone</strong><span><a href="tel:18882233797" style="color:#fff;text-decoration:none;">(888) 223-3797</a></span>',
        )
        text = text.replace(
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Office</strong><span>(888) 223-3797</span>',
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Web</strong><span><a href="https://A1FencePro.com" style="color:var(--yellow);text-decoration:none;">A1FencePro.com</a></span>',
        )
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
