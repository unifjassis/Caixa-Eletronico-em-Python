from services.persistencia import salvar_conta

def sacar(conta, valor):
    if conta.sacar(valor):
        salvar_conta(conta)
        return True
    return False

def depositar(conta, valor):
    conta.depositar(valor)
    salvar_conta(conta)

def transferir(conta_origem, conta_destino, valor):
    if conta_origem.sacar(valor):
        conta_origem.extrato.append(
            f"Transferência enviada para {conta_destino.numero}: -R${valor:.2f}"
        )
        conta_destino.depositar(valor)
        conta_destino.extrato.append(
            f"Transferência recebida de {conta_origem.numero}: +R${valor:.2f}"
        )
        salvar_conta(conta_origem)
        salvar_conta(conta_destino)
        return True
    return False
