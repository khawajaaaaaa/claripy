"""
Tools for importing and exporting tabular datasets.

The focus of this module is on *safe* CSV loading: clearly reporting errors and
using sensible defaults that are appropriate for quick exploratory work.
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

import pandas as pd

PathLike = Union[str, Path]


def load_csv(path: PathLike, **read_csv_kwargs) -> pd.DataFrame:
    """
    Load a CSV file into a :class:`pandas.DataFrame`.

    Parameters
    ----------
    path:
        Path to a ``.csv`` file.
    **read_csv_kwargs:
        Additional keyword arguments passed directly to :func:`pandas.read_csv`.
        A few safe defaults are applied if the caller does not override them:

        - ``na_values`` is extended with common dirty markers such as
          ``\"ERROR\"`` and ``\"UNKNOWN\"``.
        - ``keep_default_na`` is set to ``True``.

    Returns
    -------
    pandas.DataFrame
        The loaded dataset.
    """

    full_path = Path(path)
    if not full_path.exists():
        # Use ``format`` instead of an f‑string to minimise any issues with
        # different Python versions or encodings.
        raise FileNotFoundError("CSV file not found: {}".format(full_path))

    # Start from user‑provided kwargs but make sure we include a few convenient
    # NA markers that show up in the cafe dataset.
    na_values = set(read_csv_kwargs.pop("na_values", []))
    na_values.update({"ERROR", "UNKNOWN", ""})

    df = pd.read_csv(
        full_path,
        na_values=list(na_values),
        keep_default_na=True,
        **read_csv_kwargs,
    )
    return df


def export_csv(df: pd.DataFrame, path: PathLike, index: bool = False, **to_csv_kwargs) -> None:
    """
    Save a :class:`pandas.DataFrame` to disk as a CSV file.

    Parameters
    ----------
    df:
        The DataFrame to save.
    path:
        Destination file path. Parent directories are created automatically.
    index:
        Whether to write the DataFrame index into the file (defaults to
        ``False`` for cleaner outputs).
    **to_csv_kwargs:
        Additional keyword arguments forwarded to :meth:`pandas.DataFrame.to_csv`.
    """

    full_path = Path(path)
    full_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(full_path, index=index, **to_csv_kwargs)


