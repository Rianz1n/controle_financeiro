# 💰 Controle Financeiro  

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)]()  

Um sistema simples em **Python** para controle de finanças pessoais.  
Permite registrar ganhos e gastos, visualizar histórico e consultar o saldo atual.  
Todos os dados são armazenados automaticamente em um arquivo JSON.  

---

## 🚀 Funcionalidades
- 📥 Registrar ganhos  
- 📤 Registrar gastos  
- 📜 Visualizar histórico de transações  
- 💵 Consultar saldo atual  
- 💾 Dados salvos em JSON automaticamente  

---

## 🛠️ Tecnologias utilizadas
- [Python 3.11+](https://www.python.org/)  
- [Colorama](https://pypi.org/project/colorama/) → saída colorida no terminal  
- JSON → armazenamento dos dados  

---

## 📂 Estrutura do projeto
controle_financeiro/
│── financas/ # Pasta onde ficam os arquivos de dados
│ └── transacoes.json # Transações salvas
│── main/
│ └── financas.py # Código principal
│── README.md # Documentação do projeto
│── requirements.txt # Dependências
│── .gitignore # Arquivos a serem ignorados no Git