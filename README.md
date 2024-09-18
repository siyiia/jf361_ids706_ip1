# jf361_ids706_ip1
[![pipeline status](https://gitlab.com/SeJingjing/jf361_ids706_ip1/badges/main/pipeline.svg?job=install)](https://gitlab.com/SeJingjing/jf361_ids706_ip1/-/commits/main)
[![pipeline status](https://gitlab.com/SeJingjing/jf361_ids706_ip1/badges/main/pipeline.svg?job=format)](https://gitlab.com/SeJingjing/jf361_ids706_ip1/-/pipelines)

 ## Project Introduction
This project is to create pandas descriptive statistics script.

## Project Requirments
- Python script using Pandas for descriptive statistics
- Read a dataset (CSV or Excel)
- Generate summary statistics (mean, median, standard deviation)
- Create at least one data visualization

## Project Setup
1. **Read a CSV file** The first step is to read the dataset using Pandas. This allows you to load the data into a DataFrame for further analysis:
    ```
   import pandas as pd
    df = pd.read_csv('data/dataset.csv')
   ```
2. **Analyze Summary Statistics**: Pandas provides a convenient method `df.describe()` to generate summary statistics such as count, mean, standard deviation (std), minimum, and maximum for each numeric column in the dataset.
   ```angular2html
    analysed_data = df.describe()
    print(analysed_data)
    ```
3. **Visualizing the Data**: Pandas provides a convenient method `df.hist()` to help better understand the data distribution. Histograms are generated for each numeric column.
    ```
   df.hist(bins=10, edgecolor='black')
   ```
4. **Generate a Report**: The summary statistics and visualizations are compiled into a Markdown report. The detailed code of `create_summary_report()` method is in the `src/main.py` file.


## Project Output
The markdown summary report is under the `output` dictionary with name `summary_report.md`