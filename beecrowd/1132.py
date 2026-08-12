X = int(input())
Y = int(input())

x = min(X, Y)
y = max(X, Y)
soma = 0


for i in range(x, y +1):
    if i % 13 != 0:
         soma += i

print(soma)