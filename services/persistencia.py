import os
import json
from models.conta import Conta
from utils.criptografia import criptografar, descriptografar

DATA_DIR = "data"

def salvar_conta(conta: Conta):
    """Salva os dados da conta em um arquivo criptografado."""
    caminho = os.path.join(DATA_DIR, f"conta_{conta.numero}.txt")
    dados = {
        "numero": conta.numero,
        "titular": conta.titular,
        "senha": conta.senha,
        "saldo": conta.saldo,
        "extrato": conta.extrato
    }
    texto_json = json.dumps(dados, indent=4)
    texto_criptografado = criptografar(texto_json)
    with open(caminho, "w") as f:
        f.write(texto_criptografado)

def carregar_contas():
    """Carrega todas as contas da pasta data a partir de arquivos criptografados."""
    contas = {}
    for nome_arquivo in os.listdir(DATA_DIR):
        if nome_arquivo.startswith("conta_") and nome_arquivo.endswith(".txt"):
            caminho = os.path.join(DATA_DIR, nome_arquivo)
            with open(caminho, "r") as f:
                texto_criptografado = f.read()
                texto_json = descriptografar(texto_criptografado)
                dados = json.loads(texto_json)
                conta = Conta(
                    numero=dados["numero"],
                    titular=dados["titular"],
                    senha=dados["senha"],
                    saldo=dados["saldo"]
                )
                conta.extrato = dados.get("extrato", [])
                contas[conta.numero] = conta
    return contas