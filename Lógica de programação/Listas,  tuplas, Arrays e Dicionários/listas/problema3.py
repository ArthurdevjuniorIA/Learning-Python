devolveu_toalha = [ ]
retirou_toalha = [ ]
nome_atleta = [ ]
while True:
    print("1 - Retirar toalha\n2 - Devolver toalha\n0 - Encerrar")
    opcao = int(input("Opção: "))
    if opcao == 0:
        print("===== RELATÓRIO =====")
        print("Atletas que devolveram a toalha: ")
        for devolveu in devolveu_toalha:
            print(f"-{devolveu}")
        print("Atletas que ainda estão com toalha: ")
        for retirou in retirou_toalha:
            print(f"-{retirou}")
        break

    elif opcao == 1:
        nome = input("Nome do atleta: ")
        if nome not in retirou_toalha:
             nome_atleta.append(nome)
             retirou_toalha.append(nome)
             print("Toalha entregue")
        else:
            print("Você já retirou uma toalha hoje!")
    elif opcao == 2:
        nome = input("Nome do atleta: ")
        devolveu_toalha.append(nome)
        if nome in retirou_toalha:
            retirou_toalha.remove(nome)
        print("Devolução registrada")