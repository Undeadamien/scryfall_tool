#!/usr/bin/env bash

set -e

cd "$(dirname "$0")"

LINK_BULK_DATA="https://api.scryfall.com/bulk-data"
RAW_BULK_DATA="$(curl "${LINK_BULK_DATA}")"

SELECTED_TYPE="default_cards"
LINK_SELECTED_TYPE="$(jq -r --arg type "${SELECTED_TYPE}" '.data | .[] | select(.type == $type) | .download_uri' <<<"${RAW_BULK_DATA}")"

FILENAME_SELECTED_TYPE="${LINK_SELECTED_TYPE##*/}"

echo "${LINK_SELECTED_TYPE}"
echo "${FILENAME_SELECTED_TYPE}"

if [ ! -f "${FILENAME_SELECTED_TYPE}" ]; then
	find . -name "unique-artwork*.json" -delete
	curl -v "${LINK_SELECTED_TYPE}" >"${FILENAME_SELECTED_TYPE}"
fi
