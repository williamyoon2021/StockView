import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
%matplotlib inline

class metrics:
    def price_to_earnings():
        start = '2014-01-01'
        end = '2019-01-01'

        # downloads 5 year data
        # open, close, high, low, volume 
        tcs = yf.download('TCS',start,end)

        # stock fluctuation
        tcs['Volume'].plot(label = 'TCS', figsize = (15,7))
        plt.title('Volume of Stock traded')
        plt.legend

        # market cap
        tcs['MarketCap'] = tcs['Open'] * tcs['Volume']
        tcs['MarketCap'].plot(label = 'TCS', figsize = (15,7))

        # 50-day moving average
        tcs['MA50'] = tcs['Open'].rolling(50).mean()
        tcs['MA50'].plot()

        # 200-day moving average
        tcs['MA200'] = tcs['Open'].rolling(200).mean()
        tcs['MA200'].plot()

        # scatter plot matrix
        data = pd.concat([tcs['Open']], axis = 1)
        data.columns = ['TCSOpen']
        scatter_matrix(data, figsize = (8,8), hist_kwds={'bins':250})