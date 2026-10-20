tempo1 = float(input())
tempo2 = float(input())
tempo3 = float(input())
tempos = [tempo1, tempo2, tempo3]
tempo_maior = 0
for i in range(len(tempos)):
    n = i+1
    if tempos[i]>tempo_maior:
        tempo_maior = tempos[i]
   