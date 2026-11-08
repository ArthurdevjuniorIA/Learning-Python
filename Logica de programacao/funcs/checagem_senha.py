def checador_senha(texto):
    pontos = 0
    if len(texto)>=8:
        pontos+=1
    if any(c.isupper() for c in texto):
        pontos+=1
    if any(c.isdigit() for c in texto):
        pontos+=1
    if any(c in "!@#$%&" for c in texto):
        pontos+=1
    return pontos
def verificador_segurança(pontuacao):
    if pontuacao == 4:
        print("Senha forte")
    elif pontuacao>2:
        print("Senha média")
    else:
        print("Senha fraca")

senha = input("Digite sua senha: ")
pontos = checador_senha(senha)
verificador_segurança(pontos)