from unittest import TestCase
from laboratorio_7.Cuenta import Cuenta

class TestCuenta(TestCase):
    def test_deposito(self):
        c=Cuenta()
        self.assertLess(c.deposito(1000), 600)


    def test_retiro(self):
        c=Cuenta()
        self.assertEqual(c.retiro(1000), 500)
