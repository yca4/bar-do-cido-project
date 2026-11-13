from cardapio import carregar_cardapio, listar_cardapio
from relatorios import registrar_venda

def abrir_mesa(mesas):
    print("\n--- ABRIR MESA / COMANDA ---")
    mesa = input("Digite o número ou identificação da mesa: ").strip()
    if mesa in mesas:
        print(f"Erro: A mesa {mesa} já está aberta!")
    else:
        mesas[mesa] = []
        print(f"Mesa {mesa} aberta com sucesso!")

def adicionar_item(mesas):
    print("\n--- ADICIONAR ITEM NA COMANDA ---")
    mesa = input("Digite o número da mesa: ").strip()
    if mesa not in mesas:
        print(f"Erro: A mesa {mesa} não está aberta!")
        return

    tem_produtos = listar_cardapio()
    if not tem_produtos:
        return

    cardapio = carregar_cardapio()
    codigo = input("Digite o código do produto desejado: ").strip()
    if codigo not in cardapio:
        print("Erro: Produto não encontrado no cardápio!")
        return

    qtd_str = input("Digite a quantidade: ").strip()
    qtd = int(qtd_str)
    if qtd <= 0:
        print("Erro: Quantidade inválida!")
        return

    nome_produto = cardapio[codigo]["nome"]
    preco_unitario = cardapio[codigo]["preco"]
    subtotal = preco_unitario * qtd

    item = [codigo, nome_produto, qtd, preco_unitario, subtotal]
    mesas[mesa].append(item)
    print(f"{qtd}x '{nome_produto}' adicionado(s) à mesa {mesa}!")

def fechar_conta(mesas):
    print("\n--- FECHAMENTO DE CONTA ---")
    mesa = input("Digite o número da mesa a ser fechada: ").strip()
    if mesa not in mesas:
        print(f"Erro: A mesa {mesa} não foi encontrada!")
        return

    itens = mesas[mesa]
    if len(itens) == 0:
        print(f"A mesa {mesa} não possui nenhum consumo registrado.")
        del mesas[mesa]
        print(f"Mesa {mesa} encerrada sem cobrança.")
        return

    print(f"\n================ EXTRATO DA MESA {mesa} ================")
    print(f"{'PRODUTO':<25} | {'QTD':>4} | {'UNIT (R$)':>10} | {'SUBTOTAL':>10}")
    print("-" * 57)

    total_conta = 0.0
    for linha in itens:
        nome = linha[1]
        qtd = linha[2]
        unit = linha[3]
        subtotal = linha[4]
        total_conta += subtotal
        print(f"{nome:<25} | {qtd:>4} | {unit:>10.2f} | {subtotal:>10.2f}")

    print("-" * 57)
    print(f"TOTAL A PAGAR: R$ {total_conta:.2f}")
    print("=========================================================")

    registrar_venda(mesa, total_conta, itens)
    del mesas[mesa]
    print(f"Conta da mesa {mesa} finalizada e venda registrada com sucesso!")
