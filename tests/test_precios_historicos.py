import unittest
from data.precios_historicos import obtener_precios_historicos
import pandas as pd

class TestPreciosHistoricos(unittest.TestCase):
    def test_obtener_precios_historicos(self):
        fechas = pd.date_range(start="2021-01-01", end="2023-12-31", freq='M')
        df_precios_historicos = obtener_precios_historicos(fechas)
        self.assertFalse(df_precios_historicos.empty)
        self.assertTrue('BTC' in df_precios_historicos.columns)

if __name__ == '__main__':
    unittest.main()
