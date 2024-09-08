from DCF import DCFModel


class ScenarioAnalysis:
    def __init__(self, base_case, optimistic_case, pessimistic_case):
        self.base_case = base_case
        self.optimistic_case = optimistic_case
        self.pessimistic_case = pessimistic_case
        self.dcf_model = DCFModel
        self.revenue = self.dcf_model.calculate_revenue()

    def run_scenario(self, scenario):
        revenue_growth_rate = scenario['revenue_growth_rate']
        operating_margin = scenario['operating_margin']
        wacc = scenario['wacc']
        terminal_value_growth_rate = scenario['terminal_value_growth_rate']

        # Calculate the present value of the cash flows
        cash_flows = []
        for year in range(5):
            revenue = self.revenue * (1 + revenue_growth_rate) ** year
            ebit = revenue * operating_margin
            cash_flow = ebit * (1 - 0.25)  # assume 25% tax rate
            cash_flows.append(cash_flow)

        present_value = 0
        for year, cash_flow in enumerate(cash_flows):
            present_value += cash_flow / (1 + wacc) ** year

        # Calculate the terminal value
        terminal_value = cash_flows[-1] * (1 + terminal_value_growth_rate) / (wacc - terminal_value_growth_rate)

        # Calculate the equity value
        equity_value = present_value + terminal_value

        return equity_value

    def run_analysis(self):
        base_case_value = self.run_scenario(self.base_case)
        optimistic_case_value = self.run_scenario(self.optimistic_case)
        pessimistic_case_value = self.run_scenario(self.pessimistic_case)

        return {
            'Base Case': base_case_value,
            'Optimistic Case': optimistic_case_value,
            'Pessimistic Case': pessimistic_case_value
        }

"""
# Define the scenarios
base_case = {
    'revenue_growth_rate': 0.10,
    'operating_margin': 0.20,
    'wacc': 0.08,
    'terminal_value_growth_rate': 0.03
}

optimistic_case = {
    'revenue_growth_rate': 0.15,
    'operating_margin': 0.25,
    'wacc': 0.07,
    'terminal_value_growth_rate': 0.04
}

pessimistic_case = {
    'revenue_growth_rate': 0.05,
    'operating_margin': 0.15,
    'wacc': 0.09,
    'terminal_value_growth_rate': 0.02
}

# Create the scenario analysis object
analysis = ScenarioAnalysis(base_case, optimistic_case, pessimistic_case)

# Run the analysis
results = analysis.run_analysis()

# Print the results
print(results)

"""

# Define the scenarios