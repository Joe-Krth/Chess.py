from pecas import Torre, Cavalo, Bispo, Rainha, Rei, Peao, Peca

#Validadores
def validador_peca(peca, turno):
    if peca == " ":
        return False
    elif turno % 2 == 1:
        if peca.cor == "branca":
            return True
    else:
        if peca.cor == "preta":
            return True

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

#Verificadores
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
        
def xeque_mate(tabuleiro):
    movimentos_restantes_brancas = []
    movimentos_restantes_pretas = []
    for linha in tabuleiro:
        for peca in linha:
            if isinstance(peca, Peca):
                if peca.cor == "branca":
                    if validador_movimento(tabuleiro, peca) != []:
                        movimentos_restantes_brancas.append(1)
                else:
                    if validador_movimento(tabuleiro, peca) != []:
                        movimentos_restantes_pretas.append(1)
    if movimentos_restantes_brancas == []:
        print("Xeque-mate!")
        print("Pretas Vencem!")
        return True
    elif movimentos_restantes_pretas == []:
        print("Xeque-mate!")
        print("Brancas Vencem!")
        return True

def afogamento(tabuleiro):
    movimentos_restantes_brancas = []
    movimentos_restantes_pretas = []
    for linha in tabuleiro:
        for peca in linha:
            if isinstance(peca, Peca):
                if peca.cor == "branca":
                    if validador_movimento(tabuleiro, peca) != []:
                        movimentos_restantes_brancas.append(1)
                else:
                    if validador_movimento(tabuleiro, peca) != []:
                        movimentos_restantes_pretas.append(1)
    if movimentos_restantes_brancas == [] or movimentos_restantes_pretas == []:
        print("Empate!")
        return True
