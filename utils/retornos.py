def retornos(df_portafolios):
    g_portafolios = df_portafolios.pct_change()
    g_portafolios = g_portafolios.dropna()
    return g_portafolios