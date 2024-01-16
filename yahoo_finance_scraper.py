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
			self.stock_info['Symbol'] = soup.find('h1').text.strip() #assuming the stock symbol is an H1 tag, can be modified if necessary, you would change this to 'h2' or 'h3' if that was how the website was organized
			tables = soup.find_all('table')
			for table in tables:
				rows = table.find_all('tr')
				for row in rows:
					columns = row.find_all(['th', 'td'])
					if len(columns) ==2: # if true, adds the data to 'self.finacial_data' dictionary
						self.financial_data[columns[0].text.strip()] = columns[1].text.strip() #this a check to ensure only rows w/ 2 columns are processed
		else:
			print(f"Failed to retrieve the page. Status code {response.status_code}")
	def print_data(self): #function to print the extracted data
		print("Stock Information: ", self.stock_info)
		print("\n")
		print("Financial Statement Data: ", self.financial_data)
		
	def save_to_csv(self):
		with open('stock_data.csv', 'w' , newline= '') as csvfile: #opens a CSV file in write mode, "newline=''" is used to ensure newline characters handled properly in csv file
			fieldnames = ['Attribute', 'Value'] #defiing the column headers
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #creates a CSV writer for 'stock_data.csv' and makes the file have columns 'Attribute' and 'Value"
			
			writer.writeheader() #writes the header row
			for key, value in self.stock_info.items(): # writes the stock info into the CSV
				writer.writerow({'Attribute': key, 'Value': value})
			for key, value in self.financial_data.items(): #writes the financial data to the CSV
				writer.writerow({'Attribute': key, 'Value': value})
		
			
