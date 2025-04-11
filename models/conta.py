class Conta:
    def __init__(self, numero, titular, senha, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: +R${valor:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f}")
            return True
        return False

    def mostrar_extrato(self):
        return self.extrato
