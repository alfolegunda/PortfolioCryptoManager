import pypfopt

class PortfolioOptimizer:
    def __init__(self, retornos, cov_matrix, weight_bounds=(0, 1)):
        self.retornos = retornos
        self.cov_matrix = cov_matrix
        self.weight_bounds = weight_bounds

    def _initialize_ef(self):
        return pypfopt.EfficientFrontier(self.retornos, self.cov_matrix, weight_bounds=self.weight_bounds)

    def optimize(self, strategy, **kwargs):
        ef = self._initialize_ef()
        if strategy == 'min_volatility':
            weights = ef.min_volatility()
        elif strategy == 'max_sharpe':
            weights = ef.max_sharpe()
        elif strategy == 'max_quadratic_utility':
            weights = ef.max_quadratic_utility(**kwargs)
        elif strategy == 'efficient_risk':
            weights = ef.efficient_risk(**kwargs)
        elif strategy == 'efficient_return':
            weights = ef.efficient_return(**kwargs)
        else:
            raise ValueError("Invalid strategy")

        cleaned_weights = ef.clean_weights()
        print(cleaned_weights)
        ef.portfolio_performance(verbose=True)
        return cleaned_weights

# Uso de la clase
retornos_CAPM = ...  # Reemplaza con tus datos
df_cov = ...  # Reemplaza con tus datos

optimizer = PortfolioOptimizer(retornos_CAPM, df_cov)

# Ejemplo de uso para cada estrategia
#optimizer.optimize('min_volatility')
#optimizer.optimize('max_sharpe')
#optimizer.optimize('max_quadratic_utility', risk_aversion=0.01)
#optimizer.optimize('efficient_risk', target_volatility=0.4)
#optimizer.optimize('efficient_return', target_return=0.04)



#min_volatility(): Minimizar la volatilidad.
#max_sharpe(risk_free_rate=0.02): Maximizar el Sharpe Ratio (>1 bueno, >2 muy bueno, >3 a la nasa)
#max_quadratic_utility(risk_aversion=1, market_neutral=False): Maximizar la utilidad cuadrática.
#efficient_risk(target_volatility, market_neutral=False): Maximiza el retorno dado un riesgo objetivo. EL portafolio resultante tendrá menor volatilidad que el target (pero no garantiza que sea igual).
#efficient_return(target_return, market_neutral=False): Después de optimizar, calcula la performance del portafolio optimo. Hay problemas con la última versión de Python.