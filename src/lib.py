import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path


# Load file
def read_csv_file(file_path):
    raw_data_df = pd.read_csv(file_path)
    return raw_data_df


# Descriptive statistics
def get_mean(raw_data_df, colname):
    data_mean = raw_data_df[colname].mean()
    return data_mean


def get_median(raw_data_df, colname):
    data_median = raw_data_df[colname].median()
    return data_median


def get_std(raw_data_df, colname):
    data_std = raw_data_df[colname].std()
    return data_std


def get_all_statistics(raw_data_df):
    stats_data = (
        raw_data_df.describe()
        .loc[["mean", "50%", "std"]]
        .rename(index={"50%": "median"})
    )
    return stats_data


# Data visualization
def create_visualization(
    data_df, stats_data, output_dir=Path("./output"), color="skyblue", jupyter=False
):
    axes = data_df.hist(bins=10, edgecolor="black", figsize=(12, 10), color=color)
    output_file = output_dir / "data_visualization.png"

    for ax, col in zip(axes.flatten(), stats_data.columns):
        mean_val = stats_data.loc["mean", col]
        median_val = stats_data.loc["median", col]

        ax.axvline(
            mean_val,
            color="red",
            linestyle="dashed",
            linewidth=2,
            label=f"Mean: {mean_val:.2f}",
        )
        ax.axvline(
            median_val,
            color="blue",
            linestyle="dotted",
            linewidth=2,
            label=f"Median: {median_val:.2f}",
        )

        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        ax.legend()

    plt.tight_layout()

    if jupyter:
        plt.show()
    else:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        plt.savefig(output_file)
        plt.close()
