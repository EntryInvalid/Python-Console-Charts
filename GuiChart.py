import mplfinance as mpf
import talib
import matplotlib.pyplot as plt
import matplotlib


class GuiChart:

    def __init__(self):
        self.ta = talib

    def get_chart(self, dataframe):
        # Set plot and index
        plot = dataframe
        print(plot)

        indicators = self.get_indicators(plot)

        matplotlib.use('TkAgg')

        # Plot the candlestick chart with additional plots
        mpf.plot(plot, type='candle', addplot=indicators, volume=True)
        plt.show()

    def get_indicators(self, plot):

        # Calculate Moving Averages (MAs)
        plot['MA10'] = (self.ta.SMA(plot['Close'], timeperiod=10))
        plot['MA20'] = self.ta.SMA(plot['Close'], timeperiod=20)
        plot['MA50'] = self.ta.SMA(plot['Close'], timeperiod=50)

        # Calculate RSI
        plot['RSI'] = self.ta.RSI(plot['Close'])

        # Calculate MACD
        plot['MACD'], plot['MACD_Signal'], plot['MACD_Hist'] = (talib.MACD(plot['Close']))

        # Create additional plots for indicators
        indicators = [
            mpf.make_addplot(plot['MA10'], color='green'),
            mpf.make_addplot(plot['MA20'], color='yellow'),
            mpf.make_addplot(plot['MA50'], color='red'),
            mpf.make_addplot(plot['RSI'], panel=1, color='green'),
            mpf.make_addplot(plot['MACD'], panel=2, color='brown')
        ]

        return indicators
