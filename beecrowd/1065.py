numero = 0

for i in range(5):

    valor = int(input())

    if valor % 2 == 0:

        numero += 1

print(f"{numero} valores pares")