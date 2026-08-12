lista = []


while True:
    nome = input("Nome do voluntário (ou 'fim' para encerrar):")


    if nome.strip().lower() == "fim":
        break
    lista.append(nome)


print("=== EQUIPES FORMADAS ===")
print("")
print("Equipe 1")
for nome in lista[0:3]:
    print("-", nome)
print("")
print("Equipe 2")
for nome in lista[3:6]: 
    print("-", nome)
print("")
print("Equipe 3")
for nome in lista[6:]:
    print("-", nome)



