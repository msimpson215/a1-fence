#!/usr/bin/env python3
"""Fix collateral damage from sealcoat -> fence install global replace."""

from pathlib import Path
import re

PUBLIC = Path(__file__).resolve().parents[1] / "public"

FOOTER_SERVICES = """<li style="margin-bottom:10px;"><a href="sealcoating.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Wood Fencing</a></li><li style="margin-bottom:10px;"><a href="crack-filling.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Vinyl Fencing</a></li><li style="margin-bottom:10px;"><a href="parking-lot-striping.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Picket Fencing</a></li><li style="margin-bottom:10px;"><a href="asphalt-patching.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Wrought Iron</a></li><li style="margin-bottom:10px;"><a href="concrete-work.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Commercial Fencing</a></li><li style="margin-bottom:10px;"><a href="bollard-installation.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Chain Link</a></li>"""

MOBILE_BLOCK = """  <a href="#services">Services</a>
  <a href="sealcoating.html">Wood Fencing</a>
  <a href="crack-filling.html">Vinyl Fencing</a>
  <a href="parking-lot-striping.html">Picket Fencing</a>
  <a href="asphalt-patching.html">Wrought Iron</a>
  <a href="concrete-work.html">Commercial Fencing</a>
  <a href="bollard-installation.html">Chain Link</a>"""

EXPECT_BOX = """        <p>We start with a site walk — property lines, utilities, slopes, and gate locations. Permits and HOA approvals are flagged up front.</p>
        <p>Posts are set to depth, rails leveled, and fabric or boards hung to spec. We protect landscaping and clean up daily.</p>
        <p>When we are done, you get a straight, secure fence line — that is the A1 standard.</p>"""

INDEX_CARDS = [
    ("<h3>Commercial Properties</h3><p>Retail centers, office parks, and commercial facilities with full design, install, and maintain fences programs.</p>",
     "<h3>Wood Fencing</h3><p>Privacy and perimeter wood fences for homes, HOAs, churches, and light commercial sites.</p>"),
    ("<h3>Retail &amp; Strip Malls</h3><p>National retailers, shopping centers, and multi-tenant properties — fence installing, striping, ADA compliance, and fire lanes.</p>",
     "<h3>Picket Fencing</h3><p>Classic front-yard picket and garden borders — wood or vinyl, HOA-friendly heights.</p>"),
    ("<h3>Apartments &amp; Municipalities</h3><p>Apartment complexes, condominiums, HOA communities, and municipal properties — full fence installation and maintenance programs.</p>",
     "<h3>Wrought Iron</h3><p>Ornamental iron entries, monuments, churches, and upscale commercial driveways.</p>"),
    ("<h3>Industrial &amp; Warehouse</h3><p>Heavy-duty fence installation and repair for distribution centers, warehouses, and industrial facilities.</p>",
     "<h3>Chain Link</h3><p>Galvanized and vinyl-coated cyclone fencing for warehouses, utilities, and construction sites.</p>"),
]

OUR_WORK_GALLERY = """    <div class="service-grid">
      <a href="gallery-sealcoating.html" class="service-card">
        <img src="images/fences/wood-fence.jpg" alt="Wood fencing"/>
        <div class="service-card-label">
          <h3 style="color:#F5C518;">Wood Fencing</h3>
          <p>Cedar, pine, and pressure-treated privacy fences for residential and commercial properties.</p>
          <span class="view-btn">View Gallery &#8594;</span>
        </div>
      </a>
      <a href="gallery-crackfill.html" class="service-card">
        <img src="images/fences/vinyl-fence.jpg" alt="Vinyl fencing"/>
        <div class="service-card-label">
          <h3 style="color:#F5C518;">Vinyl Fencing</h3>
          <p>Low-maintenance vinyl panels — clean lines, no painting, built for Midwest weather.</p>
          <span class="view-btn">View Gallery &#8594;</span>
        </div>
      </a>
      <a href="gallery-striping.html" class="service-card">
        <img src="images/fences/picket-fence.jpg" alt="Picket fencing"/>
        <div class="service-card-label">
          <h3 style="color:#F5C518;">Picket Fencing</h3>
          <p>Decorative front-yard and garden picket fences in wood or vinyl.</p>
          <span class="view-btn">View Gallery &#8594;</span>
        </div>
      </a>
      <a href="gallery-paving.html" class="service-card">
        <img src="images/fences/wrought-iron-fence.jpg" alt="Wrought iron fencing"/>
        <div class="service-card-label">
          <h3 style="color:#F5C518;">Wrought Iron</h3>
          <p>Ornamental iron and steel entries, gates, and architectural perimeters.</p>
          <span class="view-btn">View Gallery &#8594;</span>
        </div>
      </a>
      <a href="gallery-concrete.html" class="service-card">
        <img src="images/fences/commercial-fence.jpg" alt="Commercial fencing"/>
        <div class="service-card-label">
          <h3 style="color:#F5C518;">Commercial Fencing</h3>
          <p>Retail, industrial, and municipal perimeter programs — multi-site capable.</p>
          <span class="view-btn">View Gallery &#8594;</span>
        </div>
      </a>
      <a href="gallery-patching.html" class="service-card">
        <img src="images/fences/chain-link-fence.jpg" alt="Chain link fencing"/>
        <div class="service-card-label">
          <h3 style="color:#F5C518;">Chain Link</h3>
          <p>Galvanized and vinyl-coated cyclone fence for security and equipment yards.</p>
          <span class="view-btn">View Gallery &#8594;</span>
        </div>
      </a>
    </div>"""


def fix_text(text: str) -> str:
    text = text.replace("fence installing.html", "sealcoating.html")
    text = text.replace("Fence installing", "Fence installation")
    text = text.replace("fence installing", "fence installation")
    text = re.sub(r"(Wood|Vinyl|Picket|Wrought Iron|Commercial Fencing|Chain Link) \1 / Sealing", r"\1", text)
    text = re.sub(r"Lot (Wood Fencing|Vinyl Fencing|Picket Fencing|Wrought Iron|Commercial Fencing|Chain Link)", r"\1", text)
    text = re.sub(r"(Wood Fencing|Vinyl Fencing|Picket Fencing|Wrought Iron|Commercial Fencing|Chain Link) Finishing", r"\1", text)
    text = text.replace("maintain fences programs", "fence programs")
    text = text.replace(
        "Commercial fence installing, striping, paving, and concrete services across St. Louis and the Midwest.",
        "Wood, vinyl, picket, wrought iron, chain link, and commercial perimeter fencing across St. Louis and the Midwest.",
    )
    text = text.replace('<div class="body-text"><div class="body-text">', '<div class="body-text">')
    # Expect box on service pages
    text = re.sub(
        r"<p>We start with a full lot assessment.*?</p>\s*<p>When we're done, your lot looks like day one\. That's the A1 standard\.</p>",
        EXPECT_BOX,
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<p>We start with a full lot assessment.*?</p>\s*<p>When we&#8217;re done, your lot looks like day one\. That&#8217;s the A1 standard\.</p>",
        EXPECT_BOX,
        text,
        flags=re.DOTALL,
    )
    # Footer service lists (broken)
    text = re.sub(
        r"<ul style=\"list-style:none;\">.*?</ul>\s*</div>\s*<div>\s*<div style=\"font-size:0\.72rem;font-weight:800;letter-spacing:0\.14em;text-transform:uppercase;color:#F5C518;margin-bottom:20px;\">Markets</div>",
        f"<ul style=\"list-style:none;\">{FOOTER_SERVICES}</ul>\n    </div>\n    <div>\n      <div style=\"font-size:0.72rem;font-weight:800;letter-spacing:0.14em;text-transform:uppercase;color:#F5C518;margin-bottom:20px;\">Markets</div>",
        text,
        count=1,
        flags=re.DOTALL,
    )
    return text


def main():
    for path in PUBLIC.glob("*.html"):
        text = fix_text(path.read_text(encoding="utf-8"))
        path.write_text(text, encoding="utf-8")

    index = PUBLIC / "index.html"
    t = index.read_text(encoding="utf-8")
    t = re.sub(
        r'<div class="mobile-menu" id="mobileMenu">.*?</div>\s*<section class="hero">',
        f'<div class="mobile-menu" id="mobileMenu">\n{MOBILE_BLOCK}\n  <a href="our-work.html">Our Work</a>\n  <a href="about.html">About</a>\n  <a href="javascript:void(0)" onclick="openVox()">Artificial Intelligence Team Member</a>\n  <a href="tel:13149495660">(314) 949-5660</a>\n  <a href="sms:13149495660" title="Text a real person — not a chatbot">Text Us</a>\n</div>\n\n<section class="hero">',
        t,
        count=1,
        flags=re.DOTALL,
    )
    for old, new in INDEX_CARDS:
        t = t.replace(old, new)
    index.write_text(t, encoding="utf-8")

    our = PUBLIC / "our-work.html"
    ot = our.read_text(encoding="utf-8")
    ot = fix_text(ot)
    ot = ot.replace("A1 Professional Fence &amp; Sealing", "A1 Professional Fence")
    ot = re.sub(
        r'<p class="hero-sub">[^<]*</p>',
        '<p class="hero-sub">10,000+ fence projects across 17 states.</p>',
        ot,
        count=1,
    )
    ot = re.sub(
        r"background:url\('images/St\. Louis skyline[^']+'\)",
        "background:url('images/fences/fence-hero.jpg')",
        ot,
        count=1,
    )
    ot = re.sub(
        r'<div class="service-grid">.*?</div>\s*</div>\s*</section>\s*<!-- INTRO',
        OUR_WORK_GALLERY + "\n  </div>\n</section>\n\n<!-- INTRO",
        ot,
        count=1,
        flags=re.DOTALL,
    )
    our.write_text(ot, encoding="utf-8")

    # Gallery images on service pages
    for name in ["sealcoating.html", "crack-filling.html", "parking-lot-striping.html",
                 "asphalt-patching.html", "concrete-work.html", "bollard-installation.html"]:
        p = PUBLIC / name
        t = p.read_text(encoding="utf-8")
        t = re.sub(r'src="images/(?:Sealing|sealing|crack|striping|paving|concrete|patch)[^"]*"', 'src="images/fences/wood-fence.jpg"', t)
        imgs = {
            "sealcoating.html": ["wood-fence.jpg", "wood-fence-2.jpg", "picket-fence.jpg"] * 2,
            "crack-filling.html": ["vinyl-fence.jpg", "vinyl-fence-2.jpg", "picket-fence.jpg"] * 2,
            "parking-lot-striping.html": ["picket-fence.jpg", "picket-fence-2.jpg", "wood-fence.jpg"] * 2,
            "asphalt-patching.html": ["wrought-iron-fence.jpg", "wrought-iron-fence-2.jpg", "commercial-fence.jpg"] * 2,
            "concrete-work.html": ["commercial-fence.jpg", "commercial-fence-2.jpg", "chain-link-fence.jpg"] * 2,
            "bollard-installation.html": ["chain-link-fence.jpg", "chain-link-fence-2.jpg", "commercial-fence.jpg"] * 2,
        }[name]
        for img in imgs:
            t = re.sub(
                r'(<div style="position:relative;overflow:hidden;aspect-ratio:4/3;background:#1a1a1a;"><img src=")[^"]+(" alt="" style="width:100%;height:100%;object-fit:cover;"/>)',
                rf"\1images/fences/{img}\2",
                t,
                count=1,
            )
        p.write_text(fix_text(t), encoding="utf-8")

    print("Fixes applied.")


if __name__ == "__main__":
    main()
