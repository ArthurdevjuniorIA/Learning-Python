listatags = []
nomes = []

entrada = input("Informe as tags das provas:")
tags = entrada.split()
listatags.append(tags)

while True:
    entrada2 = input("Registro (TAG NOME ou FIM):")
    tags, nome = entrada2.split()

    if nome == "FIM":
        break
    else:
        if tags not in listatags:
            print("Tag de Prova inválida.")
        else:
            nomes.append(nome)

print("===== RELATÓRIO FINAL =====")
print("")
for tags, nome in listatags,nomes: 
    print(tags, nome)