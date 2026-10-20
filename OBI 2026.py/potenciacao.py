def potencia(number,potencia):
    number = number
    number = number**potencia
    print(f"{number:.4f}")

numero,potencia_desejada = input("").split(" ")
numero,potencia_desejada = float(numero), float(potencia_desejada)
potencia(numero,potencia_desejada)