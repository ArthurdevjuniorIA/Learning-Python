lista = []

for i in range(1, 11):
    nome = input(f"Informe o nome do {i}º colocado:")

    lista.append(nome)

while True:
    consulta = input("Digite o nome do candidato para consulta (ou 'fim' para encerrar):")

    if consulta.strip().lower() == "fim":
        print("Programa encerrado.")
        break

    if consulta in lista:
        print(f"{consulta} está na {lista.index(consulta) + 1}ª posição.")