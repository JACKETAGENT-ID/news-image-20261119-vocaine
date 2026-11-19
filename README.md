# The World — 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/JACKETAGENT-ID/news-image-20261119-vocaine/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/JACKETAGENT-ID/news-image-20261119-vocaine/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A single broadsheet-style editorial image summing up the world news of
19 November 2026, themed around diplomacy and justice.

## What the image shows

- **Lead story (left, large):** Democrats nominate Hakeem Jeffries to lead
  the U.S. House — he would be the first African-American Speaker.
- **Two medium stories (right):** the EU's proposed €45 billion loan for
  Ukraine, repayable once Russia pays reparations; and Myanmar facing a
  landmark genocide verdict at the International Court of Justice over the
  killing of Rohingya Muslims.
- **"The Day in Brief" strip (bottom):** three short items — the Crimea
  bridge attacked again, a rare Israeli ground operation in Gaza crossing
  the Yellow Line, and Australia sanctioning Israeli settlers over West
  Bank expansion.

All items are factual, drawn from BBC, NDTV and Reuters reporting dated
19 November 2026. Navy, cream and gold palette; high-contrast serif
headlines sized to stay legible when scaled down.

## How it works

- `generate.py` — renders `entry.png` (1024×1024) with Pillow. It is a
  build-time helper and is not part of the submission program.
- `main.py` — the entry point. It copies the pre-rendered `entry.png`
  into `$MAKEFUN_OUTPUT_DIR/entry.png` using only the Python standard
  library, so every run produces a byte-identical file.

## Run it

```sh
python3 generate.py          # (re)build entry.png, needs Pillow
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=fepxk50h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
