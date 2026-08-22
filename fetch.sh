#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later
# Wasl - a verifiable nasab. Copyright (C) 2026 Hendra Saputra.
# Download the pinned OpenITI source texts into corpus/.
# Files are gitignored; corpus/SHA256SUMS is committed so any drift is detectable.
set -eu
cd "$(dirname "$0")"
mkdir -p corpus
tail -n +2 sources.tsv | while IFS="$(printf '\t')" read -r key uri url rest; do
  [ -z "$key" ] && continue
  if [ -f "corpus/$key.txt" ]; then echo "have  $key"; continue; fi
  echo "fetch $key"
  curl -sSL --fail --max-time 300 "$url" -o "corpus/$key.txt"
done
( cd corpus && shasum -a 256 ./*.txt | sort -k2 > SHA256SUMS )
echo "ok - $(ls corpus/*.txt | wc -l | tr -d ' ') texts"
