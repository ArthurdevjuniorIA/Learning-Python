
print("===== CARTELA DE BINGO =====")

numeros_cartelas = list(map(int, input("Informe os números da sua cartela: ").split()))
while True:
    numero_sorteado = int(input("Número sorteado: "))
    if numero_sorteado == 0:
        print("Jogo finalizado pelo usuário.")
        break

    if numero_sorteado not in numeros_cartelas:
        print(f"O número {numero_sorteado} não está na sua cartela")

    else:
        print(f"O número {numero_sorteado} foi marcado")
        numeros_cartelas.remove(numero_sorteado)
    
    if numeros_cartelas == [ ]:
        print("🎉 BINGO! Todos os números da cartela foram sorteados!")
        break
