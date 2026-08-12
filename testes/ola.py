quantidade = 0

numero = int(input("Digite um número (0 para encerrar): "))

while numero != 0:

    quantidade += 1

    numero = int(input("Digite um número (0 para encerrar): "))

print("Quantidade de valores digitados:", quantidade)