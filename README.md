# jf361_ids706_ip1
[![Install](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/install.yml/badge.svg)](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/install.yml)
[![Format](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/format.yml/badge.svg)](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/format.yml)
[![Lint](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/lint.yml/badge.svg)](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/lint.yml)
[![Test](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/test.yml/badge.svg)](https://github.com/siyiia/jf361_ids706_ip1/actions/workflows/test.yml)

### Video Link
[Watch the video here](https://youtu.be/4voIdhXp2YE)

## Project Introduction
This project is about continuous integration using GitHub actions of python data science project

## Project Structure
```angular2html
project/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
|
├── .github/
│   └── workflows/
│       ├── install.yml
│       ├── format.yml
│       ├── lint.yml
│       └── test.yml
|
├── src/
│   ├── script.py
│   └── lib.py
│
├── tests/
│   ├── test_script.py 
│   └── test_lib.py
│
├── main.ipynb
├── Makefile
├── requirements.txt
├── README.md
```

## Project Description
This project demonstrates how to implement Continuous Integration (CI) for a Python-based data science project using GitHub CI. The project includes functionality for performing descriptive statistics using Pandas, automated testing with the pytest-nbval plugin for Jupyter Notebooks, code formatting, linting, and testing. A Makefile is used to streamline running tasks, while GitHub CI is used to automatically execute these tasks in the pipeline. This ensures high-quality, maintainable code through automated checks and tests.

## Project Setup
For Mini Project 2 with a similar structure but with added functions for the testing and Makefile.
1. Formats Python code using `black`
<p align="center">
  <img src="screenshots/format.png" />
</p>

2. Lints the code using `ruff` to catch any errors or style issues.
<p align="center">
  <img src="screenshots/lint.png" />
</p>

3. Runs both notebook and script tests using `pytest` with `nbval` to ensure correctness.
<p align="center">
  <img src="screenshots/test.png" />
</p>

## Project Output
The markdown summary report is under the `output` dictionary with name `summary_report.md`. You can find them here [Summary Report](./output/summary_report.md).
