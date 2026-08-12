v = 0
c = 0
while True:
    v = int(input())

    if v == 0:
       break
    
    if v > 80:
     c += 1

print("Veículos acima do limite:", c)