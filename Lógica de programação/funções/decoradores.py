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