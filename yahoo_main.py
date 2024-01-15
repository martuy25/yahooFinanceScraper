#!/bin/python3

import sys
from yahoo_finance_scraper import YahooFinanceScrapper

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Program takes two arguments, please try again")
	else:
		url = sys.argv[1] #gets the url from cmd Line
		scraper = YahooFinanceScrapper(url)
		scraper.scrape_stock_data()
		scraper.print_data()
		scraper.save_to_csv()
