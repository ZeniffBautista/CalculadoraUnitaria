# test_app.py
import unittest
from app import suma, resta, multiplicacion

class TestFunciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 3), 6)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(3, 2), 1)
        self.assertEqual(resta(2, 2), 0)
        self.assertEqual(resta(0, 1), -1)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 2), 6)
        self.assertEqual(multiplicacion(4, 0), 0)
        self.assertEqual(multiplicacion(5, -1), -5)

if __name__ == '__main__':
    unittest.main()
