valores = [1,2,3,4,5,-3,-4]
for i,valor in enumerate(valores):
    if valor<0:
        valores[i] = 0
print(valores)
