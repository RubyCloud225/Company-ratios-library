from marketshare import MarketAnalysis

class MarketCalculator:
    def __init__(self, total_population, total_consumption, total_revenue, lead_generation_data, total_customers, total_leads, desired_market_share, marketing_budget, sales_team_size):
        self.total_population = total_population
        self.total_leads = total_leads
        self.total_customers = total_customers
        self.total_consumption = total_consumption
        self.market_shares = MarketAnalysis
        self.lead_generation_data = lead_generation_data
        self.desired_market_share = desired_market_share
        self.marketing_budget = marketing_budget
        self.sales_team_size = sales_team_size
        self.total_revenue = total_revenue

    def calculate_consumption_per_capita(self):
        consumption_per_capita = self.total_consumption / self.total_population
        return consumption_per_capita
    
    def calculate_conversion(self):
        if self.total_leads == 0:
            return 0.0 # avoids division by zero
        conversion_rate = (self.total_customers / self.total_leads) * 100
        return conversion_rate

    def calculate_tam(self, consumption_per_capita):
        """
        Calculate the Total Addressable Market by multiplying the total population bu consumption per capita

        :return: The TAM
        """

        tam = self.total_population * consumption_per_capita
        return tam
    
    def calculate_target_market_size(self, tam):
        """
        Calculate the target market size by multiplying Tam and desired market share

        :return: The target market size
        """
        target_market_size = tam * self.desired_market_share
        return target_market_size
    
    def calculate_cost_per_lead(self):
        """
        Calculate the cost per lead by taking a weighted average of the cost per lead for each channel.
        
        :return: The cost per lead
        """
        total_leads = sum([leads for _, leads in self.lead_generation_data.values()])
        weighted_sum = sum([spend / leads for spend, leads in self.lead_generation_data.values()])
        cost_per_lead = weighted_sum / total_leads
        return cost_per_lead
    
    def calculate_lead_generation_rate(self, cost_per_lead):
        lead_generation_rate = self.marketing_budget / cost_per_lead
        return lead_generation_rate
    
    def calculate_cost_per_lead(self, lead_generation_rate):
        cost_per_lead = self.marketing_budget / lead_generation_rate
        return cost_per_lead

    def calculate_penetration_rate(self, tam, target_market_size):
        """
        Calculate the Penetration rate by dividing the target market size by the TAM

        :param tam: The Total Addressable Market
        :return: The penetration rate
        """
        penetration_rate = target_market_size / tam
        return penetration_rate
    
    def calculate_competition_rate(self, calculate_number_of_competitors):
        competition_rate = calculate_number_of_competitors / self.total_population
        return competition_rate
    
    def calculate_sales_conversion_rate(self, lead_generation_rate):
        """
        Calculate the sales conversion rate by dividing the sales team size by the lead generation rate

        :return: The sales conversion rate
        """
        sales_conversion_rate = self.sales_team_size / lead_generation_rate
        return sales_conversion_rate
    
    def calculate_sam(self, tam, penetration_rate):
        """
        Calculate the Serviceable Avaliable Market (SAM) by multiplying TAM by pentration rate

        :param tam: the total addressable market
        :return: The SAM
        """
        sam = tam * penetration_rate
        return sam
    
    def calculate_som(self, sam, competition_rate, sales_conversion_rate):
        """
        Calculate the Serviceable Obtainable Market (SOM) by multiplying the SAM, competition rate and sales conversion rate

        :param sam: The Serviceable Avaliable Market
        :return: The SOM
        """
        som = sam * (1 - competition_rate) * sales_conversion_rate
        return som
    
    def calculate_market_size(self, sam, tam):
        """
        Calculate the market size by multiplying the Tam and SAM

        return: The market size
        """
        market_size = sam * tam
        return market_size
    
    def calculate_average_revenue_per_user(self):
        
        return self.total_revenue / self.total_leads
    
    def calculate_revenue_by_firm(self):
        arpus = []
        for leads in self.total_leads_by_firm():
            arpus.append(self.total_revenue * (leads / self.total_leads))
        return arpus
    
    def calculate_potential_revenue(self, average_revenue_per_user, market_size):
        """
        Calculate the potential revenue by multiplying the market size and average revenue per user

        :param average_revenue
        :return: The potential revenue
        """
        potential_revenue = market_size * average_revenue_per_user
        return potential_revenue
    
"""
# Example usage:
marketing_spend = 100000
lead_generation_data = {
    "Facebook": (30000, 300),
    "Google Ads": (25000, 250),
    "Email": (20000, 200),
    # ...
}

calculator = CostPerLeadCalculator(marketing_spend, lead_generation_data)
cost_per_lead = calculator.calculate_cost_per_lead()
print("Cost per Lead:", cost_per_lead)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
tam = calculator.calculate_tam()
print("Total Addressable Market (TAM):", tam)

calculator = EnergyCalculator(total_energy_consumption=100000000, total_population=100000)
energy_consumption_per_capita = calculator.calculate_energy_consumption_per_capita()
print("Energy Consumption per Capita:", energy_consumption_per_capita)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
target_market_size = calculator.calculate_target_market_size()
print("Target Market Size:", target_market_size)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
lead_generation_rate = calculator.calculate_lead_generation_rate()
print("Lead Generation Rate:", lead_generation_rate)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
number_of_competitors = calculator.calculate_number_of_competitors()
print("Number of Competitors:", number_of_competitors)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
tam = calculator.calculate_tam()
target_market_size = calculator.calculate_target_market_size()
penetration_rate = calculator.calculate_penetration_rate(tam, target_market_size)
print("Penetration Rate:", penetration_ra

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
competition_rate = calculator.calculate_competition_rate()
print("Competition Rate:", competition_rate)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
sales_conversion_rate = calculator.calculate_sales_conversion_rate()
print("Sales Conversion Rate:", sales_conversion_rate)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
tam = calculator.calculate_tam()
penetration_rate = calculator.calculate_penetration_rate(tam, calculator.calculate_target_market_size())
sam = calculator.calculate_sam(tam, penetration_rate)
print("Serviceable Available Market (SAM):", sam)

calculator = EnergyMarketCalculator(energy_consumption_per_capita=1000, desired_market_share=0.2, market_concentration=0.5, marketing_budget=100000, sales_team_size=10, conversion_rate_from_lead_to_customer=0.1)
tam = calculator.calculate_tam()
target_market_size = calculator.calculate_target_market_size()
penetration_rate = calculator.calculate_penetration_rate(tam, target_market_size)
sam = calculator.calculate_sam(tam, penetration_rate)
competition_rate = calculator.calculate_competition_rate()
sales_conversion_rate = calculator.calculate_sales_conversion_rate()
som = calculator.calculate_som(sam, competition_rate, sales_conversion_rate)

"""