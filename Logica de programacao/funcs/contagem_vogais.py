import unicodedata
import sys as interrompe

vogais = ["a","e","i","o","u"]
def remover_acentos(texto):
     texto_normalizado = unicodedata.normalize('NFKD', texto)
    
    # Monta o texto de volta, ignorando os acentos desmembrados
     texto_sem_acento = "".join([caractere for caractere in texto_normalizado if not unicodedata.combining(caractere)])
    
     return texto_sem_acento

def contador_de_vogais(texto):
    quantas_vogais = 0
    letras = [a_vogal for a_vogal in texto if a_vogal.isalpha()]
    for vogal in letras:
        if vogal in vogais:
            quantas_vogais+=1
    return quantas_vogais

texto = input("Digite um texto: ").strip().lower()
texto = remover_acentos(texto)
if any(char.isdigit() for char in texto):
    print("O texto deve conter apenas caracteres, sem números")
    interrompe.exit()

quantidade = contador_de_vogais(texto)
print("O texto contém",quantidade,"vogais")