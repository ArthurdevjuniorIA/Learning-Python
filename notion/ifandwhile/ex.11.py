c = "="
for i in range(0, 11):
  # "ljust(10)"" garante que a string sempre ocupe 10 caracteres, preenchendo o resto com espaços.
  barra = c * i
  print(f"[{barra.ljust(10)}] {i * 10}%")
