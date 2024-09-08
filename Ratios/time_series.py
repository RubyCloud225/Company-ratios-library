import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

class StockPricePredictor:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)['Close']

    def decompose_time_series(self):
        result = seasonal_decompose(self.data, model='additive', period=1)
        plt.figure(figsize=(12, 8))
        plt.subplot(4, 1, 1)
        plt.plot(result.trend, label='Trend')
        plt.title('Trend Component')
        plt.subplot(4, 1, 2)
        plt.plot(result.seasonal, label='Seasonal')
        plt.title('Seasonal Component')
        plt.subplot(4, 1, 3)
        plt.plot(result.resid, label='Residual')
        plt.title('Residual Component')
        plt.subplot(4, 1, 4)
        plt.plot(self.data, label='Original Time Series')
        plt.title('Original Time Series')
        plt.tight_layout()
        plt.show()

    def fit_arma_model(self):
        ARMAmodel = ARIMA(self.data, order=(2, 2, 2))
        ARMAmodel = ARMAmodel.fit()
        y_pred = ARMAmodel.get_forecast(len(self.data))
        y_pred_df = pd.DataFrame(y_pred.predicted_mean, index=self.data.index)
        return y_pred_df

    def fit_sarima_model(self):
        SARIMAXmodel = SARIMAX(self.data, order=(5, 4, 2), seasonal_order=(2, 2, 2, 12))
        SARIMAXmodel = SARIMAXmodel.fit()
        y_pred = SARIMAXmodel.get_forecast(len(self.data))
        y_pred_df = y_pred.conf_int(alpha=0.05)
        y_pred_df["Predictions"] = SARIMAXmodel.predict(start=y_pred_df.index[0], end=y_pred_df.index[-1])
        y_pred_df.index = self.data.index
        y_pred_out = y_pred_df["Predictions"]
        plt.plot(y_pred_out, color='blue', label='SARIMA Predictions')
        plt.legend()
        plt.show()
