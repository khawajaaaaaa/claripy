"""
claripy
=======

Utilities for quickly inspecting and lightly cleaning tabular datasets.

The most important user‑facing functions are re‑exported here for
convenience so that typical usage looks like::

    from claripy import load_csv, summarize_column

See the module‑level docstrings for more detailed information.
"""

from .data_io import load_csv, export_csv
from .data_profile import missing_summary, column_overview, data_profile
from .stats_tools import summarize_column
from .fill_missing import replace_with_mean, replace_with_median
from .detect_outliers import flag_outliers, trim_outliers
from .quick_viz import show_histogram, plot_box

__all__ = [
    "load_csv",
    "export_csv",
    "missing_summary",
    "column_overview",
    "data_profile",
    "summarize_column",
    "replace_with_mean",
    "replace_with_median",
    "flag_outliers",
    "trim_outliers",
    "show_histogram",
    "plot_box",
]


