import sys
import os
import pandas as pd
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.lib import (
    read_csv_file,
    get_mean,
    get_median,
    get_std,
    get_all_statistics,
    create_visualization,
)


@pytest.fixture
def sample_data():
    data = {"col1": [10, 20, 30, 40, 50], "col2": [5, 15, 25, 35, 45]}
    return pd.DataFrame(data)


def test_read_csv_file(tmp_path):
    temp_file = tmp_path / "test.csv"
    temp_file.write_text("col1,col2\n10,5\n20,15\n30,25\n40,35\n50,45")

    df = read_csv_file(temp_file)
    assert not df.empty
    assert list(df.columns) == ["col1", "col2"]
    assert len(df) == 5


def test_get_mean(sample_data):
    assert get_mean(sample_data, "col1") == 30
    assert get_mean(sample_data, "col2") == 25


def test_get_median(sample_data):
    assert get_median(sample_data, "col1") == 30
    assert get_median(sample_data, "col2") == 25


def test_get_std(sample_data):
    assert round(get_std(sample_data, "col1"), 2) == 15.81
    assert round(get_std(sample_data, "col2"), 2) == 15.81


def test_get_all_statistics(sample_data):
    stats_data = get_all_statistics(sample_data)

    assert "mean" in stats_data.index
    assert "median" in stats_data.index
    assert "std" in stats_data.index
    assert stats_data.loc["mean", "col1"] == 30
    assert stats_data.loc["median", "col2"] == 25


def test_create_visualization(sample_data, tmp_path):
    output_file = tmp_path / "data_visualization.png"

    stats_data = pd.DataFrame(
        {"mean": [30, 25], "median": [30, 25]}, index=["col1", "col2"]
    ).T

    create_visualization(sample_data, stats_data, output_dir=tmp_path)

    assert output_file.exists()
