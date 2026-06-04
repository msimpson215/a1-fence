#!/usr/bin/env python3
"""Convert Joe's example fence PNGs into public/images/fences/*.jpg and market cards."""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "public" / "images"
FENCES = IMG / "fences"
MARKETS = IMG / "markets"

# source PNG -> one or more output JPG paths
MAPPING = {
    "wood1.png": [
        FENCES / "wood-fence.jpg",
        FENCES / "wood-fence-2.jpg",
    ],
    "vinyl1.png": [
        FENCES / "vinyl-fence.jpg",
        FENCES / "vinyl-fence-2.jpg",
        FENCES / "fence-hero.jpg",
        MARKETS / "residential.jpg",
    ],
    "picket1.png": [
        FENCES / "picket-fence.jpg",
        FENCES / "picket-fence-2.jpg",
        FENCES / "picket-home-hero.jpg",
        MARKETS / "hoa.jpg",
    ],
    "cyclone1.png": [
        FENCES / "chain-link-fence.jpg",
    ],
    "commercial1.png": [
        FENCES / "commercial-fence.jpg",
        FENCES / "commercial-fence-2.jpg",
    ],
    "commercial2.png": [
        FENCES / "wrought-iron-fence.jpg",
        FENCES / "wrought-iron-fence-2.jpg",
        FENCES / "chain-link-fence-2.jpg",
    ],
}

MAX_EDGE = 1920
JPEG_QUALITY = 88


def save_jpg(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        if max(w, h) > MAX_EDGE:
            scale = MAX_EDGE / max(w, h)
            im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        im.save(dest, "JPEG", quality=JPEG_QUALITY, optimize=True)
    print(f"  {dest.relative_to(ROOT)}")


def main() -> None:
    print("Wiring example fence photos...")
    for name, outputs in MAPPING.items():
        src = IMG / name
        if not src.exists():
            raise SystemExit(f"Missing source: {src}")
        print(f"{name} ->")
        for out in outputs:
            save_jpg(src, out)
    print("Done.")


if __name__ == "__main__":
    main()
