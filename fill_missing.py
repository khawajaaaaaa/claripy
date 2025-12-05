"""
Convenience functions for filling missing values.
"""

from __future__ import annotations

from typing import Hashable

import pandas as pd


def replace_with_mean(df: pd.DataFrame, column: Hashable) -> pd.DataFrame:
    """
    Return a copy of ``df`` where missing entries in ``column`` are replaced
    with the column mean (numeric columns only).
    """

    if column not in df.columns:
        raise KeyError("Column '{}' not found in DataFrame.".format(column))

    result = df.copy()
    numeric = pd.to_numeric(result[column], errors="coerce")
    mean_value = numeric.mean()
    result[column] = numeric.fillna(mean_value)
    return result


def replace_with_median(df: pd.DataFrame, column: Hashable) -> pd.DataFrame:
    """
    Return a copy of ``df`` where missing entries in ``column`` are replaced
    with the column median (numeric columns only).
    """

    if column not in df.columns:
        raise KeyError("Column '{}' not found in DataFrame.".format(column))

    result = df.copy()
    numeric = pd.to_numeric(result[column], errors="coerce")
    median_value = numeric.median()
    result[column] = numeric.fillna(median_value)
    return result


