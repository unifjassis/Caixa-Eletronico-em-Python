import unittest
from models.conta import Conta

class TestConta(unittest.TestCase):
    def test_deposito(self):
        conta = Conta("001", "João", "123")
        conta.depositar(100)
        self.assertEqual(conta.saldo, 100)

    def test_saque_valido(self):
        conta = Conta("001", "João", "123", saldo=200)
        sucesso = conta.sacar(100)
        self.assertTrue(sucesso)
        self.assertEqual(conta.saldo, 100)

    def test_saque_invalido(self):
        conta = Conta("001", "João", "123", saldo=50)
        sucesso = conta.sacar(100)
        self.assertFalse(sucesso)
        self.assertEqual(conta.saldo, 50)

    def test_extrato_apos_operacoes(self):
        conta = Conta("001", "João", "123")
        conta.depositar(150)
        conta.sacar(50)
        extrato = conta.mostrar_extrato()
        self.assertIn("Depósito", extrato[0])
        self.assertIn("Saque", extrato[1])

if __name__ == '__main__':
    unittest.main()