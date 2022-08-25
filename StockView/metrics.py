from cgitb import text
from tracemalloc import start
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf # Yahoo Finance stock data
import config

# dict_keys(['zip', 'sector', 'fullTimeEmployees', 'longBusinessSummary', 'city', 'phone', 'state', 'country', 'companyOfficers', 'website', 
# 'maxAge', 'address1', 'fax', 'industry', 'address2', 'ebitdaMargins', 'profitMargins', 'grossMargins', 'operatingCashflow', 'revenueGrowth', 
# 'operatingMargins', 'ebitda', 'targetLowPrice', 'recommendationKey', 'grossProfits', 'freeCashflow', 'targetMedianPrice', 'currentPrice', 
# 'earningsGrowth', 'currentRatio', 'returnOnAssets', 'numberOfAnalystOpinions', 'targetMeanPrice', 'debtToEquity', 'returnOnEquity', 'targetHighPrice', 
# 'totalCash', 'totalDebt', 'totalRevenue', 'totalCashPerShare', 'financialCurrency', 'revenuePerShare', 'quickRatio', 'recommendationMean', 'exchange', 
# 'shortName', 'longName', 'exchangeTimezoneName', 'exchangeTimezoneShortName', 'isEsgPopulated', 'gmtOffSetMilliseconds', 'quoteType', 'symbol', 'messageBoardId', 
# 'market', 'annualHoldingsTurnover', 'enterpriseToRevenue', 'beta3Year', 'enterpriseToEbitda', '52WeekChange', 'morningStarRiskRating', 'forwardEps', 
# 'revenueQuarterlyGrowth', 'sharesOutstanding', 'fundInceptionDate', 'annualReportExpenseRatio', 'totalAssets', 'bookValue', 'sharesShort', 'sharesPercentSharesOut', 
# 'fundFamily', 'lastFiscalYearEnd', 'heldPercentInstitutions', 'netIncomeToCommon', 'trailingEps', 'lastDividendValue', 'SandP52WeekChange', 'priceToBook', 
# 'heldPercentInsiders', 'nextFiscalYearEnd', 'yield', 'mostRecentQuarter', 'shortRatio', 'sharesShortPreviousMonthDate', 'floatShares', 'beta', 'enterpriseValue', 
# 'priceHint', 'threeYearAverageReturn', 'lastSplitDate', 'lastSplitFactor', 'legalType', 'lastDividendDate', 'morningStarOverallRating', 'earningsQuarterlyGrowth', 
# 'priceToSalesTrailing12Months', 'dateShortInterest', 'pegRatio', 'ytdReturn', 'forwardPE', 'lastCapGain', 'shortPercentOfFloat', 'sharesShortPriorMonth', 
# 'impliedSharesOutstanding', 'category', 'fiveYearAverageReturn', 'previousClose', 'regularMarketOpen', 'twoHundredDayAverage', 'trailingAnnualDividendYield', 
# 'payoutRatio', 'volume24Hr', 'regularMarketDayHigh', 'navPrice', 'averageDailyVolume10Day', 'regularMarketPreviousClose', 'fiftyDayAverage', 'trailingAnnualDividendRate', 
# 'open', 'toCurrency', 'averageVolume10days', 'expireDate', 'algorithm', 'dividendRate', 'exDividendDate', 'circulatingSupply', 'startDate', 'regularMarketDayLow', 
# 'currency', 'trailingPE', 'regularMarketVolume', 'lastMarket', 'maxSupply', 'openInterest', 'marketCap', 'volumeAllCurrencies', 'strikePrice', 'averageVolume', 'dayLow', 
# 'ask', 'askSize', 'volume', 'fiftyTwoWeekHigh', 'fromCurrency', 'fiveYearAvgDividendYield', 'fiftyTwoWeekLow', 'bid', 'tradeable', 'dividendYield', 'bidSize', 'dayHigh', 
# 'regularMarketPrice', 'preMarketPrice', 'logo_url', 'trailingPegRatio'])

class metrics:
    # default download
    def def_download(name):
        # global stock # can now edit global stock
        # global stock_tick # can now edit global stock_tick
        # global start_date
        # global end_date

        config.start_date = '2017-01-01'
        config.end_date = '2022-01-01'

        # downloads 5 year data
        # open, close, high, low, volume
        config.stock = yf.download(name, config.start_date, config.end_date) 
        config.stock_tick = yf.Ticker(name)

    def write_to_html():
        # add Ticker data to data.html file 
        file = open("data.html","w") # automatically deletes past data
        result = stock.to_html()
        file.write(result)
        file.close

    # following guide
    def confused():
        close = stock['Close']
        all_weekdays = pd.date_range(start_date, end_date, freq='B')
        close = close.reindex(all_weekdays)

    # stock fluctuation
    def fluctuation(self, name): 
        global stock

        stock['Volume'].plot(label = name, figsize = (15,7))
        plt.title('Volume of Stock traded')
        plt.legend

    # market cap
    def cap(name):
        config.stock['MarketCap'] = config.stock['Open'] * config.stock['Volume']
        config.stock['MarketCap'].plot(label = name, figsize = (15,7))

    # 50-day moving average
    def fifty_day_ma():
        stock['MA50'] = stock['Open'].rolling(50).mean()
        stock['MA50'].plot()

    # 200-day moving average
    def two_hundred_day_ma():
        config.stock['MA200'] = config.stock['Open'].rolling(200).mean()
        config.stock['MA200'].plot()

    # scatter plot matrix
    def scatter_plot(name):
        data = pd.concat([stock['Open']], axis = 1)
        data.columns = [name+'Open']
        scatter_matrix(data, figsize = (8,8), hist_kwds={'bins':250})

    # volatility    
    def volatility(name):
        stock['returns'] = (stock['Close']/stock['Close'].shift(1)) - 1
        stock['returns'].hist(bins = 100, label = name, alpha = 0.5, figsize = (15,7))
        plt.legend

    # p/e ratio
    def p_e_ratio():
        stock_tick.info['forwardPE']

    # peg ratio
    def peg_ratio():
        stock_tick.info['pegRatio']
    
    # free cash flow
    def cash_flow():
        stock_tick.info['freeCashFlow']

    # return on equity
    def roe():
        stock_tick.info['returnOnEquity']

    # discounted cash flow
    def discount_cash_flow():
        stock_tick.info['returnOnEquity']

        # dcf = (cash_flow / (1 + 0.04) ** 1) + (cash_flow / (1 + 0.04) ** 1) + (cash_flow / (1 + 0.04) ** 1) + (cash_flow / (1 + 0.04) ** 1) + (cash_flow / (1 + 0.04) ** 1)