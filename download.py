#!/usr/bin/env python

import json
import os
from pathlib import Path

import requests

URL = "https://api.scryfall.com/bulk-data"
TARGET_TYPE = "default_cards"
DIR_DATA = "data"


def main():
    print("Fetching the bulk data...")
    response = requests.get(URL)
    response.raise_for_status()
    data_bulk = response.json()

    url_defaults: str | None = None
    for entry in data_bulk["data"]:
        if entry["type"] == TARGET_TYPE:
            url_defaults = entry["download_uri"]
    if not url_defaults:
        print(f"Download URI not found for '{TARGET_TYPE}'")
        return

    filename = Path(url_defaults).name
    file_path = Path(DIR_DATA, filename)

    if file_path.is_file():
        print("The data is up to date. Skipping the download.")
        return

    print(f"Removing existing JSON files from {DIR_DATA}...")
    for file in Path(DIR_DATA).glob("*.json"):
        file.unlink()
        print(f" - {file}")

    print("Downloading the newest data...")
    response = requests.get(url_defaults, stream=True)
    response.raise_for_status()

    os.makedirs(DIR_DATA, exist_ok=True)
    with open(file_path, "w") as output:
        data = json.dumps(response.json(), indent=4)
        output.write(data)
    print(f"Saved new data to '{file_path}'")
    print("Done")


if __name__ == "__main__":
    main()
