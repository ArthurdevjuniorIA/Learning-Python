numeros = [1,2,3,4]
numero_adicional = 6
outro_numero = 40
numeros.append(numero_adicional)
numeros.remove(2)
numeros.remove(4)
numeros.insert(3,outro_numero)
numeros.sort(reverse= True)
print(numeros)