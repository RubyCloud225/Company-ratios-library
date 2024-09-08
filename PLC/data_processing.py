import yfinance as yf
import pandas as pd

class StockPriceImporter:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
    
    def import_stock_prices(self):
        """
        Returns PD.Dataframe containing stock price data
        """
        try:
            self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            self.data.reset_index(inplace=True)
            self.data['Date'] = pd.to_datetime(self.data['Date']).dt.date
            
            # Define the column types
            column_types = {
                'Open': float,
                'High': float,
                'Low': float,
                'Close': float,
                'Adj Close': float,
                'Volume': int
            }
            
            # Convert each column to the specified type
            for column, column_type in column_types.items():
                self.data[column] = self.data[column].astype(column_type)
            
            return self.data
        
        except Exception as e:
            print(f"Failed to import stock price data: {e}")
            return None

    def get_stock_prices(self):
        """
        Get the imported stock price data.

        Returns:
        - pd.DataFrame: A DataFrame containing the stock price data.
        """
        return self.data

class BalanceSheetDownloader:
    def __init__(self, ticker):
        self.ticker = ticker

    def download_balance_sheet(self):
        try:
            stock = yf.Ticker(self.ticker)
            balance_sheet = stock.balance_sheet
            return balance_sheet
        except Exception as e:
            print(f"Error downloading balance sheet for {self.ticker}: {e}")
            return None

    def print_balance_sheet(self):
        balance_sheet = self.download_balance_sheet()
        if balance_sheet is not None:
            print(balance_sheet)