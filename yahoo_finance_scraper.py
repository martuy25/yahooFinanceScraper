#!bin/pyhton3

import requests
import sys
from bs4 import BeautifulSoup
import csv

class YahooFinanceScrapper:
	def __init__(self, url):
		self.url = url
		self.stock_info = {}
		self.financial_data = {}
		
	def scrape_stock_data(self):
		response = requests.get(self.url) #sends a GET request to specified URL
		if response.status_code == 200: #checks to see if the requests was succesful
			soup = BeautifulSoup(response.text, 'html.parser') # parse the HTML content of the page
			self.stock_info['Symbol'] = soup.find('h1').text.strip() #assuming the stock symbol is an H1 tag, modify as necessary
			tables = soup.find_all('table')
			for table in tables:
				rows = table.find_all('tr')
				for row in rows:
					columns = row.find_all(['th', 'td'])
					if len(columns) ==2:
						self.financial_data[columns[0].text.strip()] = columns[1].text.strip()
		else:
			print(f"Failed to retrieve the page. Status code {response.status_code}")
	def print_data(self): #function to print the extracted data
		print("Stock Information: ", self.stock_info)
		print("\n")
		print("Financial Statement Data: ", self.financial_data)
		
	def save_to_csv(self):
		with open('stock_data.csv', 'w' , newline= '') as csvfile:
			fieldnames = ['Attribute', 'Value']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			
			writer.writeheader()
			for key, value in self.stock_info.items():
				writer.writerow({'Attribute': key, 'Value': value})
			for key, value in self.financial_data.items():
				writer.writerow({'Attribute': key, 'Value': value})
		
			
