""" soma = lambda a,b : a+b
numero1 = int(input(""))
numero2 = int(input(""))
resultado = soma(numero1,numero2)
print(resultado) """

numeros = [1,2,3,4,5,6,7,8,9,65]
numeros_ao_quadrado = filter(lambda n:n**2>80 ,numeros)
for num in numeros_ao_quadrado:
    print(num)