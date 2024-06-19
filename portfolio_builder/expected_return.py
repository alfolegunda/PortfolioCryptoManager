import pypfopt

class ExpectedReturnsCalculator:
    def __init__(self, df_activos, df_benchmark=None, risk_free_rate=0.071, frequency=252):
        self.df_activos = df_activos
        self.df_benchmark = df_benchmark
        self.risk_free_rate = risk_free_rate
        self.frequency = frequency

    def calculate(self, method, **kwargs):
        if method == 'capm':
            if self.df_benchmark is None:
                raise ValueError("Benchmark data is required for CAPM returns")
            returns = pypfopt.expected_returns.capm_return(
                self.df_activos, market_prices=self.df_benchmark,
                returns_data=kwargs.get('returns_data', True),
                risk_free_rate=self.risk_free_rate,
                frequency=self.frequency
            )
        elif method == 'mean_historical':
            returns = pypfopt.expected_returns.mean_historical_return(
                self.df_activos,
                returns_data=kwargs.get('returns_data', False),
                compounding=kwargs.get('compounding', True),
                frequency=self.frequency,
                log_returns=kwargs.get('log_returns', False)
            )
        elif method == 'ema_historical':
            returns = pypfopt.expected_returns.ema_historical_return(
                self.df_activos,
                returns_data=kwargs.get('returns_data', False),
                compounding=kwargs.get('compounding', True),
                span=kwargs.get('span', 500),
                frequency=self.frequency,
                log_returns=kwargs.get('log_returns', False)
            )
        else:
            raise ValueError("Invalid method")

        return returns


# # Uso de la clase
# df_activos = ...  # Reemplaza con tus datos de activos
# df_benchmark1 = ...  # Reemplaza con tus datos de benchmark
#
# calculator = ExpectedReturnsCalculator(df_activos, df_benchmark=df_benchmark1)
#
# # Cálculo de retornos usando diferentes métodos
# retornos_CAPM = calculator.calculate('capm')
# print(retornos_CAPM)
#
# retornos_mean = calculator.calculate('mean_historical')
# print(retornos_mean)
#
# df_activos_Precios = ...  # Reemplaza con tus datos de precios de activos
# calculator_prices = ExpectedReturnsCalculator(df_activos_Precios)
#
# retornos_ema = calculator_prices.calculate('ema_historical')
# print(retornos_ema)
