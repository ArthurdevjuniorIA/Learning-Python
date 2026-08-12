nome = input("Digite seu nome de usuário:")
print("Perfis disponíveis:")
print("admin")
print("editor")
print("visualizador")
perfil = input("Digite seu perfil:")

erro = False

if nome.strip() == "":
    print("[ ERRO ] nome não pode ser vazio")
    erro = True

if perfil not in ["admin", "editor", "visualizador"]:
    print("[ ERRO ] perfil inválido")
    erro = True

if not erro:
    print("Cadastro do usuário confirmado.")