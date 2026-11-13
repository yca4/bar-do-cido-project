import os

def carregar_cardapio():
    cardapio = {}
    if os.path.exists("dados/cardapio.txt"):
        arquivo = open("dados/cardapio.txt", "r", encoding="utf-8")
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 3:
                codigo = dados[0]
                nome = dados[1]
                preco = float(dados[2])
                cardapio[codigo] = {"nome": nome, "preco": preco}
        arquivo.close()
    return cardapio

def cadastrar_produto():
    cardapio = carregar_cardapio()
    print("\n--- CADASTRO DE PRODUTO ---")
    codigo = input("Digite o código do produto: ").strip()
    if codigo in cardapio:
        print("Erro: Já existe um produto com este código!")
        return
    nome = input("Digite o nome do produto: ").strip()
    preco_str = input("Digite o preço unitário (ex: 8.50): ").strip()
    preco = float(preco_str)
    
    arquivo = open("dados/cardapio.txt", "a", encoding="utf-8")
    arquivo.write(f"{codigo};{nome};{preco:.2f}\n")
    arquivo.close()
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_cardapio():
    cardapio = carregar_cardapio()
    print("\n================ CARDÁPIO - ESPETINHO DO CIDO ================")
    if not cardapio:
        print("Nenhum produto cadastrado no momento.")
        print("==============================================================")
        return False
    print(f"{'CÓDIGO':<10} | {'PRODUTO':<30} | {'PREÇO (R$)':>12}")
    print("-" * 58)
    for codigo, info in cardapio.items():
        print(f"{codigo:<10} | {info['nome']:<30} | {info['preco']:>12.2f}")
    print("==============================================================")
    return True
