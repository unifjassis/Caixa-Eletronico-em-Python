from models.banco import Banco
from services.persistencia import salvar_conta, carregar_contas
from services.operacoes import sacar, depositar, transferir
import os

def menu():
    print("\n===== Caixa Eletrônico =====")
    print("1. Criar conta")
    print("2. Entrar")
    print("3. Sair")
    return input("Escolha uma opção: ")

def menu_conta(conta, banco):
    while True:
        print(f"\nBem-vindo(a), {conta.titular}!")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Extrato")
        print("5. Transferir")
        print("6. Encerrar conta")
        print("7. Sair da conta")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Saldo atual: R${conta.saldo:.2f}")
        elif opcao == "2":
            valor = float(input("Valor para depósito: R$"))
            depositar(conta, valor)
            print("Depósito realizado com sucesso!")
        elif opcao == "3":
            valor = float(input("Valor para saque: R$"))
            if sacar(conta, valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        elif opcao == "4":
            print("Extrato:")
            for mov in conta.mostrar_extrato():
                print("-", mov)
        elif opcao == "5":
            destino = input("Número da conta destino: ")
            if destino == conta.numero:
                print("Não é possível transferir para a mesma conta.")
                continue
            if destino in banco.contas:
                valor = float(input("Valor da transferência: R$"))
                if transferir(conta, banco.contas[destino], valor):
                    print("Transferência realizada com sucesso!")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Conta destino não encontrada.")
        elif opcao == "6":
            if conta.saldo == 0:
                confirm = input("Tem certeza que deseja encerrar a conta? (s/n): ")
                if confirm.lower() == "s":
                    del banco.contas[conta.numero]
                    caminho = os.path.join("data", f"conta_{conta.numero}.txt")
                    if os.path.exists(caminho):
                        os.remove(caminho)
                    print("Conta encerrada com sucesso!")
                    break
                else:
                    print("Encerramento cancelado.")
            else:
                print("Conta só pode ser encerrada com saldo zero.")
        elif opcao == "7":
            break
        else:
            print("Opção inválida.")

def main():
    banco = Banco()
    banco.contas = carregar_contas()

    while True:
        opcao = menu()
        if opcao == "1":
            numero = input("Número da nova conta: ")
            titular = input("Nome do titular: ")
            senha = input("Senha: ")
            if banco.criar_conta(numero, titular, senha):
                salvar_conta(banco.contas[numero])
                print("Conta criada com sucesso!")
            else:
                print("Conta já existe.")
        elif opcao == "2":
            numero = input("Número da conta: ")
            senha = input("Senha: ")
            conta = banco.autenticar(numero, senha)
            if conta:
                menu_conta(conta, banco)
            else:
                print("Dados inválidos.")
        elif opcao == "3":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
