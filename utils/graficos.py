import matplotlib.pyplot as plt

def graficar_comparacion(df_portafolios):
    plt.figure(figsize=(12, 6))

    fechas = df_portafolios.index

    for column in df_portafolios:
        plt.plot(fechas, df_portafolios[column], label=column)

    plt.title('Comparación del Valor del Portafolio a lo Largo del Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Valor del Portafolio (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
