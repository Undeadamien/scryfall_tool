#!/usr/bin/env python

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DIR_DATA = "data"


def main():
    files = list(Path(DIR_DATA).glob("*.json"))
    if not files:
        print("Not data to load")
        return

    with open(files[0]) as file:
        df = pd.read_json(file)

    df.plot()
    plt.show()


if __name__ == "__main__":
    main()
