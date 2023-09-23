from AlphaVantageAPI import AlphaVantageAPI
from MarketDataAPI import MarketDataAPI
from GuiChart import GuiChart
from BrowserChart import BrowserChart
import pandas as pd
from io import StringIO


class PythonChartsMain:

    def __init__(self):
        self.alphavantage = AlphaVantageAPI()
        self.marketdata = MarketDataAPI()
        self.gui = GuiChart()
        self.browser = BrowserChart()

    def main(self):

        while True:
            # Choose Api to launch a query for
            print("**************************************************************************")
            print()
            api_choice = input("Enter 1 to use AlphaVantageAPIs"
                               "\nEnter 2 to use MarketDataAPI"
                               "\n--")

            print()

            # Call AlphaVantage Api
            if api_choice == '1':
                dataframe = self.get_alphavantage()
                app.get_chart(dataframe)
                # Call MarketData Api
            elif api_choice == '2':
                dataframe = self.get_marketdata()
                app.get_chart(dataframe)

    def get_alphavantage(self):
        print("**************************************************************************")
        stock_data = self.alphavantage.start_query()  # call Api
        dataframe = pd.read_csv(StringIO(stock_data))  # Copy to dataframe
        dataframe['timestamp'] = pd.to_datetime(dataframe['timestamp'], format='%Y-%m-%d').dt.strftime('%m/%d/%Y')
        dataframe.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']  # Rename Columns
        dataframe.index = pd.to_datetime(dataframe['Date'])  # Set index
        print("**************************************************************************")

        return dataframe

    def get_marketdata(self):
        print("**************************************************************************")
        stock_data = self.marketdata.start_query()
        dataframe = pd.read_csv(StringIO(stock_data))  # Copy to dataframe
        dataframe['t'] = pd.to_datetime(dataframe['t'], unit='s').dt.strftime('%m/%d/%Y')  # format Date
        dataframe = dataframe[['t', 'o', 'h', 'l', 'c', 'v']]  # Reorder columns
        dataframe.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']  # Rename columns
        dataframe.index = pd.to_datetime(dataframe['Date'])  # Set index
        print("**************************************************************************")

        return dataframe

    def get_chart(self, dataframe):

        ############################################################################################################
        # Both Apis output they're data in different orders and both charts expect it in different orders ##########
        # Work this out for consistency. All other issues should already be resolved ###############################
        ############################################################################################################

        chart_choice = input("Enter 1 to use GUI Chart"
                             "\nEnter 2 to use Browser Chart"
                             "\n--")

        if chart_choice == '1':
            self.gui.get_chart(dataframe)
        elif chart_choice == '2':
            self.browser.get_chart(dataframe)


if __name__ == "__main__":
    app = PythonChartsMain()
    app.main()
