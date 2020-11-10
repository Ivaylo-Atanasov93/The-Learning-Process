import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

class Share:
    def __init__(self, ticker, start_date, market_cap=None, price_to_earnings=None):
        self.ticker = ticker.upper()
        self.start_date = start_date
        self.market_cap = market_cap
        self.price_to_earnings = price_to_earnings
        self.data = None

    def __repr__(self):
        return f'Ticker: {self.ticker}\nMarket Cap: {self.market_cap}\nP/E Ratio: {self.price_to_earnings}\nAvg. Volume:' \
            f'{sum(self.data["Volume"]) / len(self.data["Volume"]):.2f}'

    def collect_price_data(self):
        day = int(self.start_date.split('/')[0])
        month = int(self.start_date.split('/')[1])
        year = int(self.start_date.split('/')[2])
        start = dt.datetime(year, month, day)
        end = dt.datetime.now()
        self.data = web.DataReader(f'{self.ticker}', 'yahoo', start, end)
        self.data = self.data[['Open', 'High', 'Low', 'Close', 'Volume']]
        self.data.reset_index(inplace=True)
        self.data['Date'] = self.data['Date'].map(mdates.date2num)

    def show_chart(self):
        ax = plt.subplot()
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.set_title(f'{self.ticker} Share Price', color='white')
        ax.set_xlabel('Date', color='white')
        ax.set_ylabel('US Dollars', color='white')
        ax.set_facecolor('black')
        ax.figure.set_facecolor('#121212')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis_date()
        candlestick_ohlc(ax, self.data.values, 0.5, 'g', 'r')
        plt.show()


stock = Share(input('Enter a ticker: '), input('Enter a start date(format DD/MM/YYYY): '))
stock.collect_price_data()
stock.show_chart()
print(stock)

