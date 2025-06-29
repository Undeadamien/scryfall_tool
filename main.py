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
        df_base = pd.read_json(file)

    df = df_base

    df = df["artist"].value_counts()
    df = df.head(5)
    df = df.iloc[::-1]

    ax = df.plot(kind="barh", edgecolor="black", color="dodgerblue")
    for i, (value, _) in enumerate(zip(df.values, df.index)):
        ax.text(
            value / 2,
            i,
            str(value),
            ha="center",
            va="center",
            bbox=dict(facecolor="white", alpha=0.8),
        )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(True)

    plt.tick_params(
        axis="both",
        which="both",
        bottom=False,
        top=False,
        left=False,
        right=False,
    )
    plt.tick_params(
        axis="x",
        which="both",
        labelbottom=False,
    )
    plt.xlabel("")
    plt.ylabel("")
    plt.show()


if __name__ == "__main__":
    main()
