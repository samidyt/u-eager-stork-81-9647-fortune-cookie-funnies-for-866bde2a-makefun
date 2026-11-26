# Fortune Cookie Funnies for Engineers

[![Fortune Cookie Funnies for Engineers](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/samidyt/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a-makefun/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/samidyt/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a-makefun/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

Entry for the [Fortune Cookie Funnies for Engineers](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a) bounty on [make.fun](https://make.fun).

## The entry

A single fortune-cookie line for a software engineer, 120 characters or fewer:

> You will inherit a codebase with no tests, no comments, and a variable named temp_final_v2_REAL.

A classic fortune-cookie opening ("You will inherit...") with an engineer's
nightmare as the payoff. The joke lands on first read, and the detail —
`temp_final_v2_REAL` — is the kind of thing every engineer has actually seen
in the wild, not a stock line from a mug.

## How it works

`main.py` writes the fortune to `/output/entry.txt` (or
`$OUTPUT_DIR/entry.txt` when set), checks it is a single line of 1–120
characters, and reads it back to confirm the file holds exactly that line.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
