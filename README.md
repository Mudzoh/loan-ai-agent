# Loan Amortization AI Agent

A simple Streamlit app that calculates loan monthly payments and shows the full amortization schedule with CSV export.

## Setup

1. Open a terminal in this project directory:
   - `cd c:\Users\aaa\Desktop\loan-ai-agent`
2. (Optional) Create and activate a venv:
   - `python -m venv venv`
   - `venv\Scripts\activate`
3. Install dependencies:
   - `pip install -r requirements.txt`

## Run locally

```powershell
streamlit run app.py
```

Then open the URL shown in the terminal (typically `http://localhost:8501`).

## Features

- Input: loan amount, annual interest rate, term years
- Output: monthly payment, total payment, total interest
- Amortization schedule table (first and last 12 rows)
- Download full schedule as CSV

## GitHub remote setup

```powershell
git remote add origin https://github.com/YOUR_USER/loan-ai-agent.git
git branch -M main
git push -u origin main
```

## Deploy to Streamlit Community Cloud

1. Go to `https://share.streamlit.io`
2. Login with GitHub
3. Click **New app** → `YOUR_USER/loan-ai-agent` → branch `main` → file `app.py`
4. Deploy

## Optional GitHub Actions CI

Create `.github/workflows/python-app.yml`:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.14'
      - run: python -m pip install --upgrade pip
      - run: pip install -r requirements.txt
      - run: python -m py_compile app.py
```

## Notes

- You can also run locally with `python -m streamlit run app.py` if `streamlit` command is unavailable in PATH.
- Keep `requirements.txt` in sync with new dependencies.
