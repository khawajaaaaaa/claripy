"""
Helpers for flagging and trimming outliers in numeric columns.

The current implementation uses the inter‑quartile range (IQR) rule::

    outlier < Q1 - 1.5 * IQR  or  outlier > Q3 + 1.5 * IQR
"""

from __future__ import annotations

from typing import Hashable, Tuple

import numpy as np
import pandas as pd


def _iqr_bounds(series: pd.Series) -> Tuple[float, float]:
    numeric = pd.to_numeric(series, errors="coerce")
    q1 = numeric.quantile(0.25)
    q3 = numeric.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return float(lower), float(upper)


def flag_outliers(df: pd.DataFrame, column: Hashable) -> pd.Series:
    """
    Return a boolean Series indicating which rows in ``column`` are outliers
    according to the IQR rule.
    """

    if column not in df.columns:
        raise KeyError("Column '{}' not found in DataFrame.".format(column))

    lower, upper = _iqr_bounds(df[column])
    numeric = pd.to_numeric(df[column], errors="coerce")
    mask = (numeric < lower) | (numeric > upper)
    # Missing values are never flagged as outliers.
    mask = mask.fillna(False)
    return mask


def trim_outliers(df: pd.DataFrame, column: Hashable) -> pd.DataFrame:
    """
    Return a copy of ``df`` with rows containing outliers in ``column``
    removed.
    """

    mask = ~flag_outliers(df, column)
    return df.loc[mask].copy()


