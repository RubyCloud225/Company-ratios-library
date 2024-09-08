
class MarketAnalysis:
    def __init__(self, total_industry_revenue):
        self.total_industry_revenue = total_industry_revenue
        self.companies = []

    def add_company(self, name, revenue):
        self.companies.append({"name": name, "revenue": revenue})

    def calculate_market_share(self, company):
        return company["revenue"] / self.total_industry_revenue * 100

    def calculate_number_of_competitors(self):
        return len(self.companies) - 1  # Subtract 1 for the target company

    def calculate_competitor_rate(self):
        num_competitors = self.calculate_number_of_competitors()
        return num_competitors / self.total_industry_revenue * 100

    def calculate_herfindahl_hirschman_index(self):
        market_shares = [self.calculate_market_share(company) for company in self.companies]
        return sum([market_share ** 2 for market_share in market_shares])

    def interpret_herfindahl_hirschman_index(self, hh_index):
        if hh_index < 1500:
            return "Low"
        elif hh_index < 2500:
            return "Moderate"
        else:
            return "High"

    def analyze_market(self):
        num_competitors = self.calculate_number_of_competitors()
        competitor_rate = self.calculate_competitor_rate()
        hh_index = self.calculate_herfindahl_hirschman_index()
        market_concentration = self.interpret_herfindahl_hirschman_index(hh_index)

        print("Market Shares:")
        for company in self.companies:
            market_share = self.calculate_market_share(company)
            print(f"{company['name']}: {market_share:.2f}%")

        print(f"Number of competitors: {num_competitors}")
        print(f"Competitor rate: {competitor_rate:.2f}%")
        print(f"Herfindahl-Hirschman Index (HHI): {hh_index:.2f}")
        print(f"Market concentration: {market_concentration}")
"""
# Example usage:
analysis = MarketAnalysis(total_industry_revenue=10000000)
analysis.add_company("Target Company", 1000000)
analysis.add_company("Competitor 1", 500000)
analysis.add_company("Competitor 2", 750000)
analysis.add_company("Competitor 3", 400000)
analysis.add_company("Competitor 4", 600000)
analysis.add_company("Competitor 5", 300000)
analysis.add_company("Competitor 6", 450000)
analysis.add_company("Competitor 7", 550000)
analysis.add_company("Competitor 8", 650000)
analysis.add_company("Competitor 9", 700000)
analysis.add_company("Competitor 10", 800000)

analysis.analyze_market()

"""
