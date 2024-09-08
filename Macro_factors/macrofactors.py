import pandas as pd
import requests
import json
import plotly.graph_objects as go

class MacroeconomicDataCollector:
    def __init__(self):
        self.unemployment_url = 'https://api.db.nomics.world/v22/series/Eurostat/une_rt_m/M.NSA.TOTAL.PC_ACT.T.EA19?observations=1'
        self.inflation_url = 'https://api.db.nomics.world/v22/series/WB/WDI/FP.CPI.TOTL.ZG-EU?observations=1'
        self.retail_prices_url = 'https://api.db.nomics.world/v22/series/Eurostat/sts_trtu_m/M.TOVT.G47.CA.PCH_SM.EA19?observations=1'

    def get_unemployment_data(self):
        response = requests.get(self.unemployment_url)
        data = response.json()
        periods = data['series']['docs'][0]['period']
        values = data['series']['docs'][0]['value']
        dataset = data['series']['docs'][0]['dataset_name']
        unemployment_data = pd.DataFrame(values, index=periods)
        unemployment_data.columns = [dataset]
        return unemployment_data

    def get_inflation_data(self):
        response = requests.get(self.inflation_url)
        data = response.json()
        periods = data['series']['docs'][0]['period']
        values = data['series']['docs'][0]['value']
        dataset = data['series']['docs'][0]['dataset_name']
        inflation_data = pd.DataFrame(values, index=periods)
        inflation_data.columns = [dataset]
        return inflation_data

    def get_retail_prices_data(self):
        response = requests.get(self.retail_prices_url)
        data = response.json()
        periods = data['series']['docs'][0]['period']
        values = data['series']['docs'][0]['value']
        dataset = data['series']['docs'][0]['dataset_name']
        retail_prices_data = pd.DataFrame(values, index=periods)
        retail_prices_data.columns = [dataset]
        return retail_prices_data

    def collect_and_save_data(self):
        unemployment_data = self.get_unemployment_data()
        inflation_data = self.get_inflation_data()
        retail_prices_data = self.get_retail_prices_data()
        unemployment_data.to_csv('unemployment_data.csv', index=False)
        inflation_data.to_csv('inflation_data.csv', index=False)
        retail_prices_data.to_csv('retail_prices_data.csv', index=False)

"""
# Example usage:
collector = MacroeconomicDataCollector()
collector.collect_and_save_data()
"""
