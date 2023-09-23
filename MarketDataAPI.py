from datetime import datetime
import requests


class MarketDataAPI:

    def __init__(self):
        #########################################################################################################
        self.auth_token = None  # - SET API KEY HERE - #
        #########################################################################################################
        self.root_url = "https://api.marketdata.app/v1/"
        self.url = None
        
        self.security_type = None
        self.data_type = None
        self.ticker = None
        self.candle_range = None
        self.option_side = None
        self.expiration_date = None
        self.lookup_date = None
        self.start = None
        self.end = None
        self.strike_price = None
        
    def start_query(self):
        self.url = self.get_url() + "&format=csv"

        ohlc = self.api()

        return ohlc  # use security_type to determine if chart is relevant.

    def get_url(self):

        print("----------------------------------------------------------------------------------------------------")
        self.set_security()
        self.set_data()
        self.set_ticker()
        self.set_candle_range()
        self.set_option_side()
        self.set_expiration()
        self.set_start_end()
        self.set_strike()
        print("----------------------------------------------------------------------------------------------------")

        return self.compose_url()

    def api(self):

        question1 = input("Do you want to use a new MarketData API Key? Answer 'yes' to proceed or enter any key ")
        if question1 == "yes":
            question2 = input("The default API key will be regenerated after program refreshes. "
                              "If this was a mistake enter 'exit', else hit any key")
            if question2 == "exit":
                print("API key change aborted")
            else:
                self.auth_token = input("Enter your new API key here: ")

        if self.auth_token is None:
            self.auth_token = input("There is currently no MarketDataAPI Authentication auth_token set. "
                                    " Please enter auth_token now: ")

        print(self.url)
        print()

        header = {
            "Authorization": f"Token {self.auth_token}"
        }
        response = requests.request("GET", self.url, headers=header)

        if response.status_code in (200, 203):  # Check if the request was successful
            data = response.text  # Assuming the response is in JSON format
            return data
        else:
            print()
            print(f"Failed to query API. Status code: {response.status_code}")
            return None

    def set_security(self):
        # Choose a security type
        while True:
            print()
            print("Choose a category:")
            print("1. stocks")
            print("2. options")
            print("3. indices")
            print()
            choice = input("Enter the number of your choice: ")
            if choice in ['1', '2', '3']:
                self.security_type = "stocks" if choice == '1' else "options" if choice == '2' else "indices"
                break
            print()
            print("Invalid choice. Please try again.")

    def set_data(self):
        # Select data type for stocks or options
        if self.security_type == "options":
            while True:
                print()
                print("Choose a data type:")
                print("1. lookup (finds OCC option ticker symbol")
                print("2. quotes (needs OCC ticker -- includes mark, bid, bid size, ask, ask size, last, volume)")
                print("3. expirations (available expirations for ticker)")
                print("4. strikes (available strikes for given ticker and )")
                print("5. chain (shows all options data for calls or puts of given expiration date. data includes"
                      " prices, iv, greeks, extrinsic intrinsic and underlying price, etc")
                print()
                choice = input("Enter the number of your choice: ")

                if choice in ['1', '2', '3', '4', '5']:
                    self.data_type = "lookup" if choice == '1' else "quotes" if choice == '2' else "expirations" \
                        if choice == '3' else "strikes" if choice == '4' else "chain"
                    break
                print()
                print("Invalid choice. Please try again.")

        else:
            while True:
                print()
                print("Choose a data type:")
                print("1. candles (OHLC and volume for specified start/end and candle range")
                print("2. quotes (mark, bid, bid size, ask, ask size, last, volume)")
                print()
                choice = input("Enter the number of your choice: ")

                if choice in ['1', '2']:
                    self.data_type = "candles" if choice == '1' else "quotes"
                    break
                print()
                print("Invalid choice. Please try again.")

    def set_ticker(self):
        # Set ticker
        if self.security_type == "options" and self.data_type == "quotes":
            print()
            self.ticker = input("Enter the OCC option ticker symbol(try the lookup feature if you dont know it): ")

        else:
            print()
            self.ticker = input("Enter the security type's ticker: ")
            
    def set_candle_range(self):
        # Set range of each candlestick if necessary
        if self.data_type == "candles":
            while True:
                print()
                print("Choose each candlestick's range: ")
                print("1. minutely")
                print("2. hourly")
                print("3. daily")
                print("4. weekly")
                print()
                choice = input("Enter the number of your choice: ")

                if choice in ['1', '2', '3', '4']:
                    self.candle_range = "1" if choice == '1' else "H" if choice == '2' else "D" \
                        if choice == '3' else "W"
                    break
                print()
                print("Invalid choice. Please try again.")

    def set_option_side(self):
        # Set option side to call or put if necessary
        if self.data_type == "chain" or self.data_type == "lookup":
            while True:
                print()
                print("Choose to see chain for call side or put side: ")
                print("1. call")
                print("2. put")
                print()
                choice = input("Enter the number of your choice: ")

                if choice in ['1', '2']:
                    self.option_side = "call" if choice == '1' else "put"
                    break
                print()
                print("Invalid choice. Please try again.")

    def set_expiration(self):
        # Set expiration_date if necessary
        if self.data_type == "strikes" or self.data_type == "chain" or self.data_type == "lookup":
            print()
            print("Enter the expiration date for the options contract below, the format should be YYYY-MM-DD.")
            print()
            self.expiration_date = input("enter: ")

        # Parse the input string with the format YYYY-MM-DD to the desired format MM/DD/YYYY for the lookup data_type
            self.lookup_date = datetime.strptime(self.expiration_date, "%Y-%m-%d").strftime("%m/%d/%Y")

    def set_start_end(self):
        # Set start and end dates if necessary
        if self.data_type == "candles":
            print()
            self.start = input("Using the format YYYY-MM-DD, enter the start date for your query: ")

            print()
            self.end = input("Using the format YYYY-MM-DD, enter the end date for your query: ")

    def set_strike(self):
        # Set strike price
        if self.data_type == "lookup":
            print()
            self.strike_price = input("Enter the strike price for the OCC ticker you are trying to find: ")
            return self.strike_price

    def compose_url(self):
        # Compose query URL
        if self.data_type == "candles":
            query_url = (f"{self.root_url}{self.security_type}/{self.data_type}"
                         f"/{self.candle_range}/{self.ticker}?from={self.start}&to={self.end}")
            return query_url

        if self.data_type == "chain":
            query_url = (f"{self.root_url}{self.security_type}/{self.data_type}"
                         f"/{self.ticker}/?expiration={self.expiration_date}&side={self.option_side}")
            return query_url

        if self.data_type == "strikes":
            query_url = (f"{self.root_url}{self.security_type}/{self.data_type}"
                         f"/{self.ticker}?expiration={self.expiration_date}")
            return query_url

        if self.data_type == "lookup":
            query_url = (f"{self.root_url}{self.security_type}/{self.data_type}"
                         f"/{self.ticker}%0{self.lookup_date}%00{self.strike_price}00%00{self.option_side}")
            return query_url

        else:
            query_url = (f"{self.root_url}{self.security_type}/{self.data_type}"
                         f"/{self.ticker}")
            return query_url
