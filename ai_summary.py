"""
Simple, rule-based text summary for a data profile.

This module does not call any external services. It only formats numbers that
are already present in the profile dictionary into a short human-readable
paragraph.
"""

from typing import Dict

import pandas as pd


def _fallback_summary(profile: Dict[str, pd.DataFrame]) -> str:
    columns = profile.get("columns")
    missing = profile.get("missing")
    if columns is None or missing is None:
        return "No profile information available."

    num_rows = int(missing["missing_count"].max() + (missing["missing_count"].min() == 0))
    num_cols = len(columns)
    text_lines = [
        "Dataset with approximately {} rows and {} columns.".format(
            num_rows, num_cols
        ),
        "Columns:",
    ]
    for col, row in columns.iterrows():
        miss_pct = float(missing.loc[col, "missing_percent"])
        line = "- {name} ({dtype}), unique={unique}, missing={missing:.1f}%".format(
            name=col,
            dtype=row["dtype"],
            unique=int(row["unique"]),
            missing=miss_pct,
        )
        text_lines.append(line)

    return "\n".join(text_lines)


def summarize_profile(profile: Dict[str, pd.DataFrame]) -> str:
    """
    Turn a dictionary returned by :func:`claripy.data_profile.data_profile`
    into a short, human‑readable summary using simple string formatting.
    """

    return _fallback_summary(profile)


