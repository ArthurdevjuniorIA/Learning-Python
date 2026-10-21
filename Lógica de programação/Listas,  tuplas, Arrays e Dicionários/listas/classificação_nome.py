candidatos = []
print("Digite o nome dos 10 candidatos aprovados na ordem de classificação:")
for i in range(10):
    nome = input(f"Digite o nome do {i + 1}º colocado: ")
    candidatos.append(nome)

print("\n--- Cadastro realizado com sucesso! ---")
while True:
    consulta = input("\nDigite o nome de um candidato para consultar a classificação (ou 'fim' para sair): ")
    if consulta.lower() == "fim":
        print("Programa encerrado.")
        break
    if consulta in candidatos:
        posicao = candidatos.index(consulta) + 1
        print(f"O candidato {consulta} ficou na {posicao}ª posição.")
    else:
        print("Candidato não encontrado. Verifique se digitou o nome corretamente.")