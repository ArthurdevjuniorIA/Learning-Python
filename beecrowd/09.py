nome = input("Digite seu nome de usuário:")
print("Perfis disponíveis:")
print("admin")
print("editor")
print("visualizador")
perfil = input("Digite seu perfil:")
 
if nome == " ":
     print("[ ERRO ] nome não pode ser vazio")
elif perfil not in ["admin", "editor", "visualizador"]:
    print("[ ERRO ] perfil inválido")
else:
    print("Cadastro do usuário confirmado.")