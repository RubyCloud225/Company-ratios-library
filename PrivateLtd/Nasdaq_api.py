import requests
import pandas as pd

class NasdaqAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_industries(self):
        url = f"https://data.nasdaq.com/api/v3/industries?api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        industries = {}
        for industry in data['industries']:
            industries[industry['name']] = industry['tickers']
        return industries
    
    def get_company_info(self, ticker):
        url = f"https://data.nasdaq.com/api/v3/company/{ticker}?api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def get_balance_sheet(self, ticker):
        url = f"https://data.nasdaq.com/api/v3/balance-sheet/{ticker}?api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def get_share_price(self, ticker):
        url = f"https://data.nasdaq.com/api/v3/share-price/{ticker}?api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def get_dividend_payments(self, ticker):
        url = f"https://data.nasdaq.com/api/v3/dividend-payments/{ticker}?api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_historical_data(self, ticker, start_date, end_date):
        url = f"https://data.nasdaq.com/api/v3/historical-data/{ticker}?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_eod_historical_stock_market_data(self, ticker, period, start_date, end_date):
        url = f"https://data.nasdaq.com/api/v3/eod-historical-stock-market-data/{ticker}?period={period}&start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_fundamentals_data(self, ticker):
        url = f"https://data.nasdaq.com/api/v3/fundamentals-data/{ticker}?api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_historical_dividends_data(self, ticker, start_date, end_date):
        url = f"https://data.nasdaq.com/api/v3/historical-dividends-data/{ticker}?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_upcoming_earnings_data(self, ticker, start_date, end_date):
        url = f"https://data.nasdaq.com/api/v3/upcoming-earnings-data/{ticker}?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_upcoming_splits_data(self, ticker, start_date, end_date):
        url = f"https://data.nasdaq.com/api/v3/upcoming-splits-data/{ticker}?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_upcoming_IPOs_data(self, start_date, end_date):
        url = f"https://data.nasdaq.com/api/v3/upcoming-IPOs-data?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_economic_events_data(self, start_date, end_date, country, comparison):
        url = f"https://data.nasdaq.com/api/v3/economic-events-data?start_date={start_date}&end_date={end_date}&country={country}&comparison={comparison}&api_key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data

    def get_financial_news(self, start_date, end_date, t, offset, limit):
        url = f"https://data.nasdaq.com/api/v3/financial-news?start_date={start_date}&end_date={end_date}&t={t}&offset={offset}&limit={limit}&api_key={self.api_key}"
        response = requests.get(url)
    
"""
#Example usage
# Create an instance of the NasdaqAPI class with your API key
nasdaq_api = NasdaqAPI("YOUR_API_KEY")

# Get a dictionary of industries
industries = nasdaq_api.get_industries()
print("Industries:")
print(industries)

# Get company info for Apple (AAPL)
company_info = nasdaq_api.get_company_info("AAPL")
print("\nCompany Info (AAPL):")
print(company_info)

# Get balance sheet for Apple (AAPL)
balance_sheet = nasdaq_api.get_balance_sheet("AAPL")
print("\nBalance Sheet (AAPL):")
print(balance_sheet)

# Get share price for Apple (AAPL)
share_price = nasdaq_api.get_share_price("AAPL")
print("\nShare Price (AAPL):")
print(share_price)

# Get dividend payments for Apple (AAPL)
dividend_payments = nasdaq_api.get_dividend_payments("AAPL")
print("\nDividend Payments (AAPL):")
print(dividend_payments)

# Get historical data for Apple (AAPL) from 2020-01-01 to 2020-12-31
historical_data = nasdaq_api.get_historical_data("AAPL", "2020-01-01", "2020-12-31")
print("\nHistorical Data (AAPL) from 2020-01-01 to 2020-12-31:")
print(historical_data)

# Get EOD historical stock market data for Apple (AAPL) from 2020-01-01 to 2020-12-31
eod_historical_data = nasdaq_api.get_eod_historical_stock_market_data("AAPL", "daily", "2020-01-01", "2020-12-31")
print("\nEOD Historical Stock Market Data (AAPL) from 2020-01-01 to 2020-12-31:")
print(eod_historical_data)

# Get fundamentals data for Apple (AAPL)
fundamentals_data = nasdaq_api.get_fundamentals_data("AAPL")
print("\nFundamentals Data (AAPL):")
print(fundamentals_data)

# Get historical dividends data for Apple (AAPL) from 2020-01-01 to 2020-12-31
historical_dividends_data = nasdaq_api.get_historical_dividends_data("AAPL", "2020-01-01", "2020-12-31")
print("\nHistorical Dividends Data (AAPL) from 2020-01-01 to 2020-12-31:")
print(historical_dividends_data)

# Get upcoming earnings data for Apple (AAPL) from 2020-01-01 to 2020-12-31
upcoming_earnings_data = nasdaq_api.get_upcoming_earnings_data("AAPL", "2020-01-01", "2020-12-31")
print("\nUpcoming Earnings Data (AAPL) from 2020-01-01 to 2020-12-31:")
print(upcoming_earnings_data)

# Get upcoming splits data for Apple (AAPL) from 2020-01-01 to 2020-12-31
upcoming_splits_data = nasdaq_api.get_upcoming_splits_data("AAPL", "2020-01-01", "2020-12-31")
print("\nUpcoming Splits Data (AAPL) from 2020-01-01 to 2020-12-31:")
print(upcoming_splits_data)

# Get upcoming IPOs data from 2020-01-01 to 2020-12-31
upcoming_ipos_data = nasdaq_api.get_upcoming_IPOs_data("2020-01-01", "2020-12-31")
print("\nUpcoming IPOs Data from 2020-01-01 to 2020-12-31:")
print(upcoming_ipos_data)

# Get economic events data from 2020-01-01 to 2020-12-31 for the United States
economic_events_data = nasdaq_api.get_economic_events_data("2020-01-01", "2020-12-31", "United States", "GDP")
print("\nEconomic Events Data from 2020-01-01 to 2020-12-31 for the United States:")
print(economic_events_data)

# Get financial news from 2020-01-01 to 2020-12-31 for the term "Apple"
financial_news = nasdaq_api.get_financial_news("2020-01-01", "2020-12-31", "Apple", 0, 10)
print("\nFinancial News from 2020-
"""