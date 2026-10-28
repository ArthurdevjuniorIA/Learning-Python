
def verificador_palavra_longa(texto):
    # 
    Palavras_longas = []
    for palavra in texto:
        # Remove qualquer pontuação que esteja grudado na palavra
        palavra_limpa = palavra.strip(".,!()%")

        # Verifica se o tamanho da palavra é maior do que 10 caracteres para ser considerado uma palavra grande
        if len(palavra_limpa)>10:
            Palavras_longas.append(palavra_limpa)

    # Verifica se a lista de palavras longas não está vazia
    if not Palavras_longas:
        print("Nenhuma palavra longa foi encontrada")
        return -1

    # Formato a lista para printar em apenas uma linha e com a primeira letra maiúscula
    lista_formatada = ", ".join(Palavras_longas).title()
    
    print(f"Palavras longas encontradas: {lista_formatada}")
   
   # Uma boa prática retornar a lista
    return Palavras_longas

entrada = input("Digite um texto: ").split()
resultado = verificador_palavra_longa(entrada)