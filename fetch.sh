#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
# Download the pinned OpenITI source texts into corpus/.
# Files are gitignored; corpus/SHA256SUMS is committed so any drift is detectable.
set -eu
cd "$(dirname "$0")"
mkdir -p corpus
refresh=false
[ "${1:-}" = "--refresh-checksums" ] && refresh=true
tail -n +2 sources.tsv | while IFS="$(printf '\t')" read -r key uri url rest; do
  [ -z "$key" ] && continue
  if [ -f "corpus/$key.txt" ]; then echo "have  $key"; continue; fi
  echo "fetch $key"
  tmp="corpus/$key.txt.tmp"
  rm -f "$tmp"
  if ! curl -sSL --fail --max-time 300 "$url" -o "$tmp"; then
    rm -f "$tmp"
    echo "error: failed to fetch $key" >&2
    exit 1
  fi
  mv "$tmp" "corpus/$key.txt"
done
if $refresh; then
  ( cd corpus && shasum -a 256 ./*.txt | sort -k2 > SHA256SUMS )
  echo "refreshed corpus/SHA256SUMS"
else
  ( cd corpus && shasum -a 256 -c SHA256SUMS )
fi
echo "ok - $(ls corpus/*.txt | wc -l | tr -d ' ') texts"
