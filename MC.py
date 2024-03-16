# Importing Libraries 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime as dt 
import yfinance as yf

#from pandas_datareader import data as pdr   #yahoo specific data (not working!)

#import data
def get_data(stocks,start,end):
    stockdb = yf.download(stocks, start=start, end=end)['Adj Close']
    returns = stockdb.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

stockList = ['CBA','BHP','TLS','NAB','WBC','STO']
stocks = [stock + '.AX' for stock in stockList]
endDate =  dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)
print(meanReturns)


