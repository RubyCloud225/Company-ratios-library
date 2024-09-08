import numpy as np
from DCF import DCFModel

def main():
    # Create a DCFModel instance
    dcf_model_instance = DCFModel.DCFModel(ebitda=100, growth_rate=0.05, decay_rate=0.02, cost_of_debt=0.04, cost_of_equity=0.08, debt_to_equity_ratio=0.5, terminal_growth_rate=0.03, working_capital_turnover=2, capital_expenditure_rate=0.1)

    # Run the DCF model to get the enterprise value
    enterprise_value = dcf_model_instance.run_model()

    # Create a ShareValueCalculator instance
    share_value_calculator = ShareValueCalculator(enterprise_value, total_debt=500, total_cash=200, total_shares_outstanding=1000000)

    # Calculate the market value per share
    market_value_per_share = share_value_calculator.calculate_market_value_per_share()

    print("Market value per share:", market_value_per_share)

if __name__ == "__main__":
    main()

class ShareValueCalculator:
    def __init__(self, enterprise_value, total_debt, total_cash, total_shares_outstanding):
        """
        Initialize the ShareValueCalculator.

        :param enterprise_value: Enterprise value obtained from the DCFModel.
        :param total_debt: Total debt of the company.
        :param total_cash: Total cash and cash equivalents of the company.
        :param total_shares_outstanding: Total shares outstanding of the company.
        """
        self.enterprise_value = enterprise_value
        self.total_debt = total_debt
        self.total_cash = total_cash
        self.total_shares_outstanding = total_shares_outstanding

    def calculate_equity_value(self):
        """
        Calculate the equity value.

        :return: Equity value.
        """
        equity_value = self.enterprise_value + self.total_cash - self.total_debt
        return equity_value

    def calculate_market_value_per_share(self):
        """
        Calculate the market value per share.

        :return: Market value per share.
        """
        equity_value = self.calculate_equity_value()
        market_value_per_share = equity_value / self.total_shares_outstanding
        return market_value_per_share
    
"""
#Example useage

# Create a DCFModel instance
dcf_model = DCFModel(ebitda=100, growth_rate=0.05, decay_rate=0.02, cost_of_debt=0.04, cost_of_equity=0.08, debt_to_equity_ratio=0.5, terminal_growth_rate=0.03, working_capital_turnover=2, capital_expenditure_rate=0.1)

# Run the DCF model to get the enterprise value
enterprise_value = dcf_model.run_model()

# Create a ShareValueCalculator instance
share_value_calculator = ShareValueCalculator(enterprise_value, total_debt=500, total_cash=200, total_shares_outstanding=1000000)

# Calculate the market value per share
market_value_per_share = share_value_calculator.calculate_market_value_per_share()

print("Market value per share:", market_value_per_share)

"""
