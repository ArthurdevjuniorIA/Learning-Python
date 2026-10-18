def multiplicar(a,b):
    resultado = a * b
    return abs(resultado)

print(multiplicar(-10,2))

def any(iterable):
    for elemento in iterable:
        if elemento:
            return True
    return False

def verificacao_de_tipo(number):
    if isinstance(number,float):
        print("é inteiro")
    else:
        return isinstance(number,float)
print(verificacao_de_tipo(12))