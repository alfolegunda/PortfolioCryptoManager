import matplotlib.pyplot as plt
from utils import retornos
from utils import toolkit

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


def graficar_retornos(df_portafoloios):

    ret = retornos.retornos(df_portafoloios)

    for column in ret:
        sorted_returns = sorted(ret[column])
        ret_mean = ret[column].mean()
        skewness = toolkit.skewness(ret[column])

        # Output histogram
        plt.hist(sorted_returns, bins=150)
        plt.xlabel('Returns')
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column} returns', fontsize=18, fontweight='bold')
        plt.axvline(x=ret_mean, color='r', linestyle='--', label='Returns mean: ' + "{0:.2f}%".format(ret_mean * 100))
        plt.legend(loc='upper right', fontsize='x-small')
        plt.figtext(.68, .8, f"Skewness: {skewness:.2f}", fontsize=8)
        plt.show()





