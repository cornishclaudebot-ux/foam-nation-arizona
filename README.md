# Foam Nation Arizona — events site

Single self-contained website for **Foam Nation Arizona** — family foam parties at
Dink & Dine Pickle Park, Mesa, AZ. Powered by Foam Daddy, built by the DartyForLife team.

- **One file:** `index.html` (no build step, no dependencies). Photos in `/img`.
- **Brand:** bright/sunny, patriotic red + sky blue + Foam Daddy teal + foam white. Baloo 2 + Nunito.
- **Sections:** hero w/ live countdown · The Foam Days (events) · Experience · Venue (Dink & Dine) ·
  Gallery · stats · FAQ · CTA band · footer. Posh inline-checkout modal built in.

---

## ✏️ Edit your events

Open `index.html`, scroll to the `EVENTS` array near the bottom (inside `<script>`).

```js
{ id:"july4", name:"July 4th Foam Party", tier:"family", date:"2026-07-04",
  kind:"Fourth of July · family all-ages", doors:"2:00 – 6:00 PM", startHour:14,
  venue:"Dink & Dine Pickle Park", city:"Mesa, AZ", img:"img/fn-26.jpg",
  posh:"", priceFrom:"10", cta:{label:"Get tickets"} },
```

- `tier` — `"family"` (all-ages) or `"18"` (18+ after dark).
- `date` — ISO `YYYY-MM-DD`. **Past dates auto-hide.** Next upcoming event drives the hero countdown.
- `doors` — display text · `startHour` — 24h number used for the countdown.
- `img` — any photo in `/img` (fn-01…fn-37 already copied in).
- `priceFrom` — the early-bird price shown as "From $X".
- Currently live: **July 25** only (July 4 was cancelled). An 18+ "after dark" stub is commented out —
  uncomment and set a real date when locked. **Only publish dates you've committed to.**

## 💸 Family / group pricing (`#pricing`)
Explains the deal: **Single Entry** vs the featured **Family 4-Pack = Buy 4, get 1 free** (5 entries for
the price of 4 ≈ **20% off**). Both "Get tickets" buttons route to the July 25 Posh checkout, where the
actual 4-Pack ticket type / promo lives. Edit the copy/prices directly in the `#pricing` section HTML.

## 🎨 Brand
Official logo: `img/logo-white.png` (white lockup, used big in the hero). Palette = the Posh flyer's
**blues + turquoise + yellow** (CSS variables `--blue`, `--turq`, `--cyan`, `--yellow` in `:root`).
Yellow is the primary "buy" button color; blue/turquoise are structure/accents.

---

## 🎬 Hero background video
The first screen plays a full-bleed, **blurred** background video behind the logo + ticketing.

**Currently wired in:** `img/hero.mp4` — a Ken Burns motion montage built from the real family-foam
photos (opens on the Foam Daddy cannon), as an interim until an AI foam-cannon clip is generated.
Rebuild/tweak it with `python3 build-hero-montage.py` (needs ffmpeg; edit the `photos` list / timings).

To swap in a different video (e.g. the AI foam-cannon clip):
1. Drop your MP4 (H.264, ~10–20s loop, web-compressed) into `/img` as `img/hero.mp4` (overwrite).
2. `const HERO_VIDEO = "img/hero.mp4";` is already set near the bottom of the script (a hosted URL works too).
   It autoplays **muted** + loops (required for autoplay).
3. The clip is blurred/darkened via CSS (`.hero-video { filter: blur(7px) brightness(.82) ... }`) so the
   foreground logo pops and any baked-in photo watermark disappears — **reduce the blur there** if your
   clip should read sharp.
4. Poster (shown before the video loads) = `img/venue/dd-aerial.jpg` on the `<video id="heroVideo">` tag.

## 🤝 Foam Daddy partner section
`#partner` showcases the partnership — the Foam Daddy logo (`img/foam-daddy-logo.webp`), the
"exclusively powered by Foam Daddy" story, and their verified claims (hypoallergenic, non-toxic,
biodegradable, non-staining). Source claims: foamdaddy.com. Photo: `img/fn-03.jpg`.

## 📍 Venue (Dink & Dine) photos
`#venue` uses real Dink & Dine photos in `/img/venue/` (aerial, food, courts, patio) pulled from
dinkanddine.com, plus the address **1017 N Dobson Rd, Mesa, AZ 85201**. Swap any by changing the
filename. *Courtesy note: confirm with Dink & Dine that you're cleared to use their photos (you're
hosting there, so likely fine) — or replace with your own.*

---

## 🎟️ Posh ticketing (READ THIS)

Two settings at the top of the `<script>`:

1. **`POSH_ORG_URL`** — your Foam Nation storefront on Posh.
   > ⚠️ It currently points to the **known-live DartyForLife storefront** (`posh.vip/g/dartyforlife`)
   > as a placeholder so nothing is broken. **Replace it** with the real Foam Nation storefront.
   > If Foam Nation sells under its *own* Posh org, use that URL. Don't guess a slug that might 404.

2. **Per-event `posh` slug** — the part after `posh.vip/e/` (Posh dashboard → Event → Share).
   - Set it → "Get tickets" opens **that event's checkout inside this site** (iframe modal).
   - Leave `""` → opens the storefront in a new tab.

### The webhook — one setup step, then automatic
Foam Nation runs its **own Posh org**, so it is **NOT** covered by the DartyForLife webhook. Add your
webhook to the Foam Nation org once: **Posh → Settings → API Webhooks** → same API Gateway URL +
`Posh-Secret` you already use. After that, sales flow through your **AWS Lambda automatically** — the
parser is schema-tolerant and already captures `event_name`, buyer, quantity, total, and promo/ambassador
attribution, so Foam Nation sales land in DynamoDB → QBO / iMessage / Sheet / dashboard with **zero code changes**.

---

## 🖼️ Photos
37 curated event photos live in `/img` (`fn-01.jpg` … `fn-37.jpg`), copied from the finished shoot set.
Swap any card/gallery image by changing the filename. To add more, drop them in `/img` and reference
`img/yourfile.jpg`. (They already carry the "Foam Nation Arizona · Powered by Foam Daddy" watermark.)

## 🔗 Social links
`SOCIAL = { instagram:"", tiktok:"" }` at the top of the script. Fill in the real handles and the
footer links light up automatically (they're hidden while empty).

## ▶️ Preview
Launch config **foam** → `python3 -m http.server 4318 --directory ~/foam-nation-site` (port 4318).
Must be served over http(s) — the Posh iframe won't load from `file://`.

## 🚀 Deploy
Drag the folder onto **Netlify Drop**, or push to **GitHub Pages** / Cloudflare Pages. Must be **https**
(Posh checkout won't iframe otherwise). Point a domain (e.g. foamnationaz.com) at it.

---

## ✅ Fill-in checklist before going live
- [ ] Replace `POSH_ORG_URL` with the real Foam Nation storefront.
- [ ] Add per-event `posh` slugs (July 4, July 25) for in-site checkout.
- [ ] **Add your webhook to the Foam Nation Posh org** (separate org → not covered by the DFL webhook).
- [ ] Paste your **hero background video** (`HERO_VIDEO` + drop `img/hero.mp4`).
- [ ] Confirm ticket prices (`priceFrom`) and gate times match Posh.
- [ ] Add real Instagram / TikTok handles in `SOCIAL`. (Email `foamnationarizona@gmail.com` already in footer.)
- [ ] (Optional) Confirm Dink & Dine photo usage; double-check foam-safety wording (uses Foam Daddy's published claims).
- [ ] Add any additional confirmed dates (or the 18+ after-dark night).
- [ ] Deploy to https + custom domain. Optional: real OG share image.
