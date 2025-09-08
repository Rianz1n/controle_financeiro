import json
import os
from datetime import datetime
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Pasta e arquivo onde serão salvos todos os JSON
PASTA_DADOS = "data"
ARQUIVO = os.path.join(PASTA_DADOS, "transacoes.json")

# Criar pasta "data" se não existir
if not os.path.exists(PASTA_DADOS):
    os.makedirs(PASTA_DADOS)

# Carregar transações do arquivo (se existir)
def carregar_transacoes():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salvar transações no arquivo
def salvar_transacoes(transacoes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(transacoes, f, ensure_ascii=False, indent=4)

# Lista para guardar transações
transacoes = carregar_transacoes()

# Registrar ganho ou gasto
# Registrar ganho ou gasto
def registrar_transacao(tipo):
    descricao = input("Descrição: ")

    # Validação de valor numérico
    while True:
        valor = input("Valor (use ponto para centavos, ex: 25.50): ")
        try:
            valor = float(valor)
            break
        except ValueError:
            print(Fore.RED + "❌ Valor inválido! Digite apenas números. Ex: 25.50")

    # Ajusta sinal (positivo = ganho | negativo = gasto)
    if tipo == "gasto":
        valor = -abs(valor)
    else:
        valor = abs(valor)

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    transacoes.append({
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor,
        "data": data_hora
    })

    salvar_transacoes(transacoes)
    print(Fore.GREEN + "✅ Transação registrada com sucesso!")
    print(Fore.RED + "⚠️ Valor inválido! Digite apenas números.\n")

# Mostrar histórico com cores
def mostrar_transacoes():
    if not transacoes:
        print("\n📌 Nenhuma transação registrada.\n")
        return
    print("\n📜 Histórico de Transações:")
    for t in transacoes:
        cor = Fore.GREEN if t['valor'] > 0 else Fore.RED
        print(f"- {t['tipo'].upper():6} | {t['descricao']:20} | {cor}R$ {t['valor']:.2f}{Style.RESET_ALL} | {t['data_hora']}")
    print()

# Mostrar saldo com cor
def mostrar_saldo():
    saldo = sum(t["valor"] for t in transacoes)
    cor = Fore.GREEN if saldo >= 0 else Fore.RED
    print(f"\n💰 Saldo atual: {cor}R$ {saldo:.2f}{Style.RESET_ALL}\n")

# Menu principal
def menu():
    while True:
        print("=== CONTROLE FINANCEIRO ===")
        print("1️⃣ Registrar ganho")
        print("2️⃣ Registrar gasto")
        print("3️⃣ Ver histórico")
        print("4️⃣ Ver saldo")
        print("5️⃣ Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_transacao("ganho")
        elif opcao == "2":
            registrar_transacao("gasto")
        elif opcao == "3":
            mostrar_transacoes()
        elif opcao == "4":
            mostrar_saldo()
        elif opcao == "5":
            print("📌 Programa encerrado. Até mais!")
            break
        else:
            print(Fore.RED + "⚠️ Opção inválida! Escolha de 1 a 5.\n")

# Rodar programa
if __name__ == "__main__":
    menu()
