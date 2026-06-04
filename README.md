# A1 Professional Fence — Website

Clone of the A1 asphalt site structure, rebranded for fencing services (wood, vinyl, picket, wrought iron, chain link, commercial).

**Mock-up for Joe:** fence branding and photos; **phone numbers unchanged** from the asphalt site (314 / 618 offices). Logo artwork may still show 888 on the graphic — CTAs use the real lines.

## Key files

- `server/server.js` — web server
- `package.json` — dependencies
- `public/index.html` — homepage
- `public/A1_fence_logo.jpg` — full sign for hero/footer
- `public/A1_fence_logo_nav.jpg` — compact header logo
- Drop your designer’s original over these files anytime for a perfect match
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

## Deploy on Render (Node)

1. Push this repo to GitHub (`msimpson215/a1-fence`).
2. [render.com](https://render.com) → **New** → **Web Service** → connect the repo.
3. Use these settings:

| Setting | Value |
|--------|--------|
| **Environment** | Node |
| **Branch** | `main` (or `cursor/a1-fence-rebrand-0567` until merged) |
| **Root Directory** | *(leave blank)* |
| **Build Command** | `npm install` |
| **Start Command** | `npm start` |

**Environment variables** — none required. Render sets `PORT` automatically; the app already uses `process.env.PORT`.

Optional:

| Key | Value |
|-----|--------|
| `NODE_VERSION` | `20` |

4. **Create Web Service** → Render gives you a URL like `https://a1-fence.onrender.com`.

After deploy, open `/index.html` or `/` for the homepage.

## Rebrand scripts

- `scripts/rebrand-to-fence.py` — initial copy/asset swap
- `scripts/fix-fence-rebrand.py` — cleanup after global replace
