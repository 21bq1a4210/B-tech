import yfinance as yf
import time

def get_stock_price(symbols):
    while True:
        for symbol in symbols:
            try:
                data = yf.download(tickers=symbol, period='1d', interval='1m')
                if data.empty:
                    print(f"No data available for {symbol}")
                else:
                    latest_price = data['Close'].iloc[-1]
                    print(f"The latest price of {symbol} is: {latest_price}")
            except Exception as e:
                print(f"An error occurred for {symbol}: {str(e)}")
        time.sleep(60)  # Fetch stock prices every minute

symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "META"]  # Add your favorite company symbols here

get_stock_price(symbols)
