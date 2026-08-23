#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
#
# Download the pinned English reference texts into refs/.
#
# Same contract as fetch.sh and for a stronger reason. These are IN COPYRIGHT: Guillaume's
# translation is Oxford, 1955, and the scan carries no licence. Wasl fetches it to find out
# which page treats which person, records the page number, and publishes nothing from it. A
# page number is a fact; the prose is not ours to redistribute. refs/ is gitignored and
# refs/SHA256SUMS is committed, so the copy a citation was checked against is identifiable.
set -eu
cd "$(dirname "$0")"
mkdir -p refs
tail -n +2 references.tsv | while IFS="$(printf '\t')" read -r key kind author title translates edition archive file url note; do
  [ -z "$key" ] && continue
  if [ -f "refs/$key.txt" ]; then echo "have  $key"; continue; fi
  echo "fetch $key"
  curl -sSL --fail --max-time 300 "$url" -o "refs/$key.txt"
done
( cd refs && shasum -a 256 ./*.txt | sort -k2 > SHA256SUMS )
echo "ok - $(ls refs/*.txt | wc -l | tr -d ' ') reference text(s)"
