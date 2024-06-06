import yfinance as yf
import pandas as pd

def obtener_precios_historicos(start_date, end_date):
    criptos = {
        'BTC': 'BTC-USD',
        'ETH': 'ETH-USD',
        'PEPE': 'PEPE24478-USD',
        'SHIB': 'SHIB-USD',
        'SOL': 'SOL-USD'
    }

    precios_historicos = {}
    for cripto, ticker in criptos.items():
        precios_historicos[cripto] = yf.download(ticker, start=start_date, end=end_date,
                                                 progress=False)['Adj Close']

    precios_historicos = pd.DataFrame(precios_historicos)
    precios_historicos.fillna(0, inplace=True)

    return precios_historicos