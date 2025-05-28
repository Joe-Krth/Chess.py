from tabuleiro import criar_tabuleiro, exibir
from pecas import Torre, Cavalo, Bispo, Rainha, Rei, Peao, Peca
from coordenadas import codigos, coordenadas
from verificadores import promocao_peao, xeque, xeque_mate, empates, validador_peca, validador_movimento
tabuleiro = criar_tabuleiro()
turno = 1

torre_1 = Torre("torre_1", "branca", (7, 0))
cavalo_1 = Cavalo("cavalo_1", "branca", (7, 1))
bispo_1 = Bispo("bispo_1", "branca", (7, 2))
rainha_1 = Rainha("rainha_1", "branca", (7, 3))
rei_1 = Rei("rei_1", "branca", (7, 4))
bispo_2 = Bispo("bispo_2", "branca", (7, 5))
cavalo_2 = Cavalo("cavalo_2", "branca", (7, 6))
torre_2 = Torre("torre_2", "branca", (7, 7))
peao_1 = Peao("peao_1", "branca", (6,0))
peao_2 = Peao("peao_2", "branca", (6,1))
peao_3 = Peao("peao_3", "branca", (6,2))
peao_4 = Peao("peao_4", "branca", (6,3))
peao_5 = Peao("peao_5", "branca", (6,4))
peao_6 = Peao("peao_6", "branca", (6,5))
peao_7 = Peao("peao_7", "branca", (6,6))
peao_8 = Peao("peao_8", "branca", (6,7))

torre_3 = Torre("torre_3", "preta", (0, 0))
cavalo_3 = Cavalo("cavalo_3", "preta", (0, 1))
bispo_3 = Bispo("bispo_3", "preta", (0, 2))
rainha_2 = Rainha("rainha_2", "preta", (0, 3))
rei_2 = Rei("rei_2", "preta", (0, 4))
bispo_4 = Bispo("bispo_4", "preta", (0, 5))
cavalo_4 = Cavalo("cavalo_4", "preta", (0, 6))
torre_4 = Torre("torre_4", "preta", (0, 7))
peao_9 = Peao("peao_9", "preta", (1,0))
peao_10 = Peao("peao_10", "preta", (1,1))
peao_11 = Peao("peao_11", "preta", (1,2))
peao_12 = Peao("peao_12", "preta", (1,3))
peao_13 = Peao("peao_13", "preta", (1,4))
peao_14 = Peao("peao_14", "preta", (1,5))
peao_15 = Peao("peao_15", "preta", (1,6))
peao_16 = Peao("peao_16", "preta", (1,7))

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

historico_jogadas = []

def escolher_peca():
    linha, coluna = coordenadas(input("Peça: "))
    peca = tabuleiro[linha][coluna]

    validar_peca(peca, linha, coluna)

def validar_peca(peca, linha, coluna):
    if validador_peca(peca, turno):
        print(f"Movimentos Disponíveis: {', '.join(codigos(validador_movimento(tabuleiro, peca, historico_jogadas)))}")
        mover_peca(peca, linha, coluna)
    else:
        print("Peça Inválida!")
        escolher_peca()

def mover_peca(peca, linha, coluna):
    linha_dest, coluna_dest = coordenadas(input("Para: "))
    casa = tabuleiro[linha_dest][coluna_dest]
    global historico_jogadas

    if casa == " ": 
        if (linha_dest, coluna_dest) in validador_movimento(tabuleiro, peca, historico_jogadas):
            if isinstance (peca, Rei):
                if peca.cor == "branca":
                    if peca.posicao == (7, 4):
                        if (linha_dest, coluna_dest) == (7, 2):
                            torre = tabuleiro[7][0]
                            tabuleiro[7][3] = torre
                            torre.posicao = (7, 3)
                            tabuleiro[7][0] = " "
                        elif (linha_dest, coluna_dest) == (7, 6):
                            torre = tabuleiro[7][7]
                            tabuleiro[7][5] = torre
                            torre.posicao = (7, 5)
                            tabuleiro[7][7] = " "
                else:
                    if peca.posicao == (0, 4):
                        if (linha_dest, coluna_dest) == (0, 2):
                            torre = tabuleiro[0][0]
                            tabuleiro[0][3] = torre
                            torre.posicao = (0, 3)
                            tabuleiro[0][0] = " "
                        elif (linha_dest, coluna_dest) == (0, 6):
                            torre = tabuleiro[0][7]
                            tabuleiro[0][5] = torre
                            torre.posicao = (0, 5)
                            tabuleiro[0][7] = " "
            elif isinstance (peca, Peao):
                if peca.cor == "branca":
                    if (linha_dest, coluna_dest) == (2, (peca.posicao[1] - 1)):
                        tabuleiro[3][(peca.posicao[1] - 1)] = " "
                    elif (linha_dest, coluna_dest) == (2, (peca.posicao[1] + 1)):
                        tabuleiro[3][(peca.posicao[1] + 1)] = " "
                else:
                    if (linha_dest, coluna_dest) == (5, (peca.posicao[1] - 1)):
                        tabuleiro[4][(peca.posicao[1] - 1)] = " "
                    elif (linha_dest, coluna_dest) == (5, (peca.posicao[1] + 1)):
                        tabuleiro[4][(peca.posicao[1] + 1)] = " "
            tabuleiro[linha_dest][coluna_dest] = peca
            peca.posicao = (linha_dest, coluna_dest)
            tabuleiro[linha][coluna] = " "
            m = f"{peca.nome} {peca}{''.join(codigos([(linha_dest, coluna_dest)]))}"
            historico_jogadas.append(m)
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
            if (linha_dest, coluna_dest) in validador_movimento(tabuleiro, peca, historico_jogadas):
                tabuleiro[linha_dest][coluna_dest] = peca
                peca.posicao = (linha_dest, coluna_dest)
                tabuleiro[linha][coluna] = " "
                m = f"{peca.nome} {peca}x{''.join(codigos([(linha_dest, coluna_dest)]))}"
                historico_jogadas.append(m)
            else:
                print("Movimento Inválido!")
                mover_peca(peca, linha, coluna)

while turno != 0:
    promocao_peao(tabuleiro)
    if xeque(tabuleiro):
        if xeque_mate(tabuleiro, historico_jogadas):
            exibir(tabuleiro)
            break
        elif empates(tabuleiro, historico_jogadas):
            exibir(tabuleiro)
            break
        else:
            print("Xeque!")
    else:
        if empates(tabuleiro, historico_jogadas):
            exibir(tabuleiro)
            break
    exibir(tabuleiro)
    escolher_peca()
    turno += 1
