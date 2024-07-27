# yahooFinanceScraper
This Python script scrapes detailed stock and financial data from Yahoo Finance using BeautifulSoup and requests. It handles multiple ticker symbols via command-line input, formats output into readable tables, and saves data to a CSV file. Perfect for data analysis and finance projects.

# Updates
- Enhahnced Flexibility: Script now accepts multiple stock ticker symbols directly from the command line, seperated by commas, spaces or both
- Case Insensitivity: Accepts input tickers in upper or lowercase
- Improved Data Display: Using the "tabulate" library to display information clearly

# Features:

- Scrapes stock information and financial statement data from Yahoo Finance.
- Organized code structure with classes for modularity.
- Saves extracted data to a CSV file for easy analysis.

# Usage:
- Clone the repository.
- Install dependencies (requests and beautifulsoup4, tabulate).
- Run the main script, providing the Yahoo Finance URL as a command-line argument.

# Sample Output
# Financial Data Scraper Output

## Data for DIS

### Stock Information

| Field   | Value |
|---------|-------|
| Symbol  | DIS   |

### Financial Statement Data

| Field                | Value        |
|----------------------|--------------|
| Previous Close       | 89.21        |
| Open                 | 90.00        |
| Bid                  | 89.90 x 1200 |
| Ask                  | 89.82 x 1000 |
| Day's Range          | 89.33 - 90.54|
| 52 Week Range        | 78.73 - 123.74 |
| Volume               | 8,640,588    |
| Avg. Volume          | 10,728,175   |
| Market Cap (intraday)| 163.946B     |
| Beta (5Y Monthly)    | 1.40         |
| PE Ratio (TTM)       | 97.75        |
| EPS (TTM)            | 0.92         |
| Earnings Date        | Aug 7, 2024  |
| Forward Dividend & Yield | 0.90 (1.00%) |
| Ex-Dividend Date     | Jul 8, 2024  |
| 1y Target Est        | 123.49       |
