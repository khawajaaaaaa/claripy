"""
Quick visualization helpers for exploratory data analysis.
"""

from __future__ import annotations

from typing import Hashable, Optional

import matplotlib.pyplot as plt
import pandas as pd


def show_histogram(
    df: pd.DataFrame,
    column: Hashable,
    bins: int = 10,
    title: Optional[str] = None,
) -> None:
    """
    Display a histogram for a numeric column.
    """

    if column not in df.columns:
        raise KeyError("Column '{}' not found in DataFrame.".format(column))

    series = pd.to_numeric(df[column], errors="coerce")
    plt.figure()
    series.plot.hist(bins=bins)
    plt.xlabel(str(column))
    plt.ylabel("Count")
    plt.title(title or "Histogram of {}".format(column))
    plt.tight_layout()
    plt.show()


def plot_box(
    df: pd.DataFrame,
    column: Hashable,
    title: Optional[str] = None,
) -> None:
    """
    Display a box‑plot for a numeric column.
    """

    if column not in df.columns:
        raise KeyError("Column '{}' not found in DataFrame.".format(column))

    series = pd.to_numeric(df[column], errors="coerce")
    plt.figure()
    plt.boxplot(series.dropna())
    plt.ylabel(str(column))
    plt.title(title or "Box plot of {}".format(column))
    plt.tight_layout()
    plt.show()


