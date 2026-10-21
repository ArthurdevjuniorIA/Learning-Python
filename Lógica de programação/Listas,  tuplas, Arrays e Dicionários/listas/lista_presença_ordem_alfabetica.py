nome_participantes = [ ]
i= 0
while True:
    nome_de_um_participante = input("Digite seu nome: ")
    if nome_de_um_participante == "fim":
        print("=== LISTA DE PRESENÇA ===")
        for posicao in nome_participantes:
            i = i+1
            print(f"{i}-{nome_participantes}")
        break
    else:
        nome_participantes.append(nome_de_um_participante)
        nome_participantes.sort()