import unittest
from models.conta import Conta
from services.operacoes import depositar, sacar, transferir

class TestOperacoes(unittest.TestCase):
    def test_depositar(self):
        conta = Conta("002", "Maria", "abc")
        depositar(conta, 300)
        self.assertEqual(conta.saldo, 300)

    def test_sacar_valido(self):
        conta = Conta("002", "Maria", "abc", saldo=500)
        sucesso = sacar(conta, 200)
        self.assertTrue(sucesso)
        self.assertEqual(conta.saldo, 300)

    def test_sacar_invalido(self):
        conta = Conta("002", "Maria", "abc", saldo=100)
        sucesso = sacar(conta, 150)
        self.assertFalse(sucesso)
        self.assertEqual(conta.saldo, 100)

    def test_transferencia(self):
        origem = Conta("003", "Carlos", "senha", saldo=400)
        destino = Conta("004", "Ana", "senha")
        sucesso = transferir(origem, destino, 200)
        self.assertTrue(sucesso)
        self.assertEqual(origem.saldo, 200)
        self.assertEqual(destino.saldo, 200)

if __name__ == '__main__':
    unittest.main()