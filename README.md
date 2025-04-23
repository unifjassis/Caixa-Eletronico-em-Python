# 🏦 Sistema de Caixa Eletrônico em Python

Simulação de um sistema de caixa eletrônico (ATM) com autenticação, transações bancárias, armazenamento seguro e testes automatizados. Projeto desenvolvido com foco em boas práticas de programação, modularização e documentação.

---

## ✅ Funcionalidades

- Criar e encerrar contas
- Autenticação por número e senha
- Saques e depósitos com atualização de saldo
- Transferência entre contas com extrato detalhado
- Emissão de extrato bancário
- Armazenamento de dados por conta em arquivos separados
- Criptografia dos dados com base64
- Testes unitários com `unittest`

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3.x
- `unittest` (testes)
- `json` (serialização)
- `base64` (criptografia simples)
- Estrutura modular (pasta por responsabilidade)

---

## ▶️ Como Rodar o Projeto

1. Clone o repositório:  
git clone https://github.com/unifjassis/Caixa-Eletronico-em-Python.git  
cd Caixa-Eletronico-em-Python

3. Execute o main.py

4. Crie uma conta via terminal.
---

🧪 Como Executar os Testes
Pelo terminal:
```
python -m unittest discover -s tests
```


Ou rode um arquivo específico:
```
python tests/test_conta.py
```

Para exibir os testes individualmente:
```
python -m unittest discover -s tests -v
```
---

📁 Estrutura de Pastas
```
caixa_eletronico/
├── main.py
├── models/
│   ├── conta.py
│   └── banco.py
├── services/
│   ├── operacoes.py
│   └── persistencia.py
├── utils/
│   └── criptografia.py
├── data/
│   └── conta_<numero>.txt
├── tests/
│   ├── test_conta.py
│   └── test_operacoes.py
├── README.md
└── requirements.txt
```
---
```
MIT License

Copyright (c) 2025 [João Assis]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```