import requests
from bs4 import BeautifulSoup
import csv
from tabulate import tabulate

class YahooFinanceScraper:
    def __init__(self, urls):
        self.urls = urls
        self.data = {}

    def scrape_stock_data(self):
        for url in self.urls:
            ticker_symbol = url.split("/quote/")[1].split("?")[0]
            self.data[ticker_symbol] = {"stock_info": {}, "financial_data": {}}
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Directly search desired the ticker symbols
                self.data[ticker_symbol]["stock_info"]['Symbol'] = ticker_symbol

                # Extract financial data
                statistics_section = soup.find('div', {'data-testid': 'quote-statistics'})
                if statistics_section:
                    items = statistics_section.find_all('li')
                    for item in items:
                        label = item.find('span', {'class': 'label'}).text.strip()
                        value_span = item.find('span', {'class': 'value'})
                        value = value_span.find('fin-streamer').text.strip() if value_span.find('fin-streamer') else value_span.text.strip()
                        self.data[ticker_symbol]["financial_data"][label] = value
                else:
                    print(f"Failed to find the financial data section in {url}")

            else:
                print(f"Failed to grab the page. Status code {response.status_code}")

    def print_data(self):
        for ticker_symbol, data in self.data.items():
            print(f"Data for {ticker_symbol}:")
            stock_info_table = [[key, value] for key, value in data["stock_info"].items()]
            financial_data_table = [[key, value] for key, value in data["financial_data"].items()]
            print("Stock Information:\n", tabulate(stock_info_table, headers=["Field", "Value"], tablefmt="grid"))
            print("Financial Statement Data:\n", tabulate(financial_data_table, headers=["Field", "Value"], tablefmt="grid"))
            print("\n")

    def save_to_csv(self, filename='financial_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Ticker", "Field", "Value"])
            for ticker_symbol, data in self.data.items():
                for key, value in data["financial_data"].items():
                    writer.writerow([ticker_symbol, key, value])
