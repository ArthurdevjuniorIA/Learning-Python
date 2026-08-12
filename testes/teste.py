soma = 0
quantidade = 0

valor = int(input("Digite o valor que você arrecadou (0 para encerrar):"))

while valor != 0:

    soma += valor
    quantidade += 1

    valor = int(input("Digite o valor que você arrecadou (0 para encerrar): "))

print("Você arrecadou no seu cofre", soma , "reais!")
print(f"Você digitou {quantidade} valores!")

