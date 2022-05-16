import pandas as pd
import numpy as np
import plotly.graph_objects as go
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf

tickers = ['AAPL', 'GOOG', 'TSLA']
data = yf.download(tickers, start="2021-01-07",
                   end="2021-09-30", group_by='ticker')

aapl = data[('AAPL',)]
goog = data[('GOOG',)]
tsla = data[('TSLA',)]

N = len(tickers)
fig, axes = plt.subplots(N, figsize=(20, 5*N), sharex=True)

for df, t, ax in zip([aapl, goog, tsla], tickers, axes):
    mpf.plot(df, ax=ax, axtitle=t, type='line',
             show_nontrading=True)  # volume=True
