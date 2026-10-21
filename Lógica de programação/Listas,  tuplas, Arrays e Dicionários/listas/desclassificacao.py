candidatos = [ ]
for i in range(0,10):
    candidatando = input(f"Informe o nome do {i+1}º colocado: ")
    candidatos.append(candidatando)
while True:
    nome = input()
    if nome == "fim":
        break
    '''for i in range(len(candidatos)):
        if candidatos[i] == nome:
            candidatos[i] = "(DESCLASSIFICADO)"
            break
    i = candidatos.index(nome)'''
    if nome in candidatos:
        candidatos[i] = "(DESCLASSIFICADO)"
print("=== CLASSIFICAÇÃO ATUALIZADA ===")
for i,nome in enumerate(candidatos,start=1):
    print(f"{i}° lugar: {nome}")