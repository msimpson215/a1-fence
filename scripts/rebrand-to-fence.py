#!/usr/bin/env python3
"""Rebrand A1 Asphalt site copy and assets to A1 Professional Fence."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

GLOBAL_REPLACEMENTS = [
    ("A1__asphalt_logo.jpeg", "A1_fence_logo.svg"),
    ("A1 Professional Asphalt &amp; Sealing LLC", "A1 Professional Fence LLC"),
    ("A1 Professional Asphalt & Sealing LLC", "A1 Professional Fence LLC"),
    ("A1 Professional Asphalt &amp; Sealing", "A1 Professional Fence"),
    ("A1 Professional Asphalt & Sealing", "A1 Professional Fence"),
    ("A1 Professional Asphalt home", "A1 Professional Fence home"),
    ("A1 Professional Asphalt", "A1 Professional Fence"),
    ("a1asphaltpro.com", "a1fencepro.com"),
    ("A1AsphaltPros", "A1FencePros"),
    ("a-1-asphalt-pros", "a-1-fence-pros"),
    ("a1-professional-asphalt", "a1-professional-fence"),
    ("Full-service asphalt and concrete company", "Full-service commercial and residential fencing company"),
    ("asphalt and concrete", "fencing and perimeter security"),
    ("commercial asphalt", "commercial fencing"),
    ("Commercial Asphalt", "Commercial Fencing"),
    ("Pavement Solutions", "Fence Solutions"),
    ("pavement maintenance", "fence installation and repair"),
    ("parking lot", "property perimeter"),
    ("Parking Lot", "Property Perimeter"),
    ("sealcoat and restripe", "design, install, and maintain fences"),
    ("sealcoat and maintenance", "fence installation and maintenance"),
    ("Asphalt sealcoating", "Commercial fence installation"),
    ("Parking lot striping", "Picket & privacy fencing"),
    ("Crack filling commercial", "Vinyl & wood fencing"),
    ("Commercial paving nationwide", "Chain link & wrought iron nationwide"),
    ("If you <span>don&rsquo;t</span> use A1 Asphalt, it&rsquo;s your own <span>asphalt</span>", "If you <span>don&rsquo;t</span> use A1 Fence, it&rsquo;s your own <span>fence line</span>"),
    ("If you <span>don&#8217;t</span> use A1 Asphalt, it&#8217;s your own <span>asphalt</span>", "If you <span>don&#8217;t</span> use A1 Fence, it&#8217;s your own <span>fence line</span>"),
    ("use A1 Asphalt,<br/>it&rsquo;s your own <span style=\"color:#F5C518;\">asphalt</span>", "use A1 Fence,<br/>it&rsquo;s your own <span style=\"color:#F5C518;\">fence line</span>"),
    ("The Last <span>Asphalt Company</span>", "The Last <span>Fence Company</span>"),
    ("Commercial sealcoating, striping, paving, and concrete services", "Wood, vinyl, picket, wrought iron, chain link, and commercial perimeter fencing"),
    ("finished lot that looks sharp", "finished fence line that looks sharp"),
    ("Subcontract pavement work", "Subcontract fencing and perimeter work"),
    ("Heavy-duty pavement maintenance", "Heavy-duty perimeter fencing and security"),
    ("asphalt-road.jpg", "images/fences/fence-hero.jpg"),
    ("asphalt background.jpg", "images/fences/fence-hero.jpg"),
    ("images/striping%20parking%20lot.png", "images/fences/commercial-fence.jpg"),
    ("Scaling_an_asphalt_empire_with_AI.mp3", "Scaling_an_asphalt_empire_with_AI.mp3"),  # keep file if present
]

NAV_SERVICES = """        <li><a href="ai-estimator.html">AI Estimator</a></li>
        <li><a href="sealcoating.html">Wood Fencing</a></li>
        <li><a href="crack-filling.html">Vinyl Fencing</a></li>
        <li><a href="parking-lot-striping.html">Picket Fencing</a></li>
        <li><a href="asphalt-patching.html">Wrought Iron</a></li>
        <li><a href="concrete-work.html">Commercial Fencing</a></li>
        <li><a href="bollard-installation.html">Chain Link</a></li>"""

MOBILE_SERVICES = """  <a href="sealcoating.html">Wood Fencing</a>
  <a href="crack-filling.html">Vinyl Fencing</a>
  <a href="parking-lot-striping.html">Picket Fencing</a>
  <a href="asphalt-patching.html">Wrought Iron</a>
  <a href="concrete-work.html">Commercial Fencing</a>
  <a href="bollard-installation.html">Chain Link</a>"""

FOOTER_SERVICES = """        <li style="margin-bottom:10px;"><a href="sealcoating.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Wood Fencing</a></li>
        <li style="margin-bottom:10px;"><a href="crack-filling.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Vinyl Fencing</a></li>
        <li style="margin-bottom:10px;"><a href="parking-lot-striping.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Picket Fencing</a></li>
        <li style="margin-bottom:10px;"><a href="asphalt-patching.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Wrought Iron</a></li>
        <li style="margin-bottom:10px;"><a href="concrete-work.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Commercial Fencing</a></li>
        <li style="margin-bottom:10px;"><a href="bollard-installation.html" style="color:#fff;text-decoration:none;font-size:0.85rem;">Chain Link</a></li>"""

SERVICES = {
    "sealcoating.html": {
        "title": "Wood Fencing",
        "hero_h1": "Wood Fencing",
        "hero_span": "Built to Last",
        "hero_sub": "Cedar, pine, and pressure-treated privacy fences — residential and commercial.",
        "hero_bg": "images/fences/wood-fence.jpg",
        "body_h2": "Why Wood Fencing",
        "body_span": "Works",
        "body_p1": "Wood remains the most popular choice for backyards, campuses, and light commercial perimeters. We help you pick the right species, height, and board-on-board or shadowbox layout for privacy without blocking airflow.",
        "body_p2": "Our crews set posts in concrete, keep lines true, and use stainless or coated fasteners so your fence stands up to Midwest weather. Staining and sealing options are available on request.",
        "body_p3": "From HOA communities to restaurant patios, A1 coordinates access, materials, and schedule so your property stays secure and good-looking.",
        "checklist": [
            "Privacy, semi-privacy, and ranch-rail styles",
            "Pressure-treated posts and rot-resistant options",
            "Custom gates and walk-through entries",
            "Residential, church, and commercial properties",
            "Repair, replacement, and new installs",
            "Serving St. Louis and the Midwest",
        ],
        "gallery": [
            "images/fences/wood-fence.jpg",
            "images/fences/wood-fence-2.jpg",
            "images/fences/picket-fence.jpg",
        ],
    },
    "crack-filling.html": {
        "title": "Vinyl Fencing",
        "hero_h1": "Vinyl Fencing",
        "hero_span": "Low Maintenance",
        "hero_sub": "Clean white or tan vinyl — no painting, built for long-term curb appeal.",
        "hero_bg": "images/fences/vinyl-fence.jpg",
        "body_h2": "Why Vinyl",
        "body_span": "Fencing",
        "body_p1": "Vinyl gives you a crisp, uniform look year after year without the upkeep of paint or stain. It resists rot, insects, and splintering — ideal for pools, schools, and retail outparcels.",
        "body_p2": "We install industry-standard rail-and-picket systems with reinforced posts and aluminum inserts where needed for wind load. Color-matched caps and gates keep the line professional.",
        "body_p3": "Property managers love vinyl because it photographs well for leasing materials and holds up to pressure washing when the lot needs a refresh.",
        "checklist": [
            "Privacy and semi-privacy panels",
            "Pool-code heights and self-latching gates",
            "No painting or sealing required",
            "Retail, multifamily, and municipal sites",
            "Matching column and accent options",
            "Fast turnaround on standard layouts",
        ],
        "gallery": [
            "images/fences/vinyl-fence.jpg",
            "images/fences/vinyl-fence-2.jpg",
            "images/fences/picket-fence.jpg",
        ],
    },
    "parking-lot-striping.html": {
        "title": "Picket Fencing",
        "hero_h1": "Picket Fencing",
        "hero_span": "Classic Curb Appeal",
        "hero_sub": "Front-yard charm, garden borders, and decorative low fences.",
        "hero_bg": "images/fences/picket-fence.jpg",
        "body_h2": "Picket Style",
        "body_span": "Done Right",
        "body_p1": "Picket fences define the American front yard — welcoming, neat, and perfect for defining landscape beds without a solid wall of boards.",
        "body_p2": "We offer traditional pointed pickets, dog-ear, and scalloped tops in wood or vinyl. Spacing and height follow local codes and HOA guidelines.",
        "body_p3": "Whether you are framing a historic home or dressing up a new build, A1 keeps picket lines crisp and gates aligned.",
        "checklist": [
            "3–4 ft decorative heights",
            "Wood or vinyl picket systems",
            "Garden and sidewalk borders",
            "HOA-friendly designs",
            "Custom gate widths",
            "Repair of storm-damaged sections",
        ],
        "gallery": [
            "images/fences/picket-fence.jpg",
            "images/fences/picket-fence-2.jpg",
            "images/fences/wood-fence.jpg",
        ],
    },
    "asphalt-patching.html": {
        "title": "Wrought Iron Fencing",
        "hero_h1": "Wrought Iron",
        "hero_span": "& Ornamental Metal",
        "hero_sub": "Elegant security for estates, churches, and upscale commercial entries.",
        "hero_bg": "images/fences/wrought-iron-fence.jpg",
        "body_h2": "Iron &amp; Steel",
        "body_span": "Perimeters",
        "body_p1": "Ornamental iron and steel fencing adds presence at driveways, monuments, and main entries while keeping sight lines open.",
        "body_p2": "We work with powder-coated panels, welded pickets, and automated gate packages. Posts are set deep with proper footings for long-term stability.",
        "body_p3": "Pair wrought iron with masonry pillars or brick columns for a finished architectural look.",
        "checklist": [
            "Driveway and entry gates",
            "Spear-top and flat-top styles",
            "Powder-coated black, bronze, or custom colors",
            "Welded panels and rackable sections",
            "Churches, estates, and boutique retail",
            "Integrated access control prep",
        ],
        "gallery": [
            "images/fences/wrought-iron-fence.jpg",
            "images/fences/wrought-iron-fence-2.jpg",
            "images/fences/commercial-fence.jpg",
        ],
    },
    "concrete-work.html": {
        "title": "Commercial Fencing",
        "hero_h1": "Commercial",
        "hero_span": "Fencing",
        "hero_sub": "Perimeter security for retail, industrial, schools, and job sites.",
        "hero_bg": "images/fences/commercial-fence.jpg",
        "body_h2": "Commercial",
        "body_span": "Programs",
        "body_p1": "National retailers and industrial owners need fencing that meets insurance, safety, and aesthetic standards. A1 delivers turnkey perimeter packages — layout, install, and punch-list closeout.",
        "body_p2": "We coordinate with GC schedules, after-hours access, and phased installs so operations stay open. Bollards, equipment yards, and dumpster enclosures are part of the scope.",
        "body_p3": "Multi-site rollouts are our strength: one point of contact, consistent specs, photo documentation on every location.",
        "checklist": [
            "Chain link, iron, and hybrid systems",
            "Security gates and slide operators",
            "Equipment and storage yards",
            "Retail outparcels and pads",
            "Municipal and school campuses",
            "Nationwide program management",
        ],
        "gallery": [
            "images/fences/commercial-fence.jpg",
            "images/fences/commercial-fence-2.jpg",
            "images/fences/chain-link-fence.jpg",
        ],
    },
    "bollard-installation.html": {
        "title": "Chain Link Fencing",
        "hero_h1": "Chain Link",
        "hero_span": "Fencing",
        "hero_sub": "Affordable, durable perimeter — the classic cyclone fence for security.",
        "hero_bg": "images/fences/chain-link-fence.jpg",
        "body_h2": "Chain Link",
        "body_span": "Systems",
        "body_p1": "Chain link (often called cyclone fencing) is the workhorse of commercial and industrial sites — visible security without blocking airflow or light.",
        "body_p2": "We install galvanized and vinyl-coated fabric, top rails, tension wire, and barbed or razor options where code allows. Slatted privacy inserts are available.",
        "body_p3": "From 4 ft landscape borders to 10 ft security perimeters, A1 sets posts on center and pulls fabric tight for a professional finish.",
        "checklist": [
            "Galvanized and black vinyl-coated",
            "Barbed wire and security toppings",
            "Slatted privacy screens",
            "Temporary construction fence",
            "Gates for vehicles and personnel",
            "Industrial and warehouse yards",
        ],
        "gallery": [
            "images/fences/chain-link-fence.jpg",
            "images/fences/chain-link-fence-2.jpg",
            "images/fences/commercial-fence.jpg",
        ],
    },
}

GALLERY_PAGES = {
    "gallery-sealcoating.html": ("Wood Fencing Gallery", "Wood Fencing", "images/fences/wood-fence.jpg", SERVICES["sealcoating.html"]["gallery"]),
    "gallery-crackfill.html": ("Vinyl Fencing Gallery", "Vinyl Fencing", "images/fences/vinyl-fence.jpg", SERVICES["crack-filling.html"]["gallery"]),
    "gallery-striping.html": ("Picket Fencing Gallery", "Picket Fencing", "images/fences/picket-fence.jpg", SERVICES["parking-lot-striping.html"]["gallery"]),
    "gallery-paving.html": ("Wrought Iron Gallery", "Wrought Iron", "images/fences/wrought-iron-fence.jpg", SERVICES["asphalt-patching.html"]["gallery"]),
    "gallery-concrete.html": ("Commercial Fencing Gallery", "Commercial Fencing", "images/fences/commercial-fence.jpg", SERVICES["concrete-work.html"]["gallery"]),
    "gallery-patching.html": ("Chain Link Gallery", "Chain Link", "images/fences/chain-link-fence.jpg", SERVICES["bollard-installation.html"]["gallery"]),
}


def apply_global(text: str) -> str:
    for old, new in GLOBAL_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def replace_nav_services(text: str) -> str:
    text = re.sub(
        r"<ul class=\"drop\">.*?</ul>",
        f"<ul class=\"drop\">\n{NAV_SERVICES}\n      </ul>",
        text,
        count=1,
        flags=re.DOTALL,
    )
    # Mobile menu service links (between Services anchor and Our Work)
    text = re.sub(
        r'(<a href="index\.html#services">Services</a>\s*)'
        r'(<a href="sealcoating\.html">)[^<]+(</a>\s*)'
        r'(<a href="crack-filling\.html">)[^<]+(</a>\s*)'
        r'(<a href="parking-lot-striping\.html">)[^<]+(</a>\s*)'
        r'(<a href="(?:asphalt-patching|our-work)\.html">)[^<]+(</a>)',
        r"\1" + MOBILE_SERVICES + "\n  ",
        text,
        count=1,
    )
    # Footer inline service list (compact)
    text = re.sub(
        r"<li style=\"margin-bottom:10px;\"><a href=\"sealcoating\.html\"[^>]*>[^<]+</a></li>"
        r".*?"
        r"<li style=\"margin-bottom:10px;\"><a href=\"bollard-installation\.html\"[^>]*>[^<]+</a></li>",
        FOOTER_SERVICES,
        text,
        count=1,
        flags=re.DOTALL,
    )
    # Footer ul without inline styles
    text = re.sub(
        r"<li style=\"margin-bottom:10px;\"><a href=\"sealcoating\.html\" style=\"color:#fff[^\"]*\">Sealcoating</a></li>.*?"
        r"<li style=\"margin-bottom:10px;\"><a href=\"bollard-installation\.html\"[^>]*>Bollards</a></li>",
        FOOTER_SERVICES,
        text,
        count=1,
        flags=re.DOTALL,
    )
    return text


def patch_service_page(path: Path, cfg: dict) -> None:
    text = path.read_text(encoding="utf-8")
    text = apply_global(text)
    text = replace_nav_services(text)
    text = re.sub(r"<title>[^<]*</title>", f"<title>{cfg['title']} — A1 Professional Fence LLC</title>", text, count=1)
    text = re.sub(
        r"background:url\('[^']*'\) center",
        f"background:url('{cfg['hero_bg']}') center",
        text,
        count=1,
    )
    text = re.sub(
        r"<h1>[^<]*<br/><span>[^<]*</span></h1>",
        f"<h1>{cfg['hero_h1']}<br/><span>{cfg['hero_span']}</span></h1>",
        text,
        count=1,
    )
    text = re.sub(r'<p class="hero-sub">[^<]*</p>', f'<p class="hero-sub">{cfg["hero_sub"]}</p>', text, count=1)
    text = re.sub(
        r"<h2>[^<]*<span>[^<]*</span></h2>",
        f"<h2>{cfg['body_h2']} <span>{cfg['body_span']}</span></h2>",
        text,
        count=1,
    )
    ps = re.findall(r"<div class=\"body-text\">(.*?)</div>\s*<div>", text, re.DOTALL)
    if ps:
        checklist_html = "\n".join(f"        <li>{item}</li>" for item in cfg["checklist"])
        new_body = f"""<div class="body-text">
      <h2>{cfg['body_h2']} <span>{cfg['body_span']}</span></h2>
      <p>{cfg['body_p1']}</p>
      <p>{cfg['body_p2']}</p>
      <p>{cfg['body_p3']}</p>
      
      <ul class="checklist">
{checklist_html}
      </ul>
    """
        text = text.replace(ps[0], new_body, 1)

    for i, img in enumerate(cfg["gallery"] * 2):
        text = re.sub(
            r'(<div style="position:relative;overflow:hidden;aspect-ratio:4/3;background:#1a1a1a;"><img src=")[^"]+(" alt="" style="width:100%;height:100%;object-fit:cover;"/>)',
            rf"\1{cfg['gallery'][i % len(cfg['gallery'])]}\2",
            text,
            count=1,
        )
    path.write_text(text, encoding="utf-8")


def patch_gallery_page(path: Path, title: str, label: str, hero_bg: str, images: list) -> None:
    text = apply_global(path.read_text(encoding="utf-8"))
    text = replace_nav_services(text)
    text = re.sub(r"<title>[^<]*</title>", f"<title>{title} — A1 Professional Fence LLC</title>", text, count=1)
    text = text.replace("Asphalt", label).replace("Sealcoating", label).replace("Crack Filling", label)
    text = text.replace("Striping", label).replace("Paving", label).replace("Concrete", label).replace("Patching", label)
    text = re.sub(
        r"background:url\('images/[^']+'\)",
        f"background:url('{hero_bg}')",
        text,
        count=1,
    )
    for img in images * 3:
        text = re.sub(
            r'src="images/[^"]+\.jpg"',
            f'src="{img}"',
            text,
            count=1,
        )
    path.write_text(text, encoding="utf-8")


def patch_index_contact_options(text: str) -> str:
    return re.sub(
        r"<option>Sealcoating</option><option>Crack Filling</option><option>Striping</option><option>Patching</option>",
        "<option>Wood Fencing</option><option>Vinyl Fencing</option><option>Picket Fencing</option>"
        "<option>Wrought Iron</option><option>Chain Link</option><option>Commercial Fencing</option>",
        text,
    )


def main() -> None:
    targets = list(PUBLIC.glob("*.html")) + [ROOT / "package.json", ROOT / "README.md", PUBLIC / "styles.css", ROOT / "scripts" / "sync-site-nav.py"]
    for path in targets:
        if not path.exists():
            continue
        text = apply_global(path.read_text(encoding="utf-8"))
        if path.suffix == ".html":
            text = replace_nav_services(text)
        if path.name == "index.html":
            text = patch_index_contact_options(text)
            text = text.replace(
                "Industries <span>We Serve</span>",
                "Fence Types <span>We Install</span>",
            )
            text = text.replace(
                "Built for commercial properties, retail centers, municipalities, industrial facilities, and general contractors.",
                "Wood, vinyl, picket, wrought iron, chain link, and full commercial perimeter programs.",
            )
            # Service cards on homepage -> fence types
            card_replacements = [
                ('href="commercial.html" class="service-card" style="--img:url(\'images/commercial.jpg\')"',
                 'href="sealcoating.html" class="service-card" style="--img:url(\'images/fences/wood-fence.jpg\')"',
                 "<h3>Commercial Properties</h3><p>Retail centers, office parks, and commercial facilities with full sealcoat and restripe programs.</p>",
                 "<h3>Wood Fencing</h3><p>Privacy and perimeter wood fences for homes, HOAs, churches, and light commercial sites.</p>"),
                ('href="churches.html" class="service-card" style="--img:url(\'images/church.jpg\')"',
                 'href="crack-filling.html" class="service-card" style="--img:url(\'images/fences/vinyl-fence.jpg\')"',
                 "<h3>Churches &amp; Apartments</h3><p>Parking lot maintenance for churches, apartment complexes, condominiums, and community facilities.</p>",
                 "<h3>Vinyl Fencing</h3><p>Low-maintenance vinyl for pools, schools, apartments, and retail outparcels.</p>"),
                ('href="strip-malls.html" class="service-card" style="--img:url(\'images/Retail-Strip-Malls.png\')"',
                 'href="parking-lot-striping.html" class="service-card" style="--img:url(\'images/fences/picket-fence.jpg\')"',
                 "<h3>Retail &amp; Strip Malls</h3><p>National retailers, shopping centers, and multi-tenant properties — sealcoating, striping, ADA compliance, and fire lanes.</p>",
                 "<h3>Picket Fencing</h3><p>Classic front-yard picket and garden borders — wood or vinyl, HOA-friendly heights.</p>"),
                ('href="municipalities.html" class="service-card" style="--img:url(\'images/Apartments-Municipalities.png\')"',
                 'href="asphalt-patching.html" class="service-card" style="--img:url(\'images/fences/wrought-iron-fence.jpg\')"',
                 "<h3>Apartments &amp; Municipalities</h3><p>Apartment complexes, condominiums, HOA communities, and municipal properties — full sealcoat and maintenance programs.</p>",
                 "<h3>Wrought Iron</h3><p>Ornamental iron entries, monuments, churches, and upscale commercial driveways.</p>"),
                ('href="general-contractors.html" class="service-card" style="--img:url(\'images/genral-contractor.picture.jpeg\')"',
                 'href="concrete-work.html" class="service-card" style="--img:url(\'images/fences/commercial-fence.jpg\')"',
                 "<h3>General Contractors</h3><p>Subcontract fencing and perimeter work for GC projects with reliable crews and clean schedules.</p>",
                 "<h3>Commercial Fencing</h3><p>Perimeter security for retail pads, industrial yards, schools, and multi-site programs.</p>"),
                ('href="industrial.html" class="service-card" style="--img:url(\'images/Industrial-warehouse.png\')"',
                 'href="bollard-installation.html" class="service-card" style="--img:url(\'images/fences/chain-link-fence.jpg\')"',
                 "<h3>Industrial &amp; Warehouse</h3><p>Heavy-duty perimeter fencing and security for distribution centers, warehouses, and industrial facilities.</p>",
                 "<h3>Chain Link</h3><p>Galvanized and vinyl-coated cyclone fencing for warehouses, utilities, and construction sites.</p>"),
            ]
            for old_href, new_href, old_body, new_body in card_replacements:
                text = text.replace(old_href, new_href)
                text = text.replace(old_body, new_body)
            text = text.replace(
                "Handled everything including sealcoat, restripe, ADA compliance, and fire lanes. Night and day difference.",
                "Handled wood privacy, chain link perimeter, and automated gates. Night and day difference.",
            )
            text = text.replace(
                "A1 handled multiple locations this season. On time, professional crew, and the lots look incredible.",
                "A1 handled multiple locations this season. On time, professional crew, and the fences look incredible.",
            )
        path.write_text(text, encoding="utf-8")

    for fname, cfg in SERVICES.items():
        p = PUBLIC / fname
        if p.exists():
            patch_service_page(p, cfg)

    for fname, meta in GALLERY_PAGES.items():
        p = PUBLIC / fname
        if p.exists():
            patch_gallery_page(p, *meta)

    print("Rebrand complete.")


if __name__ == "__main__":
    main()
