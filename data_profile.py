"""
High‑level profiling utilities for a dataset.

These helpers provide a quick snapshot of a :class:`pandas.DataFrame` without
pulling in a heavy profiling dependency.
"""

from __future__ import annotations

from typing import Dict

import pandas as pd


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute a simple missing‑value summary for each column.

    Returns a new DataFrame with the number and percentage of missing entries.
    """

    total = len(df)
    missing = df.isna().sum()
    percent = (missing / total) * 100 if total > 0 else 0
    summary = pd.DataFrame(
        {
            "missing_count": missing,
            "missing_percent": percent.round(2),
        }
    )
    return summary


def column_overview(df: pd.DataFrame) -> pd.DataFrame:
    """
    Provide a compact overview of each column in ``df``.

    The result contains:

    - data type
    - number of unique values
    - a small example sample value (first non‑missing value)
    """

    overview_records = []
    for col in df.columns:
        series = df[col]
        sample_value = series.dropna().iloc[0] if series.dropna().size > 0 else None
        overview_records.append(
            {
                "column": col,
                "dtype": series.dtype.name,
                "unique": series.nunique(dropna=True),
                "sample_value": sample_value,
            }
        )

    overview = pd.DataFrame(overview_records).set_index("column")
    return overview


def data_profile(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Build a small dictionary of profile components for ``df``.

    The profile currently includes:

    - ``"missing"``: output of :func:`missing_summary`
    - ``"columns"``: output of :func:`column_overview`
    """

    return {
        "missing": missing_summary(df),
        "columns": column_overview(df),
    }


