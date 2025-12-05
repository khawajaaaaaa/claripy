import os
import unittest

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # use non-interactive backend suitable for tests
import matplotlib.pyplot as plt

import claripy
from claripy.ai_summary import summarize_profile


DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dirty_cafe_sales.csv")


class TestClaripyCore(unittest.TestCase):
    def setUp(self) -> None:
        # Use a small in-memory DataFrame for most tests.
        self.df = pd.DataFrame(
            {
                "A": [1.0, 2.0, None, 4.0],
                "B": [10.0, 10.0, 20.0, 1000.0],
            }
        )

    def test_load_csv_works_on_sample_file(self) -> None:
        df = claripy.load_csv(DATA_PATH)
        # Expect the cafe dataset to have 10k rows and 8 columns.
        self.assertEqual(df.shape[1], 8)
        self.assertGreaterEqual(df.shape[0], 1000)

    def test_missing_and_column_profile(self) -> None:
        profile = claripy.data_profile(self.df)
        self.assertIn("missing", profile)
        self.assertIn("columns", profile)
        self.assertEqual(set(profile["missing"].index), {"A", "B"})

    def test_summarize_column(self) -> None:
        stats = claripy.summarize_column(self.df, "A")
        # Column A has 3 non-missing values: 1, 2, 4
        self.assertEqual(stats["count"], 3)
        self.assertAlmostEqual(stats["median"], 2.0)

    def test_fill_missing_with_mean(self) -> None:
        filled = claripy.replace_with_mean(self.df, "A")
        self.assertFalse(filled["A"].isna().any())

    def test_flag_and_trim_outliers(self) -> None:
        mask = claripy.flag_outliers(self.df, "B")
        # 1000 should be flagged as an outlier.
        self.assertTrue(mask.iloc[-1])
        trimmed = claripy.trim_outliers(self.df, "B")
        self.assertEqual(len(trimmed), 3)

    def test_text_summary_runs(self) -> None:
        df = claripy.load_csv(DATA_PATH)
        profile = claripy.data_profile(df)
        text = summarize_profile(profile)
        self.assertIsInstance(text, str)
        self.assertIn("Dataset with approximately", text)

    def test_quick_viz_functions_do_not_crash(self) -> None:
        # The plotting helpers should run without raising, using the Agg backend.
        claripy.show_histogram(self.df, "A")
        claripy.plot_box(self.df, "B")


if __name__ == "__main__":
    unittest.main()


