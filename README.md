# yahooFinanceScraper
This Python web scraper extracts stock and financial statement data from Yahoo Finance. It utilizes the BeautifulSoup library for HTML parsing and requests for making HTTP requests. The script is modular, organized into classes, allowing easy extension and customization. Data is printed to the console and saved to a CSV file for further analysis.

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
- Install dependencies (requests and beautifulsoup4).
- Run the main script, providing the Yahoo Finance URL as a command-line argument.
