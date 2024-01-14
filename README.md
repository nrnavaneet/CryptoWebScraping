# CryptoWebScraping

## Overview

This Python script allows you to scrape cryptocurrency data from [Crypto.com](https://crypto.com) using the BeautifulSoup library. It extracts information such as cryptocurrency names, rankings, market cap, and 24H price changes from the website and stores it in an Excel file

## Features

- Scrapes cryptocurrency names from all pages of the [crypto.com/price](https://crypto.com/price) website.
- Demonstrates basic web scraping techniques using Python and BeautifulSoup.

## Prerequisites

- Python 3.x
- Required Python packages: requests, BeautifulSoup,openpyxl

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nrnavaneet/CryptoWebScraping.git
   cd CryptoWebScraping
   ```
2. Install the required Python packages:
  
  FOR WINDOWS
  ```bash
  pip install bs4
  pip install requests
  pip install openpyxl
  ```
  FOR MAC
  ```bash
  pip3 install bs4
  pip3 install requests
  pip3 install openpyxl
  ```
2. Run the script:

    ```bash
    python crypto_scraper.py
    ```

3. The default number of page numbers to scrape is 3. You  can change the page number in line 56.

4. Check the Excel(2706) for the details of cryptocurrencies.

## Configuration

- The script assumes that the cryptocurrency names are located within specific HTML elements. Modify the script if the website structure changes.

## Contributing

If you find a bug, have suggestions for improvements, or would like to add new features, feel free to open an issue or create a pull request.

## Author
   nrnavaneet

