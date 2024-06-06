import unittest
from data.portafolio import obtener_portafolio

class TestPortafolio(unittest.TestCase):
    def test_obtener_portafolio(self):
        portafolio = obtener_portafolio()
        self.assertEqual(portafolio['ETH'], 1)
        self.assertEqual(portafolio['SOL'], 5)
        self.assertEqual(portafolio['SHIB'], 10)
        self.assertEqual(portafolio['PEPE'], 15)

if __name__ == '__main__':
    unittest.main()
