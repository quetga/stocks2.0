 import yfinance as yf
import streamlit as st
import pandas as pd
from PIL import Image


image = Image.open('stocks_logos.jpg')
st.image(image, caption='Stocks Logo')
st.write("""
# Stock Trap
Shown are the stock **closing price** and ***volume*** of various trending companies!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'AAPL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2022-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Apple Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Apple Volume Price
""")
st.line_chart(tickerDf.Volume)

tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2022-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Google Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Google Volume Price
""")
st.line_chart(tickerDf.Volume)

tickerSymbol = 'GC=F'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2022-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Gold Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Gold Volume Price
""")
st.line_chart(tickerDf.Volume)

tickerSymbol = 'DJIA'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2019-5-31', end='2022-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## US30 Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## US30 Volume Price
""")
st.line_chart(tickerDf.Volume)
