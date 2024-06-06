import matplotlib.pyplot as plt

def graficar_comparacion(fechas, valores_portafolio, valores_portafolio_eth):
    plt.figure(figsize=(12, 6))
    plt.plot(fechas, valores_portafolio, label='Portafolio Actual')
    plt.plot(fechas, valores_portafolio_eth, label='Portafolio ETH')
    plt.title('Comparación del Valor del Portafolio a lo Largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Valor del Portafolio (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()