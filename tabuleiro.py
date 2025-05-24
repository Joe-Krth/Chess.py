def criar_tabuleiro():
    return [[" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8,
            [" "] * 8]

def exibir(tabuleiro):
    for i, linha in enumerate(tabuleiro):
            print(8 - i, end = " ")
            print(*linha)
    print(" ", "a", "b", "c", "d", "e", "f", "g", "h")