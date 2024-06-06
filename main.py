import pandas as pd
from data.precios_historicos import obtener_precios_historicos
from data.portafolio import obtener_portafolio
from utils.calculos import calcular_valor_portafolio, calcular_portafolio_eth
from utils.graficos import graficar_comparacion
from datetime import date, timedelta

def main():
    # Definir las fechas de interés
    start_date = "2021-04-01"
    today = date.today()
    ayer = today - timedelta(days=1)
    ayer = ayer.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    fechas = pd.date_range(start=start_date, end=ayer, freq='D')

    # Obtener los precios históricos de las criptomonedas
    df_precios_historicos = obtener_precios_historicos(start_date=start_date,
                                                       end_date=end_date)

    # Obtener el portafolio
    portafolio = obtener_portafolio()

    # Calcular el valor del portafolio en cada fecha
    valores_portafolio = calcular_valor_portafolio(df_precios_historicos, portafolio)

    # Calcular el valor del portafolio compuesto únicamente de ETH
    valores_portafolio_eth = calcular_portafolio_eth(valores_portafolio, df_precios_historicos['ETH'])

    # Graficar la comparación de los portafolios
    graficar_comparacion(fechas, valores_portafolio, valores_portafolio_eth)

if __name__ == '__main__':
    main()