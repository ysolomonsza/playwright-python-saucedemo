# playwright-python-saucedemo
Automated UI tests for SauceDemo using Playwright and Python
playwright-python-saucedemo/
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── test_login.py
├── conftest.py
├── requirements.txt
├── README.md

# Playwright + Python: SauceDemo Automation

This project demonstrates UI test automation for [SauceDemo](https://www.saucedemo.com/) using **Playwright** and **Python**.

## 🚀 Features

- Login test (positive and negative scenarios)
- Page Object Model structure
- Pytest integration
- Easy-to-run scripts

## 🛠️ Tech Stack

- Python 3.10+
- Playwright
- Pytest

## 📦 Installation

```bash
git clone git@github.com:ysolomonsza/playwright-python-saucedemo.git
cd playwright-python-saucedemo
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install
