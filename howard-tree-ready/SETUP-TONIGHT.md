# Howard Tree Pros — quick fix

## You need FILES at the top level, not folders

| Name | What it is |
|------|------------|
| `index.html` | The webpage (**file**, not a folder) |
| `styles.css` | Styling |
| `server.js` | Program Render runs (**file at top**, not inside a `server` folder) |
| `package.json` | Tells Render: run `node server.js` |
| `public-hero.png` | Your picture |

**Delete** the `server` **folder** on GitHub (you put `server.js` in the wrong place).

---

## GitHub upload (5 steps)

1. https://github.com/msimpson215/howardtreepros
2. Delete folder **`server`** (click in, delete `server.js`, then the folder).
3. Edit **`index.html`** — replace `bbbbb` with the real file (upload from computer or paste).
4. **Add file → Upload files** — upload to the **main page** of the repo (root):  
   `styles.css`, `server.js`, `package.json`, `public-hero.png`
5. Render → **Manual Deploy** (Build: `npm install`, Start: `npm start`)

Site: https://howardtreepros.onrender.com

---

## When adding a file on GitHub

In the name box type only `index.html` — **not** `index.html/` and not `myfolder/index.html` unless you want a subfolder.

Same for `server.js` — type `server.js` at the root, not `server/server.js`.
