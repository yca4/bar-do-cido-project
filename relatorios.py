import os

def registrar_venda(mesa, total, itens):
    arquivo = open("dados/vendas.txt", "a", encoding="utf-8")
    linha = f"{mesa};{total:.2f};{len(itens)}\n"
    arquivo.write(linha)
    arquivo.close()

def exibir_faturamento():
    print("\n============= RELATÓRIO DE FATURAMENTO DIÁRIO =============")
    if not os.path.exists("dados/vendas.txt"):
        print("Nenhuma venda registrada ainda no sistema.")
        print("===========================================================")
        return

    arquivo = open("dados/vendas.txt", "r", encoding="utf-8")
    total_faturado = 0.0
    quantidade_comandas = 0

    print(f"{'MESA':<10} | {'QTD ITENS':<12} | {'VALOR (R$)':>12}")
    print("-" * 38)
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 3:
            mesa = dados[0]
            valor = float(dados[1])
            qtd_itens = dados[2]
            total_faturado += valor
            quantidade_comandas += 1
            print(f"{mesa:<10} | {qtd_itens:<12} | {valor:>12.2f}")
    arquivo.close()

    print("-" * 38)
    print(f"Total de comandas fechadas: {quantidade_comandas}")
    print(f"FATURAMENTO TOTAL DO DIA: R$ {total_faturado:.2f}")
    print("===========================================================")
