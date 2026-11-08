import random
def gerador_senha():
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    simbolos = ["!","@","#","$","%","&"]
    senha = ""
    aleatorio_letras = random.randint(1,26)
    aleatorio_numeros = random.randint(1,9)
    aleatorio_simbolos = random.randint(1,5)
    if not senha:
        senha = letras[aleatorio_letras] + senha
    if not any(c.isdigit() for c in senha):
        senha = numeros[aleatorio_numeros] + senha
    if not any(c.islower() for c in senha):
        senha = letras[aleatorio_letras].lower() + senha
    if not any(c in "!@#$%&" for c in senha):
        senha = simbolos[aleatorio_simbolos] + senha
    for i in range(len(senha),8):
        aleatorio_letras_novamente = random.randint(1,26)
        aleatorio_numeros_novamente = random.randint(1,9)
        aleatorio_simbolos_novamente = random.randint(1,6)
        senha = letras[aleatorio_letras_novamente] + senha
        senha = numeros[aleatorio_numeros_novamente] + senha
        simbolos[aleatorio_simbolos_novamente]  + senha


    return senha

senha = gerador_senha()

print("A senha gerada foi: ",senha)