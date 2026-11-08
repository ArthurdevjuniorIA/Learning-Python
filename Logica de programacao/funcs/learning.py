def leitor_de_caracteres(texto):
    print(f"O texto digitado tem {len(texto)} caracteres ")

def saudacao_personalizada(horario):
    if horario<12:
        print("Bom dia")
    elif 12<horario<18:
        print("Boa tarde")
    else:
        print("Boa noite")

def fruta_valor():
    fruta1,fruta2,fruta3 = input("Digite os produtos separados por vírgula: ").split(",")
    preco1,preco2,preco3 = input("Digite os produtos separados por vírgula: ").split(",")
    preco1,preco2,preco3 = float(preco1), float(preco2), float(preco3)
    print(f"{fruta1}: {preco1}\n{fruta2}: {preco2}\n{fruta3}: {preco3}")

