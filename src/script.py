import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.lib import (
    read_csv_file,
    get_std,
    get_mean,
    get_median,
    get_all_statistics,
    create_visualization,
)


def custom_describe(file_path, col):
    general_df = read_csv_file(file_path)
    describe_dict = {
        "name": col,
        "mean": get_mean(general_df, col),
        "std": get_std(general_df, col),
        "median": get_median(general_df, col),
    }
    return describe_dict


def create_summary_report(file_path, output_dir=Path("./output")):
    raw_data = read_csv_file(file_path)
    summary_stats = get_all_statistics(raw_data)
    output_file = output_dir / "summary_report.md"

    markdown_content = "# Summary Report\n\n"
    markdown_content += "## Dataset Overview\n\n"
    markdown_content += "This dataset provides a comprehensive overview of various factors affecting student performance in exams.\n\n"
    markdown_content += "### First 5 Rows of the Dataset\n\n"
    markdown_content += raw_data.head().to_markdown() + "\n\n"

    markdown_content += "## Summary Statistics\n\n"
    markdown_content += summary_stats.to_markdown() + "\n\n"

    markdown_content += "## Data Visualization\n\n"
    create_visualization(raw_data, summary_stats, output_dir)
    markdown_content += "![Data Visualization](./data_visualization.png)\n\n"

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)
