from models.banco import Banco

def menu():
    print("\n===== Caixa Eletrônico =====")
    print("1. Criar conta")
    print("2. Entrar")
    print("3. Sair")
    return input("Escolha uma opção: ")

def menu_conta(conta):
    while True:
        print(f"\nBem-vindo(a), {conta.titular}!")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Extrato")
        print("5. Sair da conta")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Saldo atual: R${conta.saldo:.2f}")
        elif opcao == "2":
            valor = float(input("Valor para depósito: R$"))
            conta.depositar(valor)
            print("Depósito realizado com sucesso!")
        elif opcao == "3":
            valor = float(input("Valor para saque: R$"))
            if conta.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        elif opcao == "4":
            print("Extrato:")
            for mov in conta.mostrar_extrato():
                print("-", mov)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

def main():
    banco = Banco()

    while True:
        opcao = menu()
        if opcao == "1":
            numero = input("Número da nova conta: ")
            titular = input("Nome do titular: ")
            senha = input("Senha: ")
            if banco.criar_conta(numero, titular, senha):
                print("Conta criada com sucesso!")
            else:
                print("Conta já existe.")
        elif opcao == "2":
            numero = input("Número da conta: ")
            senha = input("Senha: ")
            conta = banco.autenticar(numero, senha)
            if conta:
                menu_conta(conta)
            else:
                print("Dados inválidos.")
        elif opcao == "3":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
