# Python Script that Generates a CSV File with Random Data

This repository contains a Python script that generates random sales data and saves it to a CSV file. The data is generated on a daily basis via a GitHub Actions workflow, and the resulting CSV file is committed and pushed back to the repository.

## Features

- Generates random sales data with various attributes (e.g., product names, quantities, prices).
- The sales data is saved to a CSV file.
- The data generation process is automated using GitHub Actions.
- The CSV file is uploaded as an artifact and committed to the repository.

## Prerequisites

Make sure you have the following installed:

- **Python 3.x**: The script is written in Python and requires version 3.x.
- **Git**: To commit and push the generated data back to the repository.

## How It Works

The process is automated via GitHub Actions and can be triggered in two ways:

1. **Scheduled Run**: The workflow runs daily at midnight and generates new sales data.
2. **Manual Trigger**: The workflow can also be triggered manually via the GitHub Actions UI.

The generated CSV file is then committed and pushed to the `master` branch, and it can also be downloaded as an artifact.

## Workflow Details

The workflow is configured to run automatically under the following conditions:

- **Scheduled Run**: Runs daily at midnight.
- **Push to `master`**: Runs when changes are pushed to the `master` branch.
- **Manual Trigger**: Can be manually triggered through the GitHub Actions UI.

### Workflow Steps

1. **Checkout repository**: The workflow checks out the repository to access the script and other files.
2. **Set up Python**: Python 3.x is installed and configured.
3. **Install dependencies**: Dependencies from `requirements.txt` are installed.
4. **Run the data generation script**: The Python script `generate_sales.py` generates new sales data.
5. **Commit and push data**: The generated CSV file is committed to the repository and pushed back to the `master` branch.
6. **Upload as artifact**: The CSV file is also uploaded as an artifact for easy download.

## Usage

### Running Locally

To run the script locally, clone the repository and run the following commands:

```bash
git clone https://github.com/OkiriGabriel/Python-script-that-generates-a-CSV-file-with-random-data-workflow.git
cd Python-script-that-generates-a-CSV-file-with-random-data-workflow
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
python generate_sales.py
