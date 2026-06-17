# Foam Nation Arizona — STATUS (paused 2026-06-17 EOD)

Resume tomorrow morning here. The site is **built, verified, and committed** — the only
thing left is choosing how to put it live.

## ✅ Done & ready to launch
Single-file site (`index.html`). Verified on desktop + mobile, no console errors.

- **Hero** — photo slideshow cycling 10 clean family foam photos (pulled from your Drive `FOAM DADDY PICTURES`).
- **Tickets** — 4 tiers with **real prices + perks**, wired to **live Posh checkout** (`posh.vip/e/foam-party-18`):
  - Single Entry — **from $10** (early bird; GA $28.49)
  - General Admission Plus — **$35** · incl. an Automatic Bubble Gun machine *(premium card)*
  - Family 4-Pack — **$100** · buy 4 get 1 free, ~20% off
  - VIP Family Bundle — **$150** · 5-for-4 + free face painting each + Bubble Gun machine *(premium card)*
- **Gallery** (12 clean photos), **Dink & Dine venue**, **Foam Daddy partner** section.
- Real logo in the **nav** + **footer**; blue/turquoise/yellow flyer palette; `foamnationarizona@gmail.com` in footer.
- All committed to local git (73 files). Staging originals + unused montage excluded via `.gitignore`.

## ⏭️ Next session — two threads

### 1. Deploy (pick a host)
- **GitHub Pages (fastest):** run `gh auth refresh -s repo` and click authorize → I create the repo, push, and enable Pages.
  *(The current `gh` token can't create repos — this grants the scope.)*
- **Netlify / Vercel:** I run `npx` deploy, you log in once → cleaner URL + easy custom domain.
- **Custom domain:** see thread 2.

### 2. National pivot (new direction)
Rebrand to national **"Foam Nation"** — one site, events across major US cities, structured **by city**,
plus a **"find the foam party near me"** geolocation feature (opt-in button → nearest city). The current
Arizona site becomes the template for city #1.
- **You:** buy a **"Foam Nation" domain** + a **new email set** *(I can't purchase — financial action)*.
  `foamnation.com` is likely taken; consider `foamnationusa.com`, `getfoamnation.com`, `.party`, `.events` — confirm at a registrar.
- **Me:** refactor to a `CITIES` data model + city selector + geolocation once the domain's chosen.

## 🔧 Pre-launch polish (non-blocking)
- Real **Instagram / TikTok** handles in the footer (currently placeholder).
- Add the FN webhook to the **Foam Nation Posh org** + update the Lambda to accept its secret (backend, separate).
- Optional: absolute `og:image` URL for social share previews; a real hero background video (slideshow works fine now).
