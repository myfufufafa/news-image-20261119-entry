# news-image-20261119 — v2 (rebuild)

Sum up 19 November's world news in one image: a broadsheet front page,
**"THE WORLD IN ONE DAY"**, Thursday 19 November 2026. The masthead claims
36 stories; the image as shipped shows the 6 leads plus briefs 7–26.

## Layout

- Masthead + subhead with the date.
- 6 lead stories with photos (2 rows x 3 columns): Trump–Xi–Putin meet in
  Shenzhen; Iran widens Gulf strikes; GTA VI launches; World Court rules on
  Myanmar; EU plans a €45bn Ukraine loan; NVIDIA beats, shares slip.
- Briefs 7–26 in columns below the leads (see note below).
- Wide world-map panel across the bottom strip with the six locations in
  today's headlines, footer "MAP: LOCATIONS IN TODAY'S HEADLINES — NOT TO
  SCALE".

## Note on briefs 27–36

Three further generations were tried to add briefs 27–36 (fresh build,
in-place edit, second fresh build). Every one of them broke something worse:
a duplicated "Washington" on the map, a missing "Gaza" label, garbled brief
text, or the edit pasting a garbled column over the map itself. The shipped
image is the clean version: all 6 leads plus briefs 7–26 (26 stories total),
with both mandated fixes verified. The masthead still reads "36 STORIES"
as in v1.

## What v2 fixes vs v1

1. **Map labels.** v1's map was a small strip with tiny, unreadable labels
   and "Kyiv" printed twice. v2's map is a tall, wide panel; each of the six
   locations — Shenzhen, the Gulf, Kyiv, Washington, Myanmar, Gaza — is
   labelled exactly once, large and legible, with leader lines where needed
   and no overlapping text. Verified by zooming into the map in the final
   1024×1024 render.
2. **Lead photo faces.** v1's lead photo had small, soft, generic faces.
   v2's photo is a large, sharp, realistic press-style shot: Trump, Xi and
   Putin big in frame at the table, each face distinct and recognisable,
   with the US, Chinese and Russian flags behind them. Verified by zooming
   into the photo in the final render.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies the shipped `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(or `/output/entry.png` by default), deterministically and byte-identically
on every run. It guards the PNG magic bytes, the 1 MiB size cap, the exact
byte size and the sha256 of the shipped image, and re-verifies the output
after writing.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py --check   # verify without writing
```

## Files

- `entry.png` — the entry image, 1024×1024 PNG, 408,385 bytes,
  sha256 `dd47cc3687e08b641850c9a2ea4d1a88c1a088816d7ad28b82daf9248281bc8e`
- `main.py` — the shipper program (Python 3.13, standard library only)
- `LICENSE` — MIT
