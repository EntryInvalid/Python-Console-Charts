import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go


class BrowserChart:
    
    def __init__(self):
        self.app = dash.Dash(__name__)
    
    def get_chart(self, dataframe):

        ohlc = go.Figure(data=[go.Candlestick(x=dataframe['Date'],
                               open=dataframe['Open'],
                               high=dataframe['High'],
                               low=dataframe['Low'],
                               close=dataframe['Close'])])
    
        # Show plot
        ohlc.show()
    
        ohlc.update_layout(
            title='Interactive Financial Data Chart',
            yaxis_title='Price',
            xaxis_title='Date',
            xaxis_rangeslider_visible=True
        )
    
        self.app.layout = html.Div([
            dcc.Graph(id='Interactive Financial Data Chart', figure=ohlc),
            # You can add more components here
        ])

        self.app.run_server(debug=True)
