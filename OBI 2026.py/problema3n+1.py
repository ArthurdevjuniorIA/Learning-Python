def collatz(numero):
    quantas_vezes = 0
    while True:
        if numero == 1:
            return quantas_vezes
        
        else:
            if numero % 2 == 0:
                numero = numero//2
            else:
                numero = (3*numero)+1
            
            quantas_vezes +=1
            continue

n = int(input())
total_vezes = collatz(n)
print(total_vezes)