import unittest
import requests  # Esto es parte de la "compilación" (instalación de dependencias)

# Funciones del software

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

# Pruebas unitarias

class TestFunciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
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
