# A1 Professional Fence — Website

Clone of the A1 asphalt site structure, rebranded for fencing services (wood, vinyl, picket, wrought iron, chain link, commercial).

## Key files

- `server/server.js` — web server
- `package.json` — dependencies
- `public/index.html` — homepage
- `public/A1_fence_logo.svg` — logo (replace with your final artwork)
- `public/images/fences/` — fence category photos (Unsplash stock; swap for your project photos)

## Service pages (same URLs as asphalt template)

| Page | Fence type |
|------|------------|
| `sealcoating.html` | Wood |
| `crack-filling.html` | Vinyl |
| `parking-lot-striping.html` | Picket |
| `asphalt-patching.html` | Wrought iron |
| `concrete-work.html` | Commercial |
| `bollard-installation.html` | Chain link |

## Deploy

Same flow as the asphalt site: push to GitHub, connect Render, `npm install`, start command `node server/server.js` (or root `server.js` per your Render config).

## Rebrand scripts

- `scripts/rebrand-to-fence.py` — initial copy/asset swap
- `scripts/fix-fence-rebrand.py` — cleanup after global replace
