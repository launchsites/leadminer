# LeadMiner

![Python](https://img.shields.io/badge/python-3.10+-blue)
![PyPI](https://img.shields.io/pypi/v/leadminer)
![Downloads](https://img.shields.io/pypi/dm/leadminer)
![License](https://img.shields.io/badge/license-MIT-green)
![CLI](https://img.shields.io/badge/interface-CLI-orange)

Find **local business leads directly from your terminal**.

LeadMiner is a fast CLI tool that searches the **Google Places API** for businesses, lets you filter them by useful outreach signals (rating, reviews, website presence), and export results instantly.

Perfect for:

- agencies doing cold outreach
- freelancers finding potential clients
- lead generation workflows
- local market research
- automation scripts

---

# Demo

![LeadMiner Demo](demo.gif)

Example command:

```bash
leadminer search plumber london --website n --output-format csv
```

Find **plumbers without websites in London** and export them to CSV.

---

# Features

### Business Search
Search businesses by **type and location**

```bash
leadminer search plumber london
```

---

### Powerful Filters

Filter results using:

- rating
- review count
- website presence

Examples:

```bash
leadminer search plumber london --website n
```

Find businesses **without websites**

```bash
leadminer search cafe manchester --min-rating 0 --max-rating 3
```

Find **poorly rated businesses**

```bash
leadminer search electrician birmingham --min-reviews 10
```

Find **established businesses**

---

### Export Results

Export results to:

- beautiful CLI tables
- CSV files for outreach workflows

```bash
leadminer search plumber london --output-format csv
```

---

### Campaign System

Store leads inside **campaigns**.

Example workflow:

```bash
leadminer campaign create plumbers
leadminer campaign select plumbers
```

Now every search result will be **saved automatically**.

---

### Local Database

LeadMiner stores all data locally using **SQLite**.

No external storage required.

---

### Clean Terminal Output

Uses the **Rich** library to display leads in structured tables.

Example output:

```
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ Name          ┃ Address           ┃ Phone        ┃ Website  ┃ Rating ┃ Reviews ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━┩
┃ London Plumb  ┃ 10 High St       ┃ 020 1234 5678┃ -        ┃ 3.2    ┃ 12      ┃
┃ Rapid Fix     ┃ 42 Bridge Rd     ┃ 020 9988 1122┃ ✔        ┃ 4.7    ┃ 89      ┃
└───────────────┴───────────────────┴──────────────┴──────────┴────────┴─────────┘
```

---

# Installation

The recommended way to install LeadMiner is **pipx**.

pipx installs CLI tools in isolated environments.

---

## Install pipx

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

Install directly from **PyPI**:

```bash
pipx install leadminer
```

Verify installation:

```bash
leadminer --help
```

---

## Install Development Version

Install the latest GitHub version:

```bash
pipx install git+https://github.com/launchsites/leadminer.git
```

---

# Setup

LeadMiner requires a **Google Places API key**.

Run:

```bash
leadminer setup key
```

Follow the instructions printed in the terminal.

Then set your API key:

```bash
leadminer setup key YOUR_API_KEY
```

Set the maximum number of businesses returned per search:

```bash
leadminer setup limit 100
```

---

# Usage

## Basic Search

```bash
leadminer search plumber london
```

---

## Website Filter

Find businesses **without websites**:

```bash
leadminer search plumber london --website n
```

Find businesses **with websites**:

```bash
leadminer search plumber london --website y
```

---

## Rating Filter

```bash
leadminer search cafe manchester --min-rating 0 --max-rating 3
```

---

## Review Count Filter

```bash
leadminer search electrician birmingham --min-reviews 20
```

---

## Export CSV

```bash
leadminer search plumber london --output-format csv
```

CSV files are saved to:

```
~/.leadminer/exports/
```

---

# Campaigns

Campaigns allow you to **store and organise leads**.

---

## Create Campaign

```bash
leadminer campaign create plumbers
```

---

## Select Campaign

```bash
leadminer campaign select plumbers
```

Search results will now be stored automatically.

---

## List Campaigns

```bash
leadminer campaign list
```

---

## View Campaign Data

```bash
leadminer campaign list plumbers
```

---

## Stop Storing Leads

```bash
leadminer campaign disconnect
```

---

## Remove Campaign

```bash
leadminer campaign remove plumbers
```

---

# Example Workflow

Find restaurants without websites and export leads.

```bash
leadminer search restaurant london --website n --output-format csv
```

Create campaign:

```bash
leadminer campaign create london-restaurants
```

Store leads automatically:

```bash
leadminer campaign select london-restaurants
```

Continue running searches and building your lead list.

---

# Data Storage

LeadMiner stores all data locally.

Base directory:

```
~/.leadminer/
```

Database:

```
~/.leadminer/leadminer.db
```

CSV exports:

```
~/.leadminer/exports/
```

---

# Commands

Search businesses

```
leadminer search
```

Campaign management

```
leadminer campaign
```

Setup API key and limits

```
leadminer setup
```

CLI help

```
leadminer help
```

---

# Tech Stack

LeadMiner is built with:

- Python
- Typer (CLI framework)
- Rich (terminal formatting)
- SQLite
- Requests
- Google Places API

---

# Roadmap

Planned improvements:

- pagination support
- multi-location search
- JSON export
- email extraction from websites
- async searching
- bulk search workflows
- outreach automation

---

# Contributing

Contributions are welcome.

Ideas for improvements:

- faster searching
- new filters
- outreach features
- better exports

Open an issue or submit a pull request.

---

# License

MIT License
