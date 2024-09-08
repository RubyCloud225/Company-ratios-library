import pandas as pd
import requests
from bs4 import BeautifulSoup

class EBITDACalculator:
    def __init__(self, csv_file, ticker_symbol):
        """
        Initialize the EBITDA calculator with a CSV file and a ticker symbol.

        :param csv_file: Path to the CSV file containing financial data.
        :param ticker_symbol: Ticker symbol of the company (e.g. "AAPL" for Apple Inc.).
        """
        self.csv_file = csv_file
        self.ticker_symbol = ticker_symbol
        self.data = pd.read_csv(csv_file)
        self.web_data = self.scrape_web_data()

    def scrape_web_data(self):
        """
        Scrape additional financial data from a website (e.g. Yahoo Finance).

        :return: Dictionary containing scraped data.
        """
        url = f"https://finance.yahoo.com/quote/{self.ticker_symbol}/financials"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        # Extract relevant data from the tables
        data = {}
        for table in tables:
            if table.find('th', text='Operating Expenses'):
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) > 1:
                        key = cols[0].text.strip()
                        value = cols[1].text.strip()
                        data[key] = value

        return data
    
    def calculate_ebitda(self):
        """
        Calculate EBITDA from the CSV data and web-scraped data.

        :return: EBITDA value.
        """
        # Extract relevant columns from the CSV data
        revenue = self.data['Revenue']
        cost_of_goods_sold = self.data['Cost of Goods Sold']

        # Extract relevant data from the web-scraped data
        operating_expenses = float(self.web_data['Operating Expenses'].replace(',', ''))
        depreciation_and_amortization = float(self.web_data['Depreciation & Amortization'].replace(',', ''))
        interest_expense = float(self.web_data['Interest Expense'].replace(',', ''))
        taxes = float(self.web_data['Provision for Income Taxes'].replace(',', ''))

        # Calculate EBITDA
        ebitda = revenue - cost_of_goods_sold - operating_expenses + depreciation_and_amortization + interest_expense + taxes

        return ebitda

    def get_ebitda_margin(self):
        """
        Calculate EBITDA margin from the CSV data and web-scraped data.

        :return: EBITDA margin value.
        """
        ebitda = self.calculate_ebitda()
        revenue = self.data['Revenue']
        ebitda_margin = (ebitda / revenue) * 100
        return ebitda_margin


# Example usage 
"""
calculator = EBITDACalculator('financial_data.csv', 'AAPL')
ebitda = calculator.calculate_ebitda()
print(f"EBITDA: ${ebitda:.2f}")
ebitda_margin = calculator.get_ebitda_margin()
print(f"EBITDA Margin: {ebitda_margin:.2f}%")
"""