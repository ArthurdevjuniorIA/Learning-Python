import time
'''
def meu_decorador(func):
    def wrapper():
        print(f"Essa é a função que estou decorando {func.__name__}")

        func()

        print(f"Executei a função {func.__name__}")

    return wrapper

@meu_decorador
def printar_nome():
    print("Meu nome é Arthur")

printar_nome()
'''
# 1. Criamos o decorador (uma função que recebe outra função)
def meu_decorador(funcao_original):
    def embrulho(*args, **kwargs):
        print("[LOG]: Uma operação foi realizada automaticamente.")
        return funcao_original(*args, **kwargs)
    return embrulho

# 2. Aplicamos o decorador usando o @
@meu_decorador
def soma(a, b):
    return a + b

@meu_decorador
def subtracao(a, b):
    return a - b

# Execução: Você só chama a função de matemática, o resto acontece sozinho!
print(soma(5, 5))
print(subtracao(10, 3))

def tempo_decorador(func):
    def wrapper(*args,**kwargs):
        start_tempo = time.time()
        func()
        end_tempo = time.time()
        print(f"O tempo de execução foi de: {end_tempo-start_tempo} segundos")
    return wrapper

@tempo_decorador
def fazer_um_bolo():
    print("Estou fazendo um bolo...")
    time.sleep(2)
    print("Terminei de fazer meu bolo")

fazer_um_bolo()