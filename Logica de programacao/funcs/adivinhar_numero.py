from random import randint as aleatorio
def validando_numero(numero_tentado):
    try:
        numero_tentado
    
    except ValueError or TypeError:
        print("Digite apenas números")
        return None

    if numero_tentado not in range(1,101):
        raise ValueError("Digite apenas números de 1 a 100")
    
def adivinhe_numero():
    numero_aleatorio = aleatorio(1,100)
    tentativas = 0
    while True:
        
        numero_chute = int(input("Tente adivinhar o número de 0 a 100: "))
        valido = validando_numero(numero_chute)
        if valido is None:
            continue
        

        if numero_chute>numero_aleatorio:
            print("Muito alto!")
            tentativas+=1
            continue
        
        elif numero_chute<numero_aleatorio:
            print("Muito baixo!")
            tentativas+=1
            continue
        
        else:
            print(f"Parabéns você acertou o número {numero_aleatorio}com {tentativas} tentativas")
            break



resultado = adivinhe_numero()

    
