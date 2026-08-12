c = 0
p = 0
n = 0
while True:
    c = int(input())

    if c == 0:
        break

    if c == 1:
        p += 1
    
    elif c == 2:
        n += 1
    
print("Acessos autorizados:", p)
print("Acessos negados:", n)
