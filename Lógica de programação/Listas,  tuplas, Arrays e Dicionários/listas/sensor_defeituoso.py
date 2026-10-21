temperaturas_validas = [ ]
soma = 0
while True:
    temperatura = float(input("Digite a temperatura (999 para encerrar): "))
    if temperatura == 999:
        for i in range(len(temperaturas_validas)):
            some = temperaturas_validas[i]
            soma = some + soma
        divide = soma/len(temperaturas_validas)
        print("Temperaturas válidas: ")
        for valido in temperaturas_validas:
            print(valido)
        print(f"Média das temperaturas: {divide:.2f}°C")
        break
    else:
        if temperatura>50 or temperatura<-20:
            continue
        temperaturas_validas.append(temperatura)
    
