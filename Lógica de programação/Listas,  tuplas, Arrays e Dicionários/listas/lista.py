lista = [0,1,7,0,5,8,0,10]
for valor in lista:
    if valor>5:
        lista.remove(valor)
print(*lista)
l1 = [valor for valor in lista !=0]
l2 = [valor for valor in lista ==0]