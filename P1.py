# importar biblioteca de deletar arquivos, data e hora
import os
from datetime import datetime

def insereNoExtrato(cpf, transacao, valor, tarifa, saldo):
    arquivo = open("%s_extrato.txt" % cpf, "r")
    operacoes = []
    for procedimento in arquivo.readlines():
        operacoes.append(procedimento)  #Adidiona no array a operação
    arquivo.close()

    novaOperacao = []

    data_e_hora_atuais = datetime.now()  #Para pegar o momento exato
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")  #Para exibir data e hora da operação
    novaOperacao.append("Data: " + data_e_hora_em_texto)
    novaOperacao.append(transacao);
    novaOperacao.append(str(valor) + ' ')  # Valor alterado do saldo
    novaOperacao.append("Tarifa: " + str(tarifa) + ' ')  # Tarifa da operação
    novaOperacao.append("Saldo: " + str(saldo) + "\n")  # Saldo pós-operação
    operacoes.append(novaOperacao)

    arquivo = open("%s_extrato.txt" % cpf, "w")  # Seleciona o arquivo extrato do cliente
    if len(operacoes) <= 1:  # Se o tamanho do array retornado for menor ou igual a 1 ele sobreescreve tudo
        for operacao in operacoes:
            arquivo.write("%s " % operacao)
        arquivo.close()
        return

    # Senao, ele tem que escrever cada propriedade de cada operação, pois vai retornar uma lista de listas
    for operacao in operacoes:
        for propriedade in operacao:
            arquivo.write("%s" % propriedade)
    arquivo.close()
    return

def cadastro():
    cpf = input("Cpf: ")

    # CASO O USUARIO EXISTA ELE VOLTA AO MENU:
    if os.path.isfile('%s.txt' % cpf):
        print()
        print('>>> Usuario ja existe <<<')

    else:
        nome = str(input("Nome: "))
        print("Existe 3 tipos de conta: Salario, Comum e Plus.")
        conta = str(input("Conta: "))
        senha = int(input("Senha numerica: "))
        saldo = float(input("Valor inicial na conta obrigatorio: "))

        # Criando arquivo no modo escrita com o titulo do cpf digitado usando marcadores
        arquivo = open("%s.txt" %cpf, "w")

        # Escrevendo no arquivo os dados do cadastro com marcadores e quebra de linha
        arquivo.write("Nome: %s\nCpf: %s\nConta: %s\nSenha: %d\nSaldo: %.2f"
                      %(nome, cpf, conta, senha, saldo))
        # fechando o arquivo
        arquivo.close()

        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
        valor = 0

        extrato = ("Data: %s + %.2f Tarifa: 0.00 Saldo: %.1f\n" %(data_e_hora_em_texto, valor, saldo))

        arquivo = open("%s_extrato.txt" %cpf, "w")

        arquivo.write(extrato)
        # fechando o arquivo
        arquivo.close()

        print()
        print(">>> Conta Criada <<<")


def delete():
    cpf = input("Qual o CPF que você deseja excluir: ")

    # Puxa pelo cpf a conta, caso exista sera deletada com o os.remove
    if os.path.isfile('%s.txt' % cpf) and os.path.isfile('%s_extrato.txt' %cpf):
        os.remove("%s.txt" %cpf)
        os.remove("%s_extrato.txt" %cpf)
        print()
        print(">>> Conta Deletada <<<")

    else:
        print('>>> A conta não existe! <<<')


def sacar():
    cpf = input("Digite  o CPF da conta: ")

    if os.path.isfile('%s.txt' % cpf):
        arquivo = open("%s.txt" % cpf, "r")

        linhas = []

        # coloca o conteudo do arquivo em uma lista de linhas,
        # entao divide os elementos separados por espaço
        for linha in arquivo.readlines():
            linha_separada = linha.split(" ")
            linhas.append(linha_separada)

        senha = int(input("Qual a senha: "))

        # compara se a senha digitada é igual a do arquivo
        if int(linhas[3][1]) == senha:

            nome = linhas[0][1]
            cpf = linhas[1][1].strip()
            conta = str(linhas[2][1]).strip()
            senha = int(linhas[3][1])
            saldo = float(linhas[4][1])

            print()
            print(" >>> Saldo atual: %.2f <<<" %saldo)
            print()
            valor = float(input("Quanto voce deseja sacar: "))

            # Verificação do tipo de conta se é salario, comum ou plus!
            if conta == "salario" or conta == "salário" or conta == "Salário" or conta == "Salario":

                taxa = ("Taxa de 5% para debitos")
                saldo_novo = saldo - (valor * 1.05)

                # Verificação de saldo negativo. Nesse caso nao pode ser negativo
                if saldo_novo <= 0:
                    print(">>> Não permitido saldo negativo! <<<")

                else:
                    arquivo = open("%s.txt" % cpf, "w")
                    arquivo.write("Nome: %sCpf: %s\nConta: %s\nSenha: %s\nSaldo: %.2f"
                              %(nome, cpf, conta, senha, saldo_novo))

                    print()
                    print(taxa)
                    print(">>> Novo saldo: %.2f <<<" % saldo_novo)

                    arquivo.close()
                    insereNoExtrato(cpf, ' - ', valor, (valor * 0.05), saldo_novo)

            elif conta == "comum" or conta == "Comum":
                taxa = ("Taxa de 3% para debitos")
                saldo_novo = saldo - (valor * 1.03)

                # Verificação de saldo negativo. Nesse caso apenas 500 reais negativos
                if saldo_novo <= -500:
                    print(">>> Não permitido saldo negativo! <<<")

                else:
                    arquivo = open("%s.txt" % cpf, "w")
                    arquivo.write("Nome: %sCpf: %s\nConta: %s\nSenha: %s\nSaldo: %.2f"
                              %(nome, cpf, conta, senha, saldo_novo))

                    print()
                    print(taxa)
                    print(">>> Novo saldo: %.2f <<<" % saldo_novo)
                    insereNoExtrato(cpf, ' - ', valor, (valor * 0.03), saldo_novo)

            elif conta == "plus" or conta == "Plus":
                taxa = ("Taxa de 1% para debitos")
                saldo_novo = saldo - (valor * 1.01)

                # Verificação de saldo negativo. Nesse caso até 5000 negativo da conta plus
                if saldo_novo <= -5000:
                    print(">>> Não permitido saldo negativo! <<<")

                else:
                    arquivo = open("%s.txt" % cpf, "w")
                    arquivo.write("Nome: %sCpf: %s\nConta: %s\nSenha: %s\nSaldo: %.2f"
                              %(nome, cpf, conta, senha, saldo_novo))

                    print()
                    print(taxa)
                    print(">>> Novo saldo: %.2f <<<" % saldo_novo)
                    arquivo.close()
                    insereNoExtrato(cpf, ' - ', valor, (valor * 0.01), saldo_novo)

            else:
                print(">>> Erro inesperado! <<<")


        else:
            print(">>> Senha Incorreta! <<<")

    else:
        print()
        print(">>> Conta não existe! <<<")


def depositar():
    cpf = input("Digite  o CPF da conta: ")

    if os.path.isfile('%s.txt' % cpf):
        arquivo = open("%s.txt" % cpf, "r")

        linhas = []

        for linha in arquivo.readlines():
            linha_separada = linha.split(" ")
            linhas.append(linha_separada)

        senha = int(input("Qual a senha: "))

        if int(linhas[3][1]) == senha:

            nome = linhas[0][1]
            cpf = linhas[1][1].strip()
            conta = linhas[2][1]
            senha = int(linhas[3][1])

            valor = float(input("Quanto deseja depositar: "))
            saldo = float(linhas[4][1]) + valor

            arquivo = open("%s.txt" % cpf, "w")
            arquivo.write("Nome: %sCpf: %s\nConta: %sSenha: %d\nSaldo: %.2f"
                          %(nome, cpf, conta, senha, saldo))
            arquivo.close()

            insereNoExtrato(cpf, ' + ', valor, 0.00, saldo)

            print()
            print(">>> Novo saldo: %.2f <<<" %saldo)

        else:
            print()
            print(">>> Senha Incorreta! <<<")

    else:
        print()
        print(">>> Conta não existe! <<<")


def extrato():
    cpf = input("Cpf: ")

    if os.path.isfile('%s_extrato.txt' %cpf):

        arquivo = open("%s_extrato.txt" % cpf, "r")

        linhas = []

        for linha in arquivo.readlines():
            linhas.append(linha)

        for operacao in linhas:
            print("\n%s " % operacao.strip())

        arquivo.close()

    else:
        print()
        print(">>> Erro inesperado! <<<")


def saldo():
    cpf = input("Digite  o CPF da conta: ")

    if os.path.isfile('%s.txt' % cpf):
        arquivo = open("%s.txt" % cpf, "r")

        linhas = []

        for linha in arquivo.readlines():
            linha_separada = linha.split(" ")
            linhas.append(linha_separada)

        senha = int(input("Qual a senha: "))

        if int(linhas[3][1]) == senha:
            print()
            print(">>> Saldo: %s <<<" % linhas[4][1])
            arquivo.close()

        else:
            print()
            print(">>> Senha incorreta! <<<")

    else:
        print()
        print(">>> Conta nao existe! <<<")


# para voltar ao menu depois de utilizar qualquer uma das opções
while True:

    # opções de uso
    print("1 - Cadastrar Conta")
    print("2 - Deletar Conta")
    print("3 - Sacar")
    print("4 - Depositar")
    print("5 - Extrato")
    print("6 - Saldo")
    print()
    print("0 - Sair")
    print()

    # entrada da opção
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        print()
        print(">>> Programa finalizado! <<<")
        # Sair do programa
        break

    elif opcao == 1:
        cadastro()
        print()

    elif opcao == 2:
        delete()
        print()

    elif opcao == 3:
        sacar()
        print()

    elif opcao == 4:
        depositar()
        print()

    elif opcao == 5:
        extrato()
        print()

    elif opcao == 6:
        saldo()
        print()