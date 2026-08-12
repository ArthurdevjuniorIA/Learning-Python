valor = int(input())
valor2 = int(input())
impares = 0 

#Para ele iniciar do "valor" e finalizar no "valor2"  e funcionar com números negativos e positivos, pois não há um intervalo entre inicialmente um número positivo e depois um negativo. O negativo teria que vir primeiro na entrada.
inicio = min(valor, valor2)
fim = max(valor, valor2)   

for i in range (inicio + 1, fim): #não inclui os extremos
     
    
    if i % 2 != 0:
     impares += i 

print(impares)