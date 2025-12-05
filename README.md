claripy

claripy is a small Python package that helps data scientists and analysts quickly
inspect and clean raw tabular datasets. It focuses on the very first stage of a
data‑science workflow: loading files safely, understanding the basic structure
of a dataset, handling missing values, detecting outliers, and running fast
visual checks.

The package is organized as a collection of focused modules:

- `data_io`: Safe loading and saving of CSV files.
- `data_profile`: Quick, high‑level summaries of a dataset (column overview and
  missing‑value profile).
- `stats_tools`: Simple descriptive statistics for individual columns.
- `fill_missing`: Convenience functions for filling missing values.
- `detect_outliers`: Simple helpers for flagging and trimming outliers.
- `quick_viz`: One‑line wrappers for quick histogram and box‑plot views.
- `ai_summary` (optional): A very small, rule‑based helper that turns the data
  profile tables into a plain‑text description using simple string formatting
  (no external AI calls are made).

The implementation mainly relies on `pandas`, `numpy`, and `matplotlib`.

The included `tests/` folder contains small unit tests that exercise the main
functions of the package. They are written using Python’s built‑in `unittest`
framework so they can be run with:


python -m unittest discover -s tests
