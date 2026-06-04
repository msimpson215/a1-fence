#!/usr/bin/env python3
"""Remove remaining asphalt/parking imagery and copy from A1 Fence mock-up."""

from pathlib import Path
import re

PUBLIC = Path(__file__).resolve().parents[1] / "public"

SLOGAN_BLOCK = """<blockquote>&ldquo;If you <span>don&rsquo;t</span> use A1 Fence,&rdquo;<br/><span style="color:#F5C518;font-style:italic;">&ldquo;Joe has to come up with a new funny line&rdquo;</span></blockquote>"""

SLOGAN_INLINE = """<div style="font-family:'Bebas Neue',sans-serif;font-size:clamp(2rem,4vw,4rem);line-height:1.05;color:#fff;text-shadow:0 6px 20px rgba(0,0,0,.7);max-width:min(1600px,92vw);margin:0 auto;">&ldquo;If you <span style="color:#F5C518;">don&rsquo;t</span> use A1 Fence,&rdquo;<br/><span style="color:#F5C518;font-style:italic;">&ldquo;Joe has to come up with a new funny line&rdquo;</span></div>"""

BRAND_TICKER = """<section class="brand-strip" aria-label="Fence materials we install">
  <p>Materials &amp; Styles We Install</p>
  <div class="ticker-wrap">
    <div class="ticker-track">
      <img src="images/fence-brands/wood.svg" alt="Wood fencing" />
      <img src="images/fence-brands/vinyl.svg" alt="Vinyl fencing" />
      <img src="images/fence-brands/picket.svg" alt="Picket fencing" />
      <img src="images/fence-brands/wrought-iron.svg" alt="Wrought iron fencing" />
      <img src="images/fence-brands/chain-link.svg" alt="Chain link fencing" />
      <img src="images/fence-brands/aluminum.svg" alt="Aluminum fencing" />
      <img src="images/fence-brands/composite.svg" alt="Composite fencing" />
      <img src="images/fence-brands/ornamental.svg" alt="Ornamental steel fencing" />
      <img src="images/fence-brands/privacy.svg" alt="Privacy fencing" />
      <img src="images/fence-brands/ranch.svg" alt="Ranch rail fencing" />
      <img src="images/fence-brands/wood.svg" alt="Wood fencing" />
      <img src="images/fence-brands/vinyl.svg" alt="Vinyl fencing" />
      <img src="images/fence-brands/picket.svg" alt="Picket fencing" />
      <img src="images/fence-brands/wrought-iron.svg" alt="Wrought iron fencing" />
      <img src="images/fence-brands/chain-link.svg" alt="Chain link fencing" />
      <img src="images/fence-brands/aluminum.svg" alt="Aluminum fencing" />
      <img src="images/fence-brands/composite.svg" alt="Composite fencing" />
      <img src="images/fence-brands/ornamental.svg" alt="Ornamental steel fencing" />
      <img src="images/fence-brands/privacy.svg" alt="Privacy fencing" />
      <img src="images/fence-brands/ranch.svg" alt="Ranch rail fencing" />
    </div>
  </div>
</section>"""

FENCE_PHOTOS = [
    "images/fences/commercial-fence.jpg",
    "images/fences/wood-fence.jpg",
    "images/fences/vinyl-fence.jpg",
    "images/fences/picket-fence.jpg",
    "images/fences/wrought-iron-fence.jpg",
    "images/fences/chain-link-fence.jpg",
]

REPLACEMENTS = [
    ("parking-lot-gate and access layout.html", "parking-lot-striping.html"),
    ("wood and vinyl fencing.html", "sealcoating.html"),
    ("A1 Professional Asphalt &amp; Sealing LLC", "A1 Professional Fence LLC"),
    ("A1 Professional Asphalt & Sealing LLC", "A1 Professional Fence LLC"),
    ("A1 Professional Asphalt &amp; Sealing", "A1 Professional Fence"),
    ("A1 Professional Asphalt & Sealing", "A1 Professional Fence"),
    ("A1 Professional Asphalt", "A1 Professional Fence"),
    ("A1__asphalt_logo.jpeg", "A1_fence_logo_nav.jpg"),
    ("Scaling_an_asphalt_empire_with_AI.mp3", "joe-fence-interview.mp3"),
    ("Asphalt fence installation", "Commercial fence installation"),
    ("asphalt-paving", "fence-install"),
    ("asphalt-road.jpg", "images/fences/fence-hero.jpg"),
    ("asphalt background.jpg", "images/fences/fence-hero.jpg"),
    ("St. Louis skyline with asphalt sealing truck (3).png", "images/fences/picket-home-hero.jpg"),
    ("images/St. Louis skyline with asphalt sealing truck (3).png", "images/fences/picket-home-hero.jpg"),
    ("gate and access layout", "fencing"),
    ("lot fence installation", "perimeter fencing"),
    ("line gate and access layout", "perimeter layout"),
    ("fire lane gate and access layout", "security gates"),
    ("parking space regate and access layout", "entry gates"),
    ("full lot fence installation", "full perimeter fencing"),
    ("fence installation and striping", "fence design and installation"),
    ("milling and repaving", "gate and fence replacement"),
    ("full-depth milling and repaving", "full perimeter replacement"),
    ("leave the lot looking like day one", "leave the fence line looking sharp"),
    ("Sealcoating, striping, concrete", "Wood, vinyl, picket, wrought iron, chain link"),
    ("sealcoat", "fence install"),
    ("restripe", "re-gate"),
    ("repaving", "fence replacement"),
    ("bollard installation", "gate hardware"),
    ("concrete work", "commercial fencing"),
    ("ADA compliance, and fire lanes", "gates, latches, and code-compliant heights"),
    ("Handled everything including fence install, restripe, ADA compliance, and fire lanes", "Handled wood privacy, chain link perimeter, and automated gates"),
]

MARKET_COPY = {
    "commercial.html": (
        "<p>A1 Professional Fence serves retail centers, office parks, mixed-use properties, schools, and commercial facilities of every size across the Midwest and nationwide.</p>"
        "<p style=\"margin-top:16px;\">Programs include perimeter fencing, security gates, equipment yards, dumpster enclosures, and multi-site rollouts. We work nights and weekends when needed to keep your property open.</p>"
        "<p style=\"margin-top:16px;\">A1 coordinates with your facilities team or property manager — on time, on spec, and clean job sites.</p>"
    ),
    "churches.html": (
        "<p>A1 installs fencing for churches, campuses, daycares, and faith-based properties — welcoming picket at the street, privacy in back, and secure chain link where needed.</p>"
        "<p style=\"margin-top:16px;\">We respect service schedules, coordinate with volunteers, and leave grounds tidy for Sunday mornings.</p>"
    ),
    "strip-malls.html": (
        "<p>A1 serves multi-tenant retail and shopping centers with consistent fence specs across pads — rear security, dumpster screens, and decorative frontage.</p>"
        "<p style=\"margin-top:16px;\">One point of contact for multi-store programs; photo documentation on every location.</p>"
    ),
    "municipalities.html": (
        "<p>A1 works with municipalities, HOAs, parks departments, and public works on ball fields, trails, utility sites, and community perimeters.</p>"
        "<p style=\"margin-top:16px;\">Code-compliant heights, approved materials, and clear closeout packages for inspectors.</p>"
    ),
    "general-contractors.html": (
        "<p>A1 partners with general contractors on new construction and remodel fencing — temp construction fence, permanent perimeter, and punch-list closeout.</p>"
        "<p style=\"margin-top:16px;\">Reliable mobilization dates and crews that match your build schedule.</p>"
    ),
    "industrial.html": (
        "<p>A1 serves warehouses, manufacturing, and distribution with heavy-duty chain link, slide gates, and security toppings.</p>"
        "<p style=\"margin-top:16px;\">Equipment yards, loading docks, and utility corridors — built for daily truck traffic and insurance requirements.</p>"
    ),
}


def fix_photo_grid(text: str) -> str:
    def repl(m):
        idx = fix_photo_grid.i % len(FENCE_PHOTOS)
        fix_photo_grid.i += 1
        return f'src="{FENCE_PHOTOS[idx]}"'
    fix_photo_grid.i = 0
    return re.sub(r'src="images/[^"]+\.(?:jpg|jpeg|png|webp)[^"]*"', repl, text)


def fix_slogan(text: str) -> str:
    text = re.sub(
        r"<blockquote>.*?</blockquote>",
        SLOGAN_BLOCK,
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(
        r'<div style="font-family:\'Bebas Neue\'.*?fence line.*?</div>',
        SLOGAN_INLINE,
        text,
        count=1,
        flags=re.DOTALL,
    )
    return text


def main():
    for path in PUBLIC.glob("*.html"):
        text = path.read_text(encoding="utf-8")
        orig = text
        for a, b in REPLACEMENTS:
            text = text.replace(a, b)
        if path.name == "index.html":
            text = re.sub(
                r'<section class="brand-strip".*?</section>',
                BRAND_TICKER,
                text,
                count=1,
                flags=re.DOTALL,
            )
            text = fix_slogan(text)
        if "slogan-band" in text or "tagline-text" in text:
            text = fix_slogan(text)
        if path.name in MARKET_COPY:
            text = re.sub(
                r'<div class="box"><p>.*?</p></div>',
                f'<div class="box">{MARKET_COPY[path.name]}</div>',
                text,
                count=1,
                flags=re.DOTALL,
            )
        if "Project Photos" in text or "photo-grid" in text:
            text = fix_photo_grid(text)
        if path.name == "about.html":
            text = text.replace(
                "background:url('images/fences/picket-home-hero.jpg')",
                "background:url('images/fences/picket-home-hero.jpg')",
            )
        if path.name == "our-work.html":
            text = re.sub(
                r'<meta name="description" content="[^"]*"',
                '<meta name="description" content="View A1 Professional Fence project galleries — wood, vinyl, picket, wrought iron, chain link, and commercial fencing."',
                text,
                count=1,
            )
            text = text.replace(
                "From fence installation and striping to full-depth milling and repaving",
                "From backyard picket to industrial chain link and ornamental iron",
            )
        if "audio-card" in text or "Scaling_an" in text or "joe-fence" in text:
            text = re.sub(
                r"<span>Joe Schanz — Owner,[^<]*</span>",
                "<span>Joe Schanz — Owner, A1 Professional Fence LLC</span>",
                text,
            )
            text = text.replace(
                "<strong>🎙 Listen to Joe's Interview</strong>",
                "<strong>🎙 Listen to Joe — Building the Fence Business</strong>",
            )
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(path.name)


if __name__ == "__main__":
    main()
