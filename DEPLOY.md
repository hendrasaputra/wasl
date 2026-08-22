# Deploying Wasl

The site is a single generated `index.html` at the repository root. GitHub Pages serves it
directly — there is no build step on their side, and no Jekyll (`.nojekyll` is present).

**Repository:** https://github.com/hendrasaputra/wasl
**Pages source:** branch `main`, folder `/` — already configured
**Custom domain:** `wasl.hensap.id` — set in `CNAME`, already registered with GitHub

## The one remaining step: point the domain at GitHub

Wasl uses a subdomain (`wasl.` under `hensap.id`), so this is a single **CNAME** record — no A
records, no IP addresses to keep up to date.

In **Hostinger → hPanel → Domains → hensap.id → DNS / Nameservers → Manage DNS records**, add:

| Field | Value |
|---|---|
| Type | `CNAME` |
| Name / Host | `wasl` |
| Points to / Target | `hendrasaputra.github.io` |
| TTL | leave default (or the lowest offered, while testing) |

Two things that catch people out:

- **Enter `wasl`, not `wasl.hensap.id`.** Hostinger appends the domain itself; typing the full
  name yields `wasl.hensap.id.hensap.id`.
- **The target has no `/wasl` path and no trailing dot issues** — it is exactly
  `hendrasaputra.github.io`, the *user* subdomain, not the repository URL.

Do **not** delete or change the CNAME record for anything else on `hensap.id`; this adds one
record and touches nothing existing.

## Checking it worked

```bash
dig +short wasl.hensap.id CNAME
```

Once that returns `hendrasaputra.github.io.`, GitHub will notice within a few minutes and issue
a Let's Encrypt certificate. Propagation is usually minutes, occasionally up to an hour.

Then turn on HTTPS enforcement (only works after the certificate is issued):

```bash
gh api -X PUT repos/hendrasaputra/wasl/pages -F https_enforced=true
```

And confirm the live site:

```bash
curl -sI https://wasl.hensap.id | head -1
```

## Publishing an update

`index.html` is generated and committed, so a change to the data is published by rebuilding and
pushing:

```bash
python3 validate.py && python3 test_wasl.py && python3 build.py
git add -A && git commit -m "..." && git push
```

Pages redeploys on push, usually within a minute. The CI workflow in
`.github/workflows/verify.yml` runs the same three commands on every push: it fetches the
pinned source texts, re-proves all 2,986 quotations against them, and **fails if `index.html`
is stale relative to the data** — so a page that no longer matches its own sources cannot sit
in the repository unnoticed.

## What is and is not in the repository

`corpus/*.txt` is deliberately gitignored — roughly 38 MB of source texts that belong to the
[OpenITI corpus](https://github.com/OpenITI) and are fetched, not vendored. `corpus/SHA256SUMS`
is committed, so any drift in those texts is detectable. Anyone cloning runs `./fetch.sh` once. See [LICENSING.md](LICENSING.md): the software is
GPL-3.0-or-later, the quotations are public-domain classical Arabic, and the corpus itself is
OpenITI's and is fetched rather than vendored.
