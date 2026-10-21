tags= ["corrida", "natacao", "xadrez", "danca"]
nomes_participantes = [ ]
corrida = [ ]
natacao = [ ]
xadrez = [ ]
danca = [ ]
print(*tags)
while True:
    tag_nome = list(map(input("Registro (TAG NOME ou FIM): ").split()))
    if tag_nome == "fim":
        print("===== RELATÓRIO FINAL =====")
        for correr in corrida:
            print(f"-{correr}")
        break
    else:
        if tag_nome[0] not in tags:
            print("Tag de prova inválida")
        else:
            nomes_participantes.append(tag_nome[0])
            if tag_nome[0] == tags[0]:
                corrida.append(tag_nome[1])
            elif tag_nome[0] == tags[1]:
                natacao.append(tag_nome[1])   
            elif tag_nome[0] == tags[2]:
                xadrez.append(tag_nome[1])
            elif tag_nome[0] == tags[3]:
                danca.append(tag_nome[1])

