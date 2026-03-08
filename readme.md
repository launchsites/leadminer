# LeadMiner

![Python](https://img.shields.io/badge/python-3.10+-blue)
![PyPI](https://img.shields.io/pypi/v/leadminer)
![License](https://img.shields.io/badge/license-MIT-green)
![CLI](https://img.shields.io/badge/interface-CLI-orange)

A fast **CLI tool for finding local business leads** using the Google Places API.

Search for businesses in any location, filter them by rating, reviews, or website presence, and export results to a clean terminal table or CSV file.

Perfect for:

- lead generation
- local outreach
- agency prospecting
- scraping potential clients quickly

---

## Demo

![LeadMiner Demo](demo.gif)

---

# Features

- Search businesses by **type and location**
- Filter by:
  - rating
  - review count
  - website presence
- Export results to:
  - CLI table
  - CSV file
- Store results in **campaigns**
- Simple **CLI workflow**
- Local SQLite database
- Clean terminal output using **Rich**

---

# Installation

The easiest way to install LeadMiner is with **pipx**.

## Install pipx (recommended)

Mac:

```bash
brew install pipx
pipx ensurepath
```

Linux:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Windows:

```bash
pip install pipx
pipx ensurepath
```

---

## Install LeadMiner

Install from **PyPI**:

```bash
pipx install leadminer
```

Then run:

```bash
leadminer --help
```

---

## Install from GitHub (development version)

If you want the latest development version instead:

```bash
pipx install git+https://github.com/launchsites/leadminer.git
```

---

# Setup

LeadMiner requires a **Google Places API key**.

To learn how to obtain one, run:

```bash
leadminer setup key
```

Then set your key:

```bash
leadminer setup key YOUR_API_KEY
```

Set how many businesses you want returned per search:

```bash
leadminer setup limit 100
```

---

# Usage

Basic search:

```bash
leadminer search plumber london
```

---

## Filters

Filter results by website presence:

```bash
leadminer search plumber london --website n
```

Only show businesses **without websites**.

---

Filter by rating:

```bash
leadminer search cafe manchester --min-rating 0 --max-rating 3
```

---

Filter by review count:

```bash
leadminer search electrician birmingham --min-reviews 10
```

---

## Export to CSV

```bash
leadminer search plumber london --output-format csv
```

CSV files are saved to:

```text
~/.leadminer/exports/
```

---

# Campaigns

Campaigns let you **store leads from searches** for later use.

Create a campaign:

```bash
leadminer campaign create plumbers
```

Select a campaign:

```bash
leadminer campaign select plumbers
```

Now all search results will automatically be saved.

---

List campaigns:

```bash
leadminer campaign list
```

View leads in a campaign:

```bash
leadminer campaign list plumbers
```

---

Stop saving searches:

```bash
leadminer campaign disconnect
```

---

Delete a campaign:

```bash
leadminer campaign remove plumbers
```

---

# Example Workflow

Find restaurants without websites:

```bash
leadminer search restaurant london --website n --output-format csv
```

Create a campaign:

```bash
leadminer campaign create london-restaurants
```

Store leads automatically:

```bash
leadminer campaign select london-restaurants
```

Run searches and build your lead list.

---

# Data Storage

LeadMiner stores data locally:

```text
~/.leadminer/
```

Database:

```text
~/.leadminer/leadminer.db
```

Exports:

```text
~/.leadminer/exports/
```

---

# Commands

Search businesses:

```text
leadminer search
```

Campaign management:

```text
leadminer campaign
```

Setup API key and limit:

```text
leadminer setup
```

Help:

```text
leadminer help
```

---

# Tech Stack

- Python
- Typer (CLI framework)
- Rich (terminal output)
- SQLite
- Google Places API
- Requests

---

# Contributing

Pull requests are welcome.

If you find bugs or have ideas for improvements, open an issue.

---

# License

MIT License