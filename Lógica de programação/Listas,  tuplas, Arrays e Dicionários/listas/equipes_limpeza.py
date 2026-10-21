equipes_de_3 = [ ]
equipes = [ ]
while True:
    voluntario = input("Nome do voluntário (ou 'fim' para encerrar): ")
    if voluntario  == "fim":
        for i in range(len(equipes)):
                print(f"Equipe {i+1}")
                print(*equipes[i],sep="\n")
        tamanho = len(equipes)+1    
        if equipes_de_3 != [ ]:
              print(f"Equipe {tamanho}")
              print(*equipes_de_3,sep="\n")
        break
        
    else:
        equipes_de_3.append(voluntario)
        if len(equipes_de_3) == 3:
                equipe_normal = equipes_de_3.copy()
                equipes.append(equipe_normal)
                equipes_de_3.clear()
                

           

