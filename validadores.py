def validador_peca(peca, turno):
    if peca == " ":
        return False
    elif turno % 2 == 1:
        if peca.cor == "branca":
            return True
    else:
        if peca.cor == "preta":
            return True

from pecas import Torre, Cavalo, Bispo, Rainha, Rei, Peao, Peca
from verificadores import xeque

def validador_movimento(tabuleiro, peca):
    if isinstance(peca, Torre):
        movimentos = peca.movimento_torre(tabuleiro)
        return simular(movimentos, tabuleiro, peca)
    elif isinstance(peca, Cavalo):
        movimentos = peca.movimento_cavalo(tabuleiro)
        return simular(movimentos, tabuleiro, peca)
    elif isinstance(peca, Bispo):
        movimentos = peca.movimento_bispo(tabuleiro)
        return simular(movimentos, tabuleiro, peca)
    elif isinstance(peca, Rainha):
        movimentos = peca.movimento_rainha(tabuleiro)
        return simular(movimentos, tabuleiro, peca)
    elif isinstance(peca, Rei):
        movimentos = peca.movimento_rei(tabuleiro)
        return simular(movimentos, tabuleiro, peca)
    elif isinstance(peca, Peao):
        movimentos = peca.movimento_peao(tabuleiro)
        return simular(movimentos, tabuleiro, peca)
    
def simular(movimentos, tabuleiro, peca):
    movimentos_legais = []
    for coord in movimentos:
        novo_tabuleiro = copiar_tabuleiro(tabuleiro)
        novo_tabuleiro[coord[0]][coord[1]] = peca
        novo_tabuleiro[peca.posicao[0]][peca.posicao[1]] = " "
        if not xeque(novo_tabuleiro):
            movimentos_legais.append(coord)
    return movimentos_legais

def copiar_tabuleiro(tabuleiro):
    novo_tabuleiro = []

    for linha in tabuleiro:
        nova_linha = []
        for peca in linha:
            if isinstance(peca, Peca):
                nova_linha.append(peca)
            else:
                nova_linha.append(" ")
        novo_tabuleiro.append(nova_linha)
    return novo_tabuleiro
