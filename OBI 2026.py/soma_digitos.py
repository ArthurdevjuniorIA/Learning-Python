def soma_digitos(numero):
    numero = str(numero)
    numero = list(numero)
    soma = [int(numeral) for numeral in numero]
    soma_total = sum(soma)
    return soma_total

valor = int(input())
soma_dos_digitos = soma_digitos(valor)
print(soma_dos_digitos)


