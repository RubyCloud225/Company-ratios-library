import wbdata
import pandas as pd


class GDPDataCollector:
    def __init__(self):
        self.indicator = 'NY.GDP.MKTP.CD'  # GDP (current US$)

    def get_gdp_data(self, country, start_year, end_year):
        """
        Get GDP data for a country over a specified period.

        Args:
            country (str): Country code (e.g. 'USA', 'CAN', etc.)
            start_year (int): Start year of the period
            end_year (int): End year of the period

        Returns:
            pandas.DataFrame: GDP data for the country over the specified period
        """
        data = wbdata.get_dataset(self.indicator, country=country, convert_date=True, 
                                start_date=start_year, end_date=end_year)
        return data

    def get_gdp_data_for_multiple_countries(self, countries, start_year, end_year):
        """
        Get GDP data for multiple countries over a specified period.

        Args:
            countries (list): List of country codes (e.g. ['USA', 'CAN', etc.])
            start_year (int): Start year of the period
            end_year (int): End year of the period

        Returns:
            pandas.DataFrame: GDP data for the countries over the specified period
        """
        data = []
        for country in countries:
            country_data = self.get_gdp_data(country, start_year, end_year)
            data.append(country_data)
        return pd.concat(data, ignore_index=True)
"""
# Example usage:
collector = GDPDataCollector()
gdp_data = collector.get_gdp_data('USA', 2010, 2020)
print(gdp_data)

multiple_countries_gdp_data = collector.get_gdp_data_for_multiple_countries(['USA', 'CAN', 'MEX'], 2010, 2020)
print(multiple_countries_gdp_data)
"""
