primeiros_colocados = [ ]
for i in range(1,11):
    informe = input(f"Informe o nome do {i}º colocado: ")
    primeiros_colocados.append(informe)
while True:
    consulta = int(input("Digite uma posição para consulta (0 para encerrar): "))
    if consulta == 0:
        break
    else:
        for i, _ in enumerate(primeiros_colocados):
            i = i + 1
            for consulta in primeiros_colocados.index():
                print(consulta)


