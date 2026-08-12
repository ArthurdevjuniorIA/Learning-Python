# 2. Consultar nadadores
codigos = []
nomes = []
quantidades = []
toalhas_disponiveis = 30
while True:
    print("=================================")
    print(" NADO LIVRE")
    print("=================================\n")
    print("1 - Cadastrar nadador")
    print("2 - Consultar nadadores")
    print("3 - Registrar retirada de toalhas")
    print("4 - Consultar toalhas em uso")
    print("0 - Sair\n")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("===== CADASTRO DE NADADOR =====\n")
        cod_input = int(input("Código: "))
        nome_input = input("Nome: ")

        # Validação: verifica se o código é número e se o nome não está vazio
        if nome_input.strip() != "":
            codigos.append(cod_input)
            nomes.append(nome_input)
            print("\nNadador cadastrado com sucesso!\n")
        else:
            print("Dados inválidos! Tente novamente.\n")

    elif opcao == 2:
        print("\n========= NADADORES =========")
        if len(codigos) > 0:
            for i in range(len(codigos)):
                print(f"{codigos[i]} - {nomes[i]}")
            print("")
        else:
            print("Nenhum nadador cadastrado.\n")
    elif opcao == 3:
        cod_input = int(input("Código: "))
        quantidade = int(input("Quantidade: "))
        toalhas_disponiveis = toalhas_disponiveis - quantidade
        print("Retirada registrada com sucesso!")
        print(f"Toalhas disponiveis: {toalhas_disponiveis}")

    elif opcao == 0:
        print("Saindo do sistema...")
        break