def coordenadas(coordenada):
    linha = 8 - int(coordenada[1])
    colunas = "abcdefgh"
    coluna = colunas.index(coordenada[0])
    return linha, coluna #Traduz pro programa. Entrada: e2; Saída: (7, 4)

def codigos(codigo):
    jogadas = []

    for x in codigo:
        linha_x = 8 - x[0]
        colunas = "abcdefgh"
        coluna_x = colunas[x[1]]
        jogadas.append(f"{coluna_x}{linha_x}")

    return jogadas #Traduz pro usuário. Entrada: (7, 4); Saída: e2 