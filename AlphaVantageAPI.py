import requests


class AlphaVantageAPI:

    def __init__(self):

        #############################################################
        self.apikey = None  # - SET API_KEY HERE - #
        #############################################################

        self.size = "&outputsize=compact"  # vs compact for 100 candles of data
        self.format = "&datatype=csv"

        self.intraday = None
        self.interval = None

    def start_query(self):
        # Choose a security type
        while True:
            print()
            print("Choose a category:")
            print("1. Stocks")
            print("2. Forex")
            print("3. Crypto")
            print("4. Commodity")
            print()
            choice = input("Enter the number of your choice: ")

            if choice in ['1', '2', '3', '4']:
                query_type = ("Stock" if choice == '1' else "Forex" if choice == '2' else "Crypto" if choice == '3'
                              else "Commodity")
                break
            print()

            print("Invalid choice. Please try again.")

        if query_type == "Stock":
            return self.stock_query()

        if query_type == "Forex":
            return self.forex_query()

        if query_type == "Crypto":
            return self.crypto_query()

        if query_type == "Commodity":
            return self.commodity_query()

    def stock_query(self):
        # Set data for stock API query
        print()
        stock_ticker = input("Enter the ticker symbol for the stock you want to query: ")

        while True:
            print()
            print("Choose the candlestick timeframe: ")
            print("1. INTRADAY")
            print("2. DAILY")
            print("3. WEEKLY")
            print("4. MONTHLY")
            print()
            choice = input("Enter the number of your choice: ")

            if choice in ['2', '3', '4']:
                interval = "DAILY" if choice == '2' else "WEEKLY" if choice == '3' else "MONTHLY"
                break
            if choice in ['1']:
                interval = "INTRADAY"
                print()
                print("Choose an intraday timeframe: ")
                print("1. 5 min")
                print("2. 15 min")
                print("3. 30 min")
                print()
                choice2 = input("Enter the number of you choice: ")

                if choice2 in ['1', '2', '3']:
                    self.intraday = "5min" if choice2 == '1' else "15min" if choice2 == '2' else "30min"
                    break
                break
            print()
            print("Invalid choice. Please try again.")

        url = (f"https://www.alphavantage.co/query?function=TIME_SERIES_{interval}&symbol="
               f"{stock_ticker}&interval={self.intraday}")

        data = self.api(url)
        return data

    def forex_query(self):
        # Set data for forex API query
        print()
        forex_from = input("Enter the ticker for the currency you would like to start with: ")
        print()
        forex_to = input("Enter the ticker for the currency you would like to end with: ")

        while True:
            print()
            print("Choose each candlestick's range: ")
            print("1. FX_DAILY")
            print("2. FX_WEEKLY")
            print("3. FX_MONTHLY")
            print()
            choice = input("Enter the number of you choice: ")

            if choice in ['1', '2', '3']:
                interval = "FX_DAILY" if choice == '1' else "FX_WEEKLY" if choice == '2' else "FX_MONTHLY"
                break
            print()
            print("Invalid choice. Please try again.")

        url = (f"https://www.alphavantage.co/query?function={interval}&from_symbol={forex_from}"
               f"&to_symbol={forex_to}")

        data = self.api(url)
        return data

    def crypto_query(self):
        # Set data for crypto API query
        crypto_ticker = input("Enter the ticker symbol for the cryptocurrency you want to query: ")
        fiat_base = input("Enter the symbol for the fiat to compare to (examples - USD, JPY, EURO, JBP, GBP): ")

        while True:
            print()
            print("Choose each candlestick's range: ")
            print("1. DAILY")
            print("2. WEEKLY")
            print("3. MONTHLY")
            print()
            choice = input("Enter the number of you choice: ")

            if choice in ['1', '2', '3']:
                interval = "DAILY" if choice == '1' else "WEEKLY" if choice == '2' else "MONTHLY"
                break
            print()
            print("Invalid choice. Please try again.")

        url = (f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_{interval}&symbol"
               f"={crypto_ticker}&market={fiat_base}")

        data = self.api(url)
        return data

    def commodity_query(self):
        # Set data for commodity API query
        while True:
            print()
            print("Choose the commodity from the list below using the listed numbers as input ")
            print("ONlY the first 3 entries have variable timeframes, all others default to monthly")
            print("1. WTI")
            print("2. BRENT")
            print("3. NATURAL_GAS")
            print("4. COPPER")
            print("5. ALUMINUM")
            print("6. COPPER")
            print("7. WHEAT")
            print("8. CORN")
            print("9. COTTON")
            print("10. SUGAR")
            print("11. COFFEE")
            print()
            choice = input("Enter the number for you choice: ")

            if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
                commodity_ticker = ("WTI" if choice == '1' else "BRENT" if choice == '2' else "NATURAL_GAS" if
                                    choice == '3' else "COPPER" if choice == '4' else "ALUMINUM" if choice == '5'
                                    else "COPPER" if choice == '6' else "WHEAT" if choice == '7' else "CORN" if
                                    choice == '8' else "COTTON" if choice == '9' else "SUGAR" if choice == '10'
                                    else "COFFEE")

                if choice in ['1', '2', '3']:
                    print()
                    print("Choose each candlestick's range: ")
                    print("1. DAILY")
                    print("2. WEEKLY")
                    print("3. MONTHLY")  # Fixed typo from "MONTHLY" to "MONTHLY"
                    print()
                    choice2 = input("Enter the number for you choice: ")

                    if choice2 in ['1', '2']:
                        self.interval = ("DAILY" if choice2 == '1' else "WEEKLY")
                    else:
                        self.interval = "MONTHLY"
                    break

                else:
                    break
            else:
                print()
                print("Invalid choice. Please try again.")

        url = (f"https://www.alphavantage.co/query?function={commodity_ticker}&interval="
               f"{self.interval}")

        self.api(url)

    def api(self, url):

        question1 = input("Do you want to use a new AlphaVantage API Key? Answer 'yes' to proceed or enter any key ")
        if question1 == "yes":
            question2 = input("The default API key will be regenerated after program refreshes. "
                              "If this was a mistake enter 'exit', else hit any key")
            if question2 == "exit":
                print("API key change aborted")
            else:
                self.apikey = input("Enter your new API key here: ")

        if self.apikey is None:
            self.apikey = input("There is currently no AlphaVantageAPI Authentication auth_token set. "
                                " Please enter auth_token now: ")

        self.apikey = f"&apikey={self.apikey}"
        url = f"{url}{self.size}{self.apikey}{self.format}"

        print(url)

        response = requests.request("GET", url)

        if response.status_code == 200 or 203:  # Check if the request was successful
            # will be predominantly using csv. add "json()" to the end of response below to use JSON
            print(f"Success!! Status code: {response.status_code}")
            return response.text
        else:
            print()
            print(f"Failed to query API. Status code: {response.status_code}")
