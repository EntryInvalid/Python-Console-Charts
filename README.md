# Python-Charts
A basic Python program that lets you choose from 2 different APIs and 2 different charting-libraries in order to gather data and visualize it in a candlestick chart

I buillt this program after bulding a GUI program with the same functionality in Java. I wanted to see just how much harder I was making it on myself using Java intsead of Python. The bigger project in Java is meant for me to slowly build and improve over-time to demonstarate my knowledge as I learn. I figured I'd stick with Java because it's structure and verbosity makes it really good for learning and demonstrating understanding more than Python. Nevertheless, I figured it would be good to post to demostrate that I can also write programs in Python.

This Program requires an API key to AlphaVantage API, or MarketData API; both of these are free. 
Without one of these you will need to get sample data and alter the code to take the sample data as input. 

To use the program run the file 'PythonChartsMain.py'. 

This program runs out of a console or a will ask you which API to use, then proceeed to ask you questions to create the API call URL. After it gets all the info it will ask you if want to use a new API Key or if you want to use the one saved. If you want to add one you can do so in the code. There is a section marked with '#' symbols at the top of the respective file (AlphaVantageAPI or MarketDataAPI). The program loops for multiple queries or charts too, so if you close a chart and do another query without closing the program it will save the key while the program is running. Once you enter the Api Key it will print part of the data in  the console and ask you if you want to use the GUI Chart or the Browser Chart. The GUI Chart is through mpl-finance and the Browser Chart is through Dash and Plotly. From there you can close out the chart and proceed to look at another chart or close the program.


# Errors
- Option Query
- Choose how much sets of data are put in the chart for AlphaVantage
- Make a small Database or even file to save the Api Key even after closing program
- 
