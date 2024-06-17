import unittest
from utils.calculos_portfolios import calcular_valor_portafolio, calcular_portafolio_eth
import pandas as pd

class TestCalculos(unittest.TestCase):
    def test_calcular_valor_portafolio(self):
        precios_historicos = pd.DataFrame({
            'BTC': [50000, 60000],
            'ETH': [4000, 4500]
        }, index=[pd.Timestamp('2021-01-01'), pd.Timestamp('2021-02-01')])
        portafolio = {
            'BTC': 0.5,
            'ETH': 10
        }
        valores_portafolio = calcular_valor_portafolio(precios_historicos, portafolio)
        self.assertEqual(len(valores_portafolio), 2)
        self.assertAlmostEqual(valores_portafolio.iloc[0], 29000)
        self.assertAlmostEqual(valores_portafolio.iloc[1], 34500)

    def test_calcular_portafolio_eth(self):
        valores_portafolio = pd.Series([29000, 34500], index=[pd.Timestamp('2021-01-01'), pd.Timestamp('2021-02-01')])
        precios_eth = pd.Series([4000, 4500], index=[pd.Timestamp('2021-01-01'), pd.Timestamp('2021-02-01')])
        valores_portafolio_eth = calcular_portafolio_eth(valores_portafolio, precios_eth)
        self.assertEqual(len(valores_portafolio_eth), 2)
        self.assertAlmostEqual(valores_portafolio_eth.iloc[0], 29000)
        self.assertAlmostEqual(valores_portafolio_eth.iloc[1], 32625)

if __name__ == '__main__':
    unittest.main()
