#!/usr/bin/env bash

LINK="https://data.scryfall.io/unique-artwork/unique-artwork-20250620090548.json"
OUTPUT="unique_artwork.json"

curl "${LINK}" >"${OUTPUT}"
