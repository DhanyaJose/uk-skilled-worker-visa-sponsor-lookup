# UK Skilled Worker Visa Sponsor Lookup

A local web app to check if a UK company is a licensed visa sponsor. Search 140,000+ organisations from the official Home Office register.

## Prerequisites

- Python 3.7+
- pip

## Setup

1. **Clone or download this folder**, then navigate into it:

   ```bash
   cd uk_skilled_worker_visa_sponsorship
   ```

2. **Download the CSV** from the [Register of Licensed Sponsors](https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers) and rename it to `sponsors.csv`:

   ```bash
   mv "2026-04-01_-_Worker_and_Temporary_Worker.csv" sponsors.csv
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**

   ```bash
   python app.py
   ```

5. **Open your browser** and go to:

   ```
   http://127.0.0.1:5000
   ```

## Usage

Type a company name into the search box. Results appear live after 3 or more characters. The search is case-insensitive and matches any part of the company name.

## Data Source

The CSV comes from the UK Government's [Register of Licensed Sponsors](https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers).

**Current data downloaded:** 1 April 2026

To update, download a new CSV from the link above and rename it to `sponsors.csv`, replacing the existing file.
