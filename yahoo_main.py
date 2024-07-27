#!/bin/python3

import sys
from yahoo_finance_scraper import YahooFinanceScraper

if __name__ == "__main__":
    base_url = "https://finance.yahoo.com/quote/"

    # Combining all arguments into a single string 
    input_tickers = ' '.join(sys.argv[1:])
    ticker_symbols = input_tickers.replace(',', ' ').split()

    # convert ticker to uppercase
    ticker_symbols = [symbol.upper() for symbol in ticker_symbols if symbol]

    if not ticker_symbols:
        ticker_symbols = ["BTC-USD", "MSFT", "SPY"]  # Default ticker symbols

    stock_urls = [f"{base_url}{symbol}?p={symbol}&.tsrc=fin-srch" for symbol in ticker_symbols]

    scraper = YahooFinanceScraper(stock_urls)
    scraper.scrape_stock_data()
    scraper.print_data()
    scraper.save_to_csv()
