# Valor Ideal Trading — redesigned site

Static HTML/CSS/JS. No build step, no framework, no dependencies except Google Fonts (see Performance).

## Deploy
1. `assets/img/` already contains the new logo (`logo-v2.png`, `logo-v2-light.png`) and the five cropped pack shots, under the same file names as the live site. Re-upload them with the pages.
2. Upload everything to the web root, replacing the current `.html` files.
3. In `enquire.html`, replace `YOUR_FORM_ID` in the form action with your form-service endpoint (e.g. Formspree). Until then the form opens the visitor's email app, pre-filled.
4. `build.py` (optional, kept alongside) regenerates the pages if you want to edit shared header/footer in one place.

## Design system
Colours (taken from the Valor logo): ink #101F3A, navy 900 #0A2858, navy 700 #1D4A8A, leaf green #1F7A47, gold (actions) #E0B13F, mist #E6EDF6, foam #F5F8FC.
Product tints (chips/rules only): D3 #F2B544, children's D3 #6EC1E4, iron #D9694E, zinc #7F9BB3, B12 #E58BA0.
Type: Bricolage Grotesque (headings), Public Sans (body). Scale ratio ~1.25, defined as CSS variables.
Motif: the droplet corner (three rounded corners, one sharp) on image frames, list markers and step markers.

## Higgsfield assets (generate, review, then add)
See the chat response for prompts. Target folder: `assets/img/`. Export WebP, plus JPG fallback if needed.
- H1 hero visual: `hero-mist.webp` 1200x1200 → replace the `<svg>` inside `.hero-art` on index.html with
  `<img src="assets/img/hero-mist.webp" alt="..." width="1200" height="1200" fetchpriority="high">`
- H2 hero loop (optional): `hero-mist.mp4` ≤1.5 MB, muted, loop, `poster` = H1.
- H3 page-head texture: `head-mist.webp` 1600x400 (optional, used as background on inner pages).
- H4 social card: a built-in `og-valor.png` (1200x630) is already in use; replace it with a generated one if you like.

## Accessibility
Skip link, semantic landmarks, visible focus ring, labelled form fields, aria-current on nav, keyboard-operable menu (Esc closes), reduced-motion respected, text contrast ≥ 4.5:1.

## Performance
Only one small script (deferred). Images are lazy-loaded below the fold with width/height set. For best speed, self-host the two fonts (woff2) and remove the Google Fonts links; verify product-photo dimensions and update width/height attributes.

## SEO — see chat response for the change log
All five URLs, titles, meta descriptions and canonicals are identical to the live site.
