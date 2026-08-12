lista = []

while True:
    t = int(input("Digite a temperatura (999 para encerrar):"))

    if t == 999:
        break

    elif t > 20 and t < 50:
        lista.append(t)

media = sum(lista)/len(lista)

print("")
print("Temperaturas válidas:")
for i in lista:
    print(i)
print("")
print("Média das temperaturas:", media)