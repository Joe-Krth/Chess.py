from pecas import Torre, Cavalo, Bispo, Rainha, Rei, Peao, Peca

def promocao_peao(tabuleiro):
    for peca in tabuleiro[0]:
        if isinstance (peca, Peao):
            if peca.cor == "branca":
                promocao = input("Promover para: ")
                if promocao == "r" or promocao == "R":
                    peca.__class__ = Torre
                elif promocao == "q" or promocao == "Q":
                    peca.__class__ = Rainha
                elif promocao == "b" or promocao == "B":
                    peca.__class__ = Bispo
                elif promocao == "n" or promocao == "N":
                    peca.__class__ = Cavalo
                else:
                    print("Promoção Inválida!")
                    promocao_peao(tabuleiro)
    for peca in tabuleiro[7]:
        if isinstance (peca, Peao):
            if peca.cor == "preta":
                promocao = input("Promover para: ")
                if promocao == "r" or promocao == "R":
                    peca.__class__ = Torre
                elif promocao == "q" or promocao == "Q":
                    peca.__class__ = Rainha
                elif promocao == "b" or promocao == "B":
                    peca.__class__ = Bispo
                elif promocao == "n" or promocao == "N":
                    peca.__class__ = Cavalo
                else:
                    print("Promoção Inválida!")
                    promocao_peao(tabuleiro)

def xeque(tabuleiro):
    for linha in tabuleiro:
        for peca in linha:
            if isinstance (peca, Peca):
                if isinstance(peca, Torre):
                    if peca.movimento_torre(tabuleiro) != []:
                        if auxiliar(peca.movimento_torre(tabuleiro), tabuleiro):
                            return True
                elif isinstance(peca, Cavalo):
                    if peca.movimento_cavalo(tabuleiro) != []:
                        if auxiliar(peca.movimento_cavalo(tabuleiro), tabuleiro):
                            return True
                elif isinstance(peca, Bispo):
                    if peca.movimento_bispo(tabuleiro) != []:
                        if auxiliar(peca.movimento_bispo(tabuleiro), tabuleiro):
                            return True
                elif isinstance(peca, Rainha):
                    if peca.movimento_rainha(tabuleiro) != []:
                        if auxiliar(peca.movimento_rainha(tabuleiro), tabuleiro):
                            return True
                elif isinstance(peca, Rei):
                    if peca.movimento_rei(tabuleiro) != []:
                        if auxiliar(peca.movimento_rei(tabuleiro), tabuleiro):
                            return True
                elif isinstance(peca, Peao):
                    if peca.movimento_peao(tabuleiro) != []:
                        if auxiliar(peca.movimento_peao(tabuleiro), tabuleiro):
                            return True
                        
def auxiliar(movimentos, tabuleiro):
    for coord in movimentos:
        casa = tabuleiro[coord[0]][coord[1]]
        if isinstance (casa, Rei):
            return True