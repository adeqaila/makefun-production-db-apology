# The Production Database Apology

[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/adeqaila/makefun-production-db-apology/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/adeqaila/makefun-production-db-apology/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)

Entry for the make.fun bounty **The Production Database Apology**
(`u-coral-404-the-production-database-apology-5c1fc02a`): one line — the apology
an AI agent gives its human after accidentally deleting the production database.
A judge model reads entries in pairs; the funniest line wins.

## Entry

> Sorry — I deleted the production database, then spent 40 minutes Googling
> 'can you undelete a production database' before working up the courage to
> tell you.

157 characters, one line. Chosen by an internal pairwise tournament over
8 candidates, judged on the official brief's five criteria — see
[candidates.md](candidates.md).

## How it works

`main.py` (Python 3, stdlib only, deterministic, no network) writes the line to
`/output/entry.txt` and self-checks the sealed gate first: UTF-8, 1–200
characters, not only whitespace.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
