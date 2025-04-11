class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular, senha):
        if numero in self.contas:
            return False  # Conta já existe
        from models.conta import Conta
        self.contas[numero] = Conta(numero, titular, senha)
        return True

    def autenticar(self, numero, senha):
        conta = self.contas.get(numero)
        if conta and conta.senha == senha:
            return conta
        return None
