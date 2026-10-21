recordes = [ ]
melhor_marca = 10.50
print("Melhor marca atual: ", melhor_marca)
while True:
    nome_competidor = input("Nome do competidor: ")
    if nome_competidor == "fim":
            for i in range(len(recordes)):
                for recorde in recordes[i]:
                    print(recorde)
            break
    marca_competidor = float(input("Marca obtida: "))
    
    if marca_competidor < melhor_marca:
        print("NOVO RECORDE!")
        nome_marca_competidor = [ nome_competidor,"-", marca_competidor]
        recordes.append(nome_marca_competidor)
    else:
        print("Não quebrou o recorde")