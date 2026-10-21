# Problema1
melhores_marcas = [ ]
while True:
    marca_obtida = float(input("Marca obtida (0 para encerrar): "))
    if marca_obtida == 0:
        print("===== 10 MELHORES MARCAS =====")
        for i in range(len(melhores_marcas)):
            print(f"{i+1}º {melhores_marcas[0+i]}")
            if i>10:
                break
        break
    else:
        melhores_marcas.append(marca_obtida)
        melhores_marcas.sort(reverse = True)
        print(melhores_marcas)
# Problema2

bolas = [ ]
while True:
    cor_bolinha = input("Cor da bolinha (ou FIM): ")
    if cor_bolinha == "FIM":
        print("===== INVENTÁRIO =====")
        for cor in bolas:
            print(cor)
        break
    else:
        bolas.append(cor_bolinha)
        
#Problema3
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
        nome_atleta.append(nome)
        retirou_toalha.append(nome)
        print("Toalha entregue")
    elif opcao == 2:
        nome = input("Nome do atleta: ")
        devolveu_toalha.append(nome)
        print("Devolução registrada")