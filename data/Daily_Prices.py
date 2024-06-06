import pandas as pd
import yfinance as yf
from datetime import date

ticker = ["BTC-USD", "ETH-USD", "SOL-USD", "SHIB-USD", "PEPE24478-USD"]

def obtener_precios_historicos(freq=None, start=None, end=None):

    if freq is None:
        periodo = "1d"
    else:
        periodo = str(freq)

    if start is None:
        start = "2020-01-01"
    else:
        start = str(start)

    if end is None:
        today = date.today()
        end = today.strftime("%Y-%m-%d")
    else:
        end = str(end)

    data = yf.download(ticker, period=periodo, start=start, end=end, progress=False)
    close = pd.DataFrame(data["Close"])

    return close