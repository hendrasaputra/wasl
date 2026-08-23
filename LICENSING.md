# Licensing

Wasl is three different kinds of thing in one repository, and they do not all carry the same
terms. This file says which is which, because a redistributor needs to know.

## 1. The software — GPL-3.0-or-later

Everything that runs: `build.py`, `validate.py`, `test_wasl.py`, `nasab.py`, `fetch.sh`,
everything in `tools/`, and `template.html` together with the CSS and JavaScript it carries into
the generated page.

> Copyright (C) 2026 Hendra Saputra
>
> This program is free software: you can redistribute it and/or modify it under the terms of the
> GNU General Public License as published by the Free Software Foundation, either version 3 of
> the License, or (at your option) any later version.
>
> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
> without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
> the GNU General Public License for more details.
>
> You should have received a copy of the GNU General Public License along with this program. If
> not, see <https://www.gnu.org/licenses/>.

The full text is in [LICENSE](LICENSE). Every source file carries an
`SPDX-License-Identifier: GPL-3.0-or-later` header.

`index.html` is generated output that embeds the template's code, so it is covered too. It is
committed so the repository is browsable without a toolchain; it is not hand-edited.

## 2. The data — `people.jsonl` and `claims.jsonl`

Also GPL-3.0-or-later as a compilation, but the parts have their own status and the distinction
matters:

- **The Arabic quotations are not ours.** They come from works whose authors died between
  151 and 630 AH (768–1233 CE). The texts are in the public domain. What a modern editor adds —
  apparatus, punctuation, pagination — is their work, and Wasl reproduces none of it beyond the
  short quotations needed to support each claim and the volume/page reference that locates them.
- **The English translations and the ALA-LC transliterations are ours**, and are released under
  the same terms as the software.
- **The structure** — which claim attaches to whom, the identifiers, the corroboration — is
  ours.

If you reuse the data, cite the printed editions named in `sources.tsv`, not this repository.
Wasl is a finding aid; the editions are the authority.

## 3. The corpus — not in this repository, and not ours

`corpus/*.txt` is deliberately **gitignored**. Those ~38 MB of machine-readable Arabic texts
belong to the [Open Islamicate Texts Initiative](https://github.com/OpenITI) and carry OpenITI's
own terms. Wasl **fetches** them (`./fetch.sh`), pins them by version URI in `sources.tsv`, and
records their checksums in `corpus/SHA256SUMS`. It does not vendor them and does not relicense
them.

This is deliberate. It keeps the repository small, it keeps provenance honest, and it means the
verification in `validate.py` runs against OpenITI's text rather than against a private copy of
it that might have drifted.

## 4. The English references — fetched to find a page, never republished

`refs/*.txt` is gitignored on the same principle as `corpus/`, and for a stronger reason.
The corpus is public-domain classical Arabic in OpenITI's machine-readable editions;
`references.tsv` pins modern translations that are **still in copyright** — A. Guillaume's
*The Life of Muhammad* is Oxford, 1955, and the scan Wasl fetches carries no licence.

Wasl reads it to establish **which page treats which person**, records that page number, and
publishes nothing from it. A page number is a fact and citing it is ordinary scholarship;
the prose is not ours to redistribute. `fetch_refs.sh` writes `refs/SHA256SUMS`, which is
committed, so the exact copy a citation was checked against stays identifiable.

The deployment enforces this rather than trusting it: the CI job that stages the site deletes
`corpus/` and `refs/` from the artifact and fails if either survives.

## 5. The biography pages are built, not stored

`bio/*.html` carries roughly 255,000 words of OpenITI's Arabic — the entries themselves, at
the pages cited. Committing them would vendor the corpus through the back door, so they are
generated in CI from the freshly fetched, checksummed text and deployed from the artifact.
The repository holds the pins in `entries.jsonl`; the published site holds the text; both come
from OpenITI's own file.

## Why GPL rather than something permissive

The point of this project is that every claim can be checked. A fork that kept the interface but
quietly dropped `validate.py`, or loosened it, would look identical and mean nothing. Copyleft
does not prevent that, but it does mean a distributed fork has to ship its source, so the check
can be inspected.
