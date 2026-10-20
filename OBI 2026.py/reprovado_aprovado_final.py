nota1, nota2 = map(float,input().split())

media = ((nota1*2) +(nota2*3))/5
if media>=7:
    print("Aprovado")
elif media<3:
    print("Reprovado")
else:
    print("Recuperacao")