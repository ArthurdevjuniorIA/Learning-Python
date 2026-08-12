lista = []

while True:
    nome = input("Nome do participante (ou 'fim' para encerrar):")
    #.strip() e .lower() ignoram se a palavra digitada tiver espaços a mais ou se estiver maiúscula ou não.
    if nome.strip().lower() == "fim":
        break
    else:
        lista.append(nome)
        ordenada = sorted(lista)

print("")
print("=== LISTA DE PRESENÇA ===")
for i, nome in enumerate(ordenada, start = 1):
    print(f"{i} - {nome}")