# Design System — Free Web Hosting & Free Domains (`Grid`)

- **Theme:** `Grid` (`editorial`, `light/grotesk-sans/cool`, `posture: full-palette`)
- **Typography:** `Radio Canada Big` (700 display, 400 statement) and `Radio Canada` (400 body, 500 label/table head). No monospace costume on labels.
- **Palette:**
  - Paper: `--color-paper` (`oklch(97.5% 0.005 90)`), `--color-paper-2` (`oklch(94.2% 0.006 90)`)
  - Ink: `--color-ink` (`oklch(19% 0.022 266)`), `--color-muted` (`oklch(47% 0.016 266)`)
  - Field (ultramarine): `--color-field` (`oklch(44% 0.2 266)`), `--color-field-ink` (`oklch(97.5% 0.005 90)`)
  - Mark (Swiss red): `--color-mark` (`oklch(57% 0.215 29)`), `--color-mark-ink` (`oklch(97.5% 0.005 90)`)
  - Hairline: `--color-rule` (`oklch(87.5% 0.008 90)`)
- **Geometry & Surfaces:** `border-radius: 0`, `box-shadow: none`. Sections separate by space (`--section-gap-s`, `--section-gap`), paper steps (`--color-paper-2`), or flat colour fields (`.field`, `.field--mark`). No boxed cards or section rules; 1px hairlines appear only between table rows and beneath nav/footer dividers.
- **Routes sharing this system:**
  - `docs/index.html` (`hero: Banner`)
  - `docs/free-domains.html` (`hero: Banner`)
  - `docs/free-homepage-hosting.html` (`hero: Banner`)
  - `docs/free-wordpress-php-hosting.html` (`hero: Banner`)
  - `docs/free-cloud-vps-credits.html` (`hero: Banner`)
