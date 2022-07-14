import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
import tkinter

%matplotlib inline

class metrics:
    stock = None

    # default download
    def __init__(self, name):
        start = '2014-01-01'
        end = '2019-01-01'

        global stock # can now edit global stock
        
        # downloads 5 year data
        # open, close, high, low, volume
        stock = yf.download(name, start, end)

    # stock fluctuation
    def fluctuation(self, name): 
        stock['Volume'].plot(label = name, figsize = (15,7))
        plt.title('Volume of Stock traded')
        plt.legend

    # market cap
    def cap(self, name):
        stock['MarketCap'] = stock['Open'] * stock['Volume']
        stock['MarketCap'].plot(label = name, figsize = (15,7))

    # 50-day moving average
    def fifty_day_ma(self, name):
        stock['MA50'] = stock['Open'].rolling(50).mean()
        stock['MA50'].plot()

    # 200-day moving average
    def two_hundred_day_ma(self, name):
        stock['MA200'] = stock['Open'].rolling(200).mean()
        stock['MA200'].plot()

    # scatter plot matrix
    def scatter_plot(self, name):
        data = pd.concat([stock['Open']], axis = 1)
        data.columns = [name+'Open']
        scatter_matrix(data, figsize = (8,8), hist_kwds={'bins':250})

    # volatility    
    def volatility(self, name):
        stock['returns'] = (stock['Close']/stock['Close'].shift(1)) - 1
        stock['returns'].hist(bins = 100, label = name, alpha = 0.5, figsize = (15,7))
        plt.legend

    # p/e ratio
    def p_e_ratio(self, name):
