import os
from cardapio import cadastrar_produto, listar_cardapio
from comandas import abrir_mesa, adicionar_item, fechar_conta
from relatorios import exibir_faturamento

os.makedirs("dados", exist_ok=True)

mesas = {}

while True:
    print("\n=== ESPETINHO DO CIDO - SISTEMA DE GESTÃO ===")
    print("1. Cadastrar Produto no Cardápio")
    print("2. Listar Cardápio")
    print("3. Abrir Mesa")
    print("4. Adicionar Item na Mesa")
    print("5. Fechar Conta da Mesa")
    print("6. Relatório de Faturamento")
    print("0. Sair do Sistema")
    print("==============================================")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            cadastrar_produto()
        case "2":
            listar_cardapio()
        case "3":
            abrir_mesa(mesas)
        case "4":
            adicionar_item(mesas)
        case "5":
            fechar_conta(mesas)
        case "6":
            exibir_faturamento()
        case "0":
            print("Encerrando o sistema do Espetinho do Cido. Até logo!")
            break
        case _:
            print("Opção inválida! Por favor, tente novamente.")
