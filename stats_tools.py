"""
Basic statistical helpers for quick column summaries.
"""

from __future__ import annotations

from typing import Dict, Hashable

import pandas as pd


def summarize_column(df: pd.DataFrame, column: Hashable) -> Dict[str, float]:
    """
    Calculate simple descriptive statistics for a numeric column.

    Parameters
    ----------
    df:
        Input DataFrame.
    column:
        Column label to summarize.

    Returns
    -------
    dict
        A dictionary with keys ``count``, ``mean``, ``median``, and ``std``.
    """

    if column not in df.columns:
        # Avoid f-strings/escaped quotes issues; use format instead.
        raise KeyError("Column '{}' not found in DataFrame.".format(column))

    series = pd.to_numeric(df[column], errors="coerce")
    desc = {
        "count": int(series.count()),
        "mean": float(series.mean()),
        "median": float(series.median()),
        "std": float(series.std(ddof=1)) if series.count() > 1 else 0.0,
    }
    return desc


