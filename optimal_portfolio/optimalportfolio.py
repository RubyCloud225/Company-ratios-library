import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize
from cvxpy import *

class OptimalPortfolio:
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.download_data()
        self.expected_returns = self.calculate_expected_returns()
        self.covariance_matrix = self.calculate_covariance_matrix()

    def download_data(self):
        data = yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close']
        return data

    def calculate_expected_returns(self):
        returns = self.data.pct_change()
        expected_returns = returns.mean() * 252
        return expected_returns

    def calculate_covariance_matrix(self):
        returns = self.data.pct_change()
        covariance_matrix = returns.cov() * 252
        return covariance_matrix

    def optimize_portfolio(self, target_return):
        n_assets = len(self.tickers)
        weights = Variable(n_assets)

        constraints = [
            sum(weights) == 1,  # sum of weights equal to 1
            weights >= 0  # no short positions
        ]

        portfolio_return = self.expected_returns.T @ weights
        portfolio_risk = quad_form(weights, self.covariance_matrix)

        objective = Minimize(portfolio_risk)
        problem = Problem(objective, constraints)
        problem.solve()

        optimal_weights = weights.value
        portfolio_return = np.dot(self.expected_returns, optimal_weights)

        if portfolio_return >= target_return:
            print("The portfolio return meets the target return of {:.2f}%.".format(target_return*100))
        else:
            print("The portfolio return does not meet the target return of {:.2f}%.".format(target_return*100))

        return optimal_weights

    def print_optimal_portfolio(self, optimal_weights):
        print("Optimal Weights:")
        for i, ticker in enumerate(self.tickers):
            print("{}: {:.2f}%".format(ticker, optimal_weights[i]*100))
"""
# Example usage
tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
start_date = '2010-01-01'
end_date = '2022-02-26'

portfolio = OptimalPortfolio(tickers, start_date, end_date)
optimal_weights = portfolio.optimize_portfolio(0.10)
portfolio.print_optimal_portfolio(optimal_weights)
"""