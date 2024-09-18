import sys
import os
import pandas as pd
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.script import custom_describe, create_summary_report


@pytest.fixture
def sample_data():
    data = {"col1": [10, 20, 30, 40, 50], "col2": [5, 15, 25, 35, 45]}
    return pd.DataFrame(data)


def test_custom_describe(sample_data, tmp_path):
    temp_file = tmp_path / "test.csv"
    sample_data.to_csv(temp_file, index=False)

    describe_data = custom_describe(temp_file, "col1")

    assert describe_data["mean"] == 30
    assert describe_data["median"] == 30
    assert round(describe_data["std"], 2) == 15.81


def test_create_summary_report(sample_data, tmp_path):
    temp_file = tmp_path / "test.csv"
    sample_data.to_csv(temp_file, index=False)

    output_file = tmp_path / "summary_report.md"

    create_summary_report(temp_file, output_dir=tmp_path)

    assert output_file.exists()

    with open(output_file, "r") as f:
        content = f.read()
        assert "## Dataset Overview" in content
        assert "## Summary Statistics" in content
        assert "## Data Visualization" in content
