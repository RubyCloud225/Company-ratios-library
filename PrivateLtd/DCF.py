import numpy as np
import matplotlib.pyplot as plt


class DCFModel:
    def __init__(self, ebitda, growth_rate, decay_rate, cost_of_debt, cost_of_equity, debt_to_equity_ratio, terminal_growth_rate, working_capital_turnover, capital_expenditure_rate):
        """
        Initalize the DCF model.

        :param ebidta: EBITDA Value
        :param growth_rate: Annual growth rate for the first 5 years.
        :param decay_rate: Annual decay rate for the growth rate.
        :param cost_of_debt: Cost of debt
        :param cost_of_equity: Cost of equity
        :param debt_to_equity_ratio: Debt to equity ratio
        :param terminal_growth_rate: Terminal growth rate for years 6 and beyond
        :param working_capital_turnover: Working capital turnover ratio
        :param capital_expenditure_rate: Capital expenditure rate as a percentage of Revenue
        """

        self.ebitda = ebitda
        self.growth_rate = growth_rate
        self.decay_rate = decay_rate
        self.cost_of_debt = cost_of_debt
        self.cost_of_equity = cost_of_equity
        self.debt_to_equity_ratio = debt_to_equity_ratio
        self.terminal_growth_rate = terminal_growth_rate
        self.working_capital_turnover = working_capital_turnover
        self.capital_expenditure_rate = capital_expenditure_rate
        self.years = 5
    
    def calculate_wacc(self):
        """
        Calculate the weighted average cost of capital (WACC)
        : return: WACC
        """
        debt_weight = self.debt_to_equity_ratio / (1 + self.debt_to_equity_ratio)
        equity_weight = 1 / (1 + self.debt_to_equity_ratio)
        wacc = debt_weight * self.cost_of_debt * (1 - 0.25) + equity_weight * self.cost_of_equity
        return wacc
    
    def calculate_revenue(self):
        """
        Calculate the revenue for each year
        :return: Array of revenue values
        """
        revenue = np.zeros(self.years + 1)
        for i in range(self.years):
            growth_rate = self.growth_rate * (1 - self.decay_rate) ** i
            revenue[i] = self.ebitda / (1 - self.growth_rate) * (1 + growth_rate) ** i
    
    def calculate_ebitda(self, revenue):
        """
        Calculate the EBITDA for each year.

        :param revenue: Array of revenue values
        :return: Array of EBITDA values
        """
        ebitda = revenue * (1 - self.growth_rate)
        return ebitda
    
    def calculate_working_capital(self, revenue):
        """
        Calculate the working capital for each year.

        :param revenue: Array of revenue values
        :return: Array of working capital values
        """
        working_capital = revenue / self.working_capital_turnover
        return working_capital
    
    def calculate_capital_expenditure(self, revenue):
        """
        Calculate the capital expenditure for each year 

        :param revenue: Array of revenue values
        :return array of capital expenditure values

        """
        capital_expenditure = revenue * self.capital_expenditure_rate
        return capital_expenditure

    def calculate_free_cash_flow(self, ebitda, working_capital, capital_expenditure):
        """
        Calculate the free cash flow for each year.

        :param ebitda: Array of EBITDA values.
        :param working_capital: Array of working capital values.
        :param capital_expenditure: Array of capital expenditure values.
        :return: Array of free cash flow values.
        """
        fcf = ebitda - working_capital - capital_expenditure
        return fcf

    def calculate_present_value(self, fcf, wacc):
        """
        Calculate the present value of the free cash flow.

        :param fcf: Array of free cash flow values.
        :param wacc: Weighted average cost of capital.
        :return: Present value of the free cash flow.
        """
        pv = 0
        for i in range(self.years):
            pv += fcf[i] / (1 + wacc) ** (i + 1)
        return pv

    def calculate_terminal_value(self, fcf):
        """
        Calculate the terminal value using the perpetuity growth model.

        :param fcf: Array of free cash flow values.
        :return: Terminal value.
        """
        terminal_value = fcf[-1] * (1 + self.terminal_growth_rate) / (self.discount_rate - self.terminal_growth_rate)
        return terminal_value

    def calculate_enterprise_value(self, fcf):
        """
        Calculate the enterprise value by adding the present value and terminal value.

        :param fcf: Array of free cash flow values.
        :return: Enterprise value.
        """
        pv = self.calculate_present_value(fcf)
        terminal_value = self.calculate_terminal_value(fcf)
        enterprise_value = pv + terminal_value / (1 + self.discount_rate) ** self.years
        return enterprise_value

    def run_model(self):
        """
        Run the DCF model and return the enterprise value.

        :return: Enterprise value.
        """
        revenue = self.calculate_revenue()
        ebitda = self.calculate_ebitda(revenue)
        working_capital = self.calculate_working_capital(revenue)
        capital_expenditure = self.calculate_capital_expenditure(revenue)
        enterprise_value = self.calculate_enterprise_value(revenue)
        return ebitda, working_capital, capital_expenditure, enterprise_value