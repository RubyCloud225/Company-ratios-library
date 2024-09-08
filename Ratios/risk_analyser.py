import pandas as pd
import numpy as np
from PLC.data_processing import StockPriceImporter

class BetaCalculator:
    def __init__(self, ticker, start_date, end_date, market_indices=['^GSPC', '^DJI', '^IXIC']):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.market_indices = market_indices
        self.selected_market_index = None
        self.stock_data = None
        self.market_data = None
        self.beta = None
    
    def select_market_index(self, index):
        if index in self.market_indices:
            self.selected_market_index = index
        else:
            print("Invalid market index. Please select from the following options:")
            print(self.market_indices)
    
    def import_stock_data(self):
        """
        Import the stock price data using the StockPriceImporter class.
        """
        importer = StockPriceImporter(self.ticker, self.start_date, self.end_date)
        self.stock_data = importer.import_stock_prices()

    def import_market_data(self):
        """
        Import the market index price data using the StockPriceImporter class.
        """
        if self.stock_data is None:
            print("Stock data is not imported. Please call import_stock_data method first.")
            return
        importer = StockPriceImporter(self.selected_market_index, self.start_date, self.end_date)
        market_data = importer.import_stock_prices()

        if market_data is None:
            print("Failed to import market data.")
            return

        common_dates = np.intersect1d(self.stock_data.index, market_data.index)
        self.stock_data = self.stock_data.loc[common_dates]
        self.market_data = market_data.loc[common_dates]

    def calculate_beta(self):
        """
        Calculate the beta of the stock.

        Returns:
        - float: The beta of the stock.
        """
        if self.stock_data is None or self.market_data is None:
            print("Please import the stock and market data first.")
            return None

        # Calculate the daily returns of the stock and market index
        common_dates = np.intersect1d(self.stock_data.index, self.market_data.index)
        stock_returns = self.stock_data.loc[common_dates, 'Close'].pct_change().dropna().values[:, np.newaxis]
        market_returns = self.market_data.loc[common_dates, 'Close'].pct_change().dropna().values[:, np.newaxis]

        # Calculate the covariance and variance
        covariance = np.cov(stock_returns.squeeze(), market_returns.squeeze())[0, 1]
        variance = np.var(market_returns)

        # Calculate the beta
        self.beta = covariance / variance
        return self.beta

    def get_beta(self):
        """
        Get the calculated beta.

        Returns:
        - float: The beta of the stock.
        """
        return self.beta.values[0][0]