import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1mo")
    return df
