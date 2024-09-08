import yfinance as yf

class RatioCalculator:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = yf.Ticker(self.ticker)

    def scrape_book_value(self):
        book_value = self.data.info['bookValue']
        return book_value

    def scrape_current_market_price(self):
        current_price = self.data.info['currentPrice']
        return current_price

    def scrape_trailing_eps(self):
        trailing_eps = self.data.info['trailingEps']
        return trailing_eps

    def scrape_dividend_per_share(self):
        dividend_per_share = self.data.info['trailingAnnualDividendRate']
        return dividend_per_share

    def scrape_total_debt(self):
        balance_sheet = self.data.balance_sheet
        total_debt = balance_sheet.loc['Long Term Debt'][0]
        return total_debt

    def scrape_risk_free_rate(self):
        irx = yf.Ticker("^IRX")
        risk_free_rate = irx.info['previousClose'] / 100
        return risk_free_rate

    def calculate_pb_ratio(self):
        book_value = self.scrape_book_value()
        current_price = self.scrape_current_market_price()
        pb_ratio = current_price / book_value
        return pb_ratio

    def calculate_pe_ratio(self):
        earnings_per_share = self.scrape_trailing_eps()
        current_price = self.scrape_current_market_price()
        pe_ratio = current_price / earnings_per_share
        return pe_ratio

    def calculate_dividend_payout_ratio(self):
        dividend_per_share = self.scrape_dividend_per_share()
        earnings_per_share = self.scrape_trailing_eps()
        dividend_payout_ratio = dividend_per_share / earnings_per_share
        return dividend_payout_ratio

    def calculate_debt_to_equity_ratio(self):
        total_debt = self.scrape_total_debt()
        book_value = self.scrape_book_value()
        debt_to_equity_ratio = total_debt / book_value
        return debt_to_equity_ratio

    def calculate_sharpe_ratio(self):
        hist = self.data.history(period='1y')
        returns = hist['Close'].pct_change()
        std_dev = returns.std()
        risk_free_rate = self.scrape_risk_free_rate()
        sharpe_ratio = (returns.mean() - risk_free_rate) / std_dev
        return sharpe_ratio

    def print_ratios(self):
        pb_ratio = self.calculate_pb_ratio()
        pe_ratio = self.calculate_pe_ratio()
        eps = self.scrape_trailing_eps()
        dividend_payout_ratio = self.calculate_dividend_payout_ratio()
        debt_to_equity_ratio = self.calculate_debt_to_equity_ratio()
        sharpe_ratio = self.calculate_sharpe_ratio()
        print(f"Earnings Per Share (EPS): ${eps:.2f}")
        print(f"P/B Ratio: {pb_ratio:.2f}")
        print(f"P/E Ratio: {pe_ratio:.2f}")
        print(f"Dividend Payout Ratio: {dividend_payout_ratio:.2f}")
        print(f"Debt to Equity Ratio: {debt_to_equity_ratio:.2f}")
        print(f"Sharpe Ratio: {sharpe_ratio:.2f}")