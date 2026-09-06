# Color theory for miniature painting

Notes from a session on picking colors for D&D miniatures, plus a visual
palette sheet.

- [`squint-test-palettes.html`](./squint-test-palettes.html) — the swatch
  reference. Open it in a browser. Seven palettes shown as a 4-role × 3-value
  grid (Dominant / Support / Accent / Neutral across; Highlight / Base / Shadow
  down). Has a **Squint Test** button that drains the hue from every swatch at
  once, and click-to-copy hex codes.
- [Test palletes](https://htmlpreview.github.io/?https://github.com/DanRoscigno/DnD/blob/master/colortheory/squint-test-palettes.html)
- [Published copy](https://claude.ai/code/artifact/e6ccc56c-dd55-4726-beaa-35b711a33323)

---

## The three ideas that carry most of the weight

Color theory for minis is simpler than the art-school version, because a
miniature is viewed at arm's length.

**1. Value beats hue.** Value = how light or dark a color is, ignoring what
color it is. If your armor, cloak, and skin are all mid-tone, the model reads as
mush from three feet away no matter how nice the colors are. Aim for a clear
light / mid / dark split across the big areas. Squint at the model — if the
shapes still separate, you're fine.

**2. Limit yourself to 2–3 hues plus neutrals.** The classic ratio is roughly
60 / 30 / 10 — a dominant color, a supporting color, and a small accent that's
the loudest thing on the model. Beginners usually fail by giving every pouch and
strap its own color; the eye then has nowhere to land.

**3. Pick a relationship, not just colors.** The four that matter:

- **Complementary** — opposite on the wheel (red/green, blue/orange,
  purple/yellow). Maximum punch. Use one as the big area and one as the small
  accent, never 50/50.
- **Split-complementary** — one color plus the two neighbors of its opposite
  (blue + orange-yellow + orange-red). Same energy, easier to not make it look
  like Christmas.
- **Analogous** — neighbors on the wheel (blue, blue-green, green). Harmonious
  and moody; needs a strong value range or a metallic to keep it from going flat.
- **Triadic** — three evenly spaced (red/yellow/blue). Bold, heraldic, very
  "classic fantasy knight."

Also worth knowing: **warm vs. cool** is a shortcut that works even within one
hue. Warm light with cool shadows (or the reverse) makes a model look lit rather
than just colored. And **metallics are colors** — gold is a warm yellow-orange,
steel is a cool grey. Count them in your scheme.

## Concrete sets to steal

| Scheme | Main (60%) | Support (30%) | Accent (10%) | Good for |
|---|---|---|---|---|
| **Classic hero** (complementary) | Deep blue cloth | Steel / cool grey | Warm gold trim | Paladins, clerics, city guard |
| **Autumn ranger** (analogous + accent) | Olive green | Warm leather brown | Rust orange | Druids, rangers, scouts |
| **Necrotic** (split-comp) | Bone / pale ivory | Dark cool grey | Sickly green + purple shadows | Undead, liches, crypts |
| **Infernal** (complementary) | Charcoal black | Dark red | Molten orange glow | Devils, tieflings, fire cults |
| **Fey** (analogous) | Teal | Sage green | Magenta or hot pink accent | Fey, elves, enchanters |
| **Desert** (warm analogous) | Sandy tan | Terracotta | Turquoise (cool break) | Nomads, genasi, tomb settings |
| **Regal villain** (complementary) | Royal purple | Black leather | Gold + bone | Warlocks, vampire nobles |

## Practical tricks

- **Desaturate everything except the accent.** If the cloak is a slightly greyed
  blue, a pure bright gold buckle sings. If the cloak is also pure saturated,
  they fight.
- **Tie the model together with one shared color.** Mix a little of your accent
  color into the shadows or a couple of unrelated details elsewhere on the model.
  It stops the scheme from looking like separate stickers.
- **Base and model should relate.** A cool grey stone base under a warm-toned
  model is free contrast; a green grass base under a green cloak kills it.
- **Painting a party or warband?** Keep one color constant across all of them
  (same leather brown, same metal) and vary the accent per model — that's how you
  get "these belong together" without them looking identical.

## Exact values

The hex ramps, wash recommendations, and nearest Citadel paint matches for all
seven palettes live in `squint-test-palettes.html` (see the `PALETTES` array in
the script block if you want the raw data). Paint names there are closest common
matches, not exact conversions — test them on a wet palette before committing to
a whole squad.
