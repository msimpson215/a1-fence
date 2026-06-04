#!/usr/bin/env python3
"""Keep original A1 phone numbers for Joe mock-up (logo may show 888)."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

REPLACEMENTS = [
    ("tel:18882233797", "tel:13149495660"),
    ("sms:18882233797", "sms:13149495660"),
    ("18882233797", "13149495660"),
    ("(888) 223-3797", "(314) 949-5660"),
    ("Call (888) 223-3797", "Call (314) 949-5660"),
]

OFFICE_NEW = """      <div style="margin-bottom:14px;color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">Call</strong><br/><a href="tel:13149495660" style="color:#fff;text-decoration:none;">(314) 949-5660</a></div>
      <div style="color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">Web</strong><br/><a href="https://A1FencePro.com" style="color:var(--yellow);text-decoration:none;">A1FencePro.com</a></div>"""

OFFICE_ORIG = """      <div style="margin-bottom:14px;color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">IL.</strong> Lebanon, IL 62254<br/>(618) 929-3301</div>
      <div style="margin-bottom:14px;color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">MO.</strong> Maryland Heights, MO<br/>(314) 949-5660</div>
      <div style="color:#fff;font-size:0.85rem;line-height:1.6;"><strong style="color:#F5C518;font-size:0.72rem;text-transform:uppercase;">MO.</strong> St. Peters, MO<br/>(314) 356-1142</div>"""

INDEX_CONTACT = """      <div class="contact-info"><p><strong>Call:</strong> <a href="tel:13149495660">(314) 949-5660</a></p>
      <p><strong>Alt:</strong> <a href="tel:16189293301">(618) 929-3301</a></p></div>"""


def main() -> None:
    for path in PUBLIC.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        text = text.replace(OFFICE_NEW, OFFICE_ORIG)
        # Footer Local/Office rows that were both set to 888
        text = text.replace(
            '<strong style="color:#F5C518;min-width:80px;font-size:0.72rem;text-transform:uppercase;">Local</strong><span>(314) 949-5660</span>',
            '<strong style="color:#F5C518;min-width:80px;font-size:0.72rem;text-transform:uppercase;">Local</strong><span>(618) 929-3301</span>',
        )
        text = text.replace(
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Local</strong><span>(314) 949-5660</span>',
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Local</strong><span>(618) 929-3301</span>',
        )
        text = text.replace(
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Phone</strong><span><a href="tel:13149495660" style="color:#fff;text-decoration:none;">(314) 949-5660</a></span>',
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Local</strong><span>(618) 929-3301</span>',
        )
        text = text.replace(
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Web</strong><span><a href="https://A1FencePro.com" style="color:var(--yellow);text-decoration:none;">A1FencePro.com</a></span>',
            '<strong style="color:var(--yellow);min-width:80px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;">Office</strong><span>(314) 949-5660</span>',
        )
        if path.name == "index.html":
            text = re.sub(
                r'<div class="contact-info">.*?</div>',
                INDEX_CONTACT.strip(),
                text,
                count=1,
                flags=re.DOTALL,
            )
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
