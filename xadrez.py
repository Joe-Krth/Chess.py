from tabuleiro import criar_tabuleiro, exibir
from pecas import Torre, Cavalo, Bispo, Rainha, Rei, Peao, Peca
from coordenadas import codigos, coordenadas
from verificadores import promocao_peao, xeque, xeque_mate, afogamento, validador_peca, validador_movimento
tabuleiro = criar_tabuleiro()
turno = 1

torre_1 = Torre("branca", (7, 0))
cavalo_1 = Cavalo("branca", (7, 1))
bispo_1 = Bispo("branca", (7, 2))
rainha_1 = Rainha("branca", (7, 3))
rei_1 = Rei("branca", (7, 4))
bispo_2 = Bispo("branca", (7, 5))
cavalo_2 = Cavalo("branca", (7, 6))
torre_2 = Torre("branca", (7, 7))
peao_1 = Peao("branca", (6,0))
peao_2 = Peao("branca", (6,1))
peao_3 = Peao("branca", (6,2))
peao_4 = Peao("branca", (6,3))
peao_5 = Peao("branca", (6,4))
peao_6 = Peao("branca", (6,5))
peao_7 = Peao("branca", (6,6))
peao_8 = Peao("branca", (6,7))

torre_3 = Torre("preta", (0, 0))
cavalo_3 = Cavalo("preta", (0, 1))
bispo_3 = Bispo("preta", (0, 2))
rainha_2 = Rainha("preta", (0, 3))
rei_2 = Rei("preta", (0, 4))
bispo_4 = Bispo("preta", (0, 5))
cavalo_4 = Cavalo("preta", (0, 6))
torre_4 = Torre("preta", (0, 7))
peao_9 = Peao("preta", (1,0))
peao_10 = Peao("preta", (1,1))
peao_11 = Peao("preta", (1,2))
peao_12 = Peao("preta", (1,3))
peao_13 = Peao("preta", (1,4))
peao_14 = Peao("preta", (1,5))
peao_15 = Peao("preta", (1,6))
peao_16 = Peao("preta", (1,7))

tabuleiro[7][0] = torre_1
tabuleiro[7][1] = cavalo_1
tabuleiro[7][2] = bispo_1
tabuleiro[7][3] = rainha_1
tabuleiro[7][4] = rei_1
tabuleiro[7][5] = bispo_2
tabuleiro[7][6] = cavalo_2
tabuleiro[7][7] = torre_2
tabuleiro[6][0] = peao_1
tabuleiro[6][1] = peao_2
tabuleiro[6][2] = peao_3
tabuleiro[6][3] = peao_4
tabuleiro[6][4] = peao_5
tabuleiro[6][5] = peao_6
tabuleiro[6][6] = peao_7
tabuleiro[6][7] = peao_8

tabuleiro[0][0] = torre_3
tabuleiro[0][1] = cavalo_3
tabuleiro[0][2] = bispo_3
tabuleiro[0][3] = rainha_2
tabuleiro[0][4] = rei_2
tabuleiro[0][5] = bispo_4
tabuleiro[0][6] = cavalo_4
tabuleiro[0][7] = torre_4
tabuleiro[1][0] = peao_9
tabuleiro[1][1] = peao_10
tabuleiro[1][2] = peao_11
tabuleiro[1][3] = peao_12
tabuleiro[1][4] = peao_13
tabuleiro[1][5] = peao_14
tabuleiro[1][6] = peao_15
tabuleiro[1][7] = peao_16

def escolher_peca():
    linha, coluna = coordenadas(input("Peça: "))
    peca = tabuleiro[linha][coluna]

    validar_peca(peca, linha, coluna)

def validar_peca(peca, linha, coluna):
    if validador_peca(peca, turno):
        print(f"Movimentos Disponíveis: {', '.join(codigos(validador_movimento(tabuleiro, peca)))}")
        mover_peca(peca, linha, coluna)
    else:
        print("Peça Inválida!")
        escolher_peca()

def mover_peca(peca, linha, coluna):
    linha_dest, coluna_dest = coordenadas(input("Para: "))
    casa = tabuleiro[linha_dest][coluna_dest]

    if casa == " ": 
        if (linha_dest, coluna_dest) in validador_movimento(tabuleiro, peca):
            tabuleiro[linha_dest][coluna_dest] = peca
            peca.posicao = (linha_dest, coluna_dest)
            tabuleiro[linha][coluna] = " "
        else:
            print("Movimento Inválido!")
            mover_peca(peca, linha, coluna)
    elif isinstance(casa, Peca):
        if casa.cor == peca.cor:
            linha, coluna = linha_dest, coluna_dest
            peca = tabuleiro[linha][coluna]
            print(f"Peça: {' '.join(codigos([peca.posicao]))}")
            validar_peca(peca, linha, coluna)
        else:
            if (linha_dest, coluna_dest) in validador_movimento(tabuleiro, peca):
                tabuleiro[linha_dest][coluna_dest] = peca
                peca.posicao = (linha_dest, coluna_dest)
                tabuleiro[linha][coluna] = " "
            else:
                print("Movimento Inválido!")
                mover_peca(peca, linha, coluna)
    
while turno != 0:
    promocao_peao(tabuleiro)
    if xeque(tabuleiro):
        if xeque_mate(tabuleiro):
            exibir(tabuleiro)
            break
        else:
            print("Xeque!")
    else:
        if afogamento(tabuleiro):
            exibir(tabuleiro)
            break
    exibir(tabuleiro)
    escolher_peca()

    turno += 1
