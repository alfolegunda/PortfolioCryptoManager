import pandas as pd

def calcular_valor_portafolio(df_precios_historicos, portafolio):
    df_cantidades = pd.DataFrame([portafolio])
    valores_portafolio = df_precios_historicos.mul(df_cantidades.iloc[0], axis=1).sum(axis=1)
    return valores_portafolio

def calcular_portafolio_eth(valores_portafolio, precios_eth):
    cantidad_eth_inicial = valores_portafolio.iloc[0] / precios_eth.iloc[0]
    valores_portafolio_eth = precios_eth * cantidad_eth_inicial
    return valores_portafolio_eth

def calcular_portafolio_btc(valores_portafolio, precios_btc):
    cantidad_btc_inicial = valores_portafolio.iloc[0] / precios_btc.iloc[0]
    valores_portafolio_btc = precios_btc * cantidad_btc_inicial
    return valores_portafolio_btc