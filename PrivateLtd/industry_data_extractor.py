from Nasdaq_api import NasdaqAPI

class IndustryDataExtractor:
    def __init__(self, api_key):
        self.nasdaq_api = NasdaqAPI(api_key)

    def get_industry_data(self, industry_name):
        industries = self.nasdaq_api.get_industries()
        if industry_name not in industries:
            raise ValueError(f"Industry'{industry_name}' not found")
        tickers = industries[industry_name]
        industry_data = {}

        for ticker in tickers:
            company_info = self.nasdaq_api.get_company_info(ticker)
            industry_data[ticker] = {
                "company_name": company_info["companyName"],
                "sector": company_info["sector"],
                "industry": company_info["industry"],
                "balance_sheet": self.nasdaq_api.get_balance_sheet(ticker),
                "share_price": self.nasdaq_api.get_share_price(ticker),
                "dividend_payments": self.nasdaq_api.get_dividend_payments(tickers)
            }
        return industry_data
    
    def get_industry_summary(self, industry_name):
        industry_data = self.get_industry_data(industry_name)
        summary = {
            "industry_name": industry_name,
            "num_companies": len(industry_data),
            "average_share_price": self._calculate_average_share_price(industry_data),
            "total_dividend_payments": self._calculate_total_dividend_payments(industry_data)
        }
        return summary

    def _calculate_average_share_price(self, industry_data):
        share_prices = [data["share_price"] for data in industry_data.values()]
        return sum(share_prices) / len(share_prices)

    def _calculate_total_dividend_payments(self, industry_data):
        dividend_payments = [data["dividend_payments"] for data in industry_data.values()]
        return sum(dividend_payments)

"""

# example usage
api_key = "YOUR_API_KEY" # replace with actual Nasdaq API key
industry_extractor = IndustryDataExtractor(api_key)

industry_name = input("Enter an industry name: ")
industry_data = industry_extractor.get_industry_data(industry_name)
print(industry_data)

industry_summary = industry_extractor.get_industry_summary(industry_name)
print(industry_summary)

"""