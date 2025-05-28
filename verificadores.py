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

def validador_movimento(tabuleiro, peca, historico_jogadas):
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
        movimentos_legais = simular(movimentos, tabuleiro, peca)
        if peca.cor == "branca":
            if roque_longo(tabuleiro, peca, historico_jogadas):
                movimentos_legais.append((7, 2))
            elif roque_curto(tabuleiro, peca, historico_jogadas):
                movimentos_legais.append((7, 6))
        else:
            if roque_longo(tabuleiro, peca, historico_jogadas):
                movimentos_legais.append((0, 2))
            elif roque_curto(tabuleiro, peca, historico_jogadas):
                movimentos_legais.append((0, 6))
        return movimentos_legais
    elif isinstance(peca, Peao):
        movimentos = peca.movimento_peao(tabuleiro)
        movimentos_legais = simular(movimentos, tabuleiro, peca)
        enPassant = en_passant(tabuleiro, peca, historico_jogadas)
        if enPassant != None:
            if peca.cor == "branca":
                if "esquerda" in enPassant:
                    movimentos_legais.append((2, peca.posicao[1] - 1))
                if "direita" in enPassant:
                    movimentos_legais.append((2, peca.posicao[1] + 1))
            else:
                if "esquerda" in enPassant:
                    movimentos_legais.append((5, peca.posicao[1] - 1))
                if "direita" in enPassant:
                    movimentos_legais.append((5, peca.posicao[1] + 1))
        return movimentos_legais

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

def en_passant(tabuleiro, peca, historico_jogadas):
    enPassant = []
    if peca in tabuleiro[3]:
        if isinstance (peca, Peao):
            if peca.cor == "branca":
                if peao_esquerda(tabuleiro, peca, historico_jogadas):
                    enPassant.append("esquerda")
                if peao_direita(tabuleiro, peca, historico_jogadas):
                    enPassant.append("direita")
                return enPassant
    elif peca in tabuleiro[4]:
        if isinstance (peca, Peao):
            if peca.cor == "preta":
                if peao_esquerda(tabuleiro, peca, historico_jogadas):
                    enPassant.append("esquerda")
                if peao_direita(tabuleiro, peca, historico_jogadas):
                    enPassant.append("direita")
                return enPassant

def peao_esquerda(tabuleiro, peca, historico_jogadas):
    historico = historico_jogadas[:-1]
    presente = []
    if peca.cor == "branca":
        peao1 = tabuleiro[3][(peca.posicao[1] - 1)]
        if isinstance (peao1, Peao):
            if peao1.cor != peca.cor:
                for item in historico:
                    if peao1.nome in item:
                        presente.append(1)
                if presente == []:
                    if peao1.nome in historico_jogadas[-1]:
                        return True
    else:
        peao1 = tabuleiro[4][(peca.posicao[1] - 1)]
        if isinstance (peao1, Peao):
            if peao1.cor != peca.cor:
                for item in historico:
                    if peao1.nome in item:
                        presente.append(1)
                if presente == []:
                    if peao1.nome in historico_jogadas[-1]:
                        return True

def peao_direita(tabuleiro, peca, historico_jogadas):
    historico = historico_jogadas[:-1]
    presente = []
    if peca.cor == "branca":
        peao1 = tabuleiro[3][(peca.posicao[1] + 1)]
        if isinstance (peao1, Peao):
            if peao1.cor != peca.cor:
                for item in historico:
                    if peao1.nome in item:
                        presente.append(1)
                if presente == []:
                    if peao1.nome in historico_jogadas[-1]:
                        return True
    else:
        peao1 = tabuleiro[4][(peca.posicao[1] + 1)]
        if isinstance (peao1, Peao):
            if peao1.cor != peca.cor:
                for item in historico:
                    if peao1.nome in item:
                        presente.append(1)
                if presente == []:
                    if peao1.nome in historico_jogadas[-1]:
                        return True

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

def roque_longo(tabuleiro, peca, historico_jogadas):
    if not xeque(tabuleiro):
        if peca.cor == "branca":
            casa1 = tabuleiro[7][1]
            casa2 = tabuleiro[7][2]
            casa3 = tabuleiro[7][3]
            if casa1 == " " and casa2 == " " and casa3 == " ":
                if simular_rei1(tabuleiro, peca):
                    presente = []
                    for item in historico_jogadas:
                        if "torre_1" in item or "rei_1" in item:
                            presente.append(1)
                    if presente == []:
                        return True
        else:
            casa1 = tabuleiro[0][1]
            casa2 = tabuleiro[0][2]
            casa3 = tabuleiro[0][3]
            if casa1 == " " and casa2 == " " and casa3 == " ":
                if simular_rei1(tabuleiro, peca):
                    presente = []
                    for item in historico_jogadas:
                        if "torre_3" in item or "rei_2" in item:
                            presente.append(1)
                    if presente == []:
                        return True

def simular_rei1(tabuleiro, peca):
    novo_tabuleiro = copiar_tabuleiro(tabuleiro)
    if peca.cor == "branca":
        novo_tabuleiro[7][1] = peca
        novo_tabuleiro[7][2] = peca
        novo_tabuleiro[7][3] = peca
        if not xeque(novo_tabuleiro):
            return True
    else:
        novo_tabuleiro[0][1] = peca
        novo_tabuleiro[0][2] = peca
        novo_tabuleiro[0][3] = peca
        if not xeque(novo_tabuleiro):
            return True

def roque_curto(tabuleiro, peca, historico_jogadas):
    if not xeque(tabuleiro):
        if peca.cor == "branca":
            casa1 = tabuleiro[7][5]
            casa2 = tabuleiro[7][6]
            if casa1 == " " and casa2 == " ":
                if simular_rei2(tabuleiro, peca):
                    presente = []
                    for item in historico_jogadas:
                        if "torre_2" in item or "rei_1" in item:
                            presente.append(1)
                    if presente == []:
                        return True
        else:
            casa1 = tabuleiro[0][5]
            casa2 = tabuleiro[0][6]
            if casa1 == " " and casa2 == " ":
                if simular_rei2(tabuleiro, peca):
                    presente = []
                    for item in historico_jogadas:
                        if "torre_4" in item or "rei_2" in item:
                            presente.append(1)
                    if presente == []:
                        return True

def simular_rei2(tabuleiro, peca):
    novo_tabuleiro = copiar_tabuleiro(tabuleiro)
    if peca.cor == "branca":
        novo_tabuleiro[7][5] = peca
        novo_tabuleiro[7][6] = peca
        if not xeque(novo_tabuleiro):
            return True
    else:
        novo_tabuleiro[0][5] = peca
        novo_tabuleiro[0][6] = peca
        if not xeque(novo_tabuleiro):
            return True

def xeque_mate(tabuleiro, historico_jogadas):
    movimentos_restantes_brancas = []
    movimentos_restantes_pretas = []
    for linha in tabuleiro:
        for peca in linha:
            if isinstance(peca, Peca):
                if peca.cor == "branca":
                    if validador_movimento(tabuleiro, peca, historico_jogadas) != []:
                        movimentos_restantes_brancas.append(1)
                else:
                    if validador_movimento(tabuleiro, peca, historico_jogadas) != []:
                        movimentos_restantes_pretas.append(1)
    if movimentos_restantes_brancas == []:
        print("Xeque-mate!")
        print("Pretas Vencem!")
        return True
    elif movimentos_restantes_pretas == []:
        print("Xeque-mate!")
        print("Brancas Vencem!")
        return True

def afogamento(tabuleiro, historico_jogadas):
    if not xeque(tabuleiro):
        movimentos_restantes_brancas = []
        movimentos_restantes_pretas = []
        for linha in tabuleiro:
            for peca in linha:
                if isinstance(peca, Peca):
                    if peca.cor == "branca":
                        if validador_movimento(tabuleiro, peca, historico_jogadas) != []:
                            movimentos_restantes_brancas.append(1)
                    else:
                        if validador_movimento(tabuleiro, peca, historico_jogadas) != []:
                            movimentos_restantes_pretas.append(1)
        if movimentos_restantes_brancas == [] or movimentos_restantes_pretas == []:
            return True

def empates_lances(historico_jogadas):
    if len(historico_jogadas) > 9:
        if(historico_jogadas[-1] == historico_jogadas[-5] == historico_jogadas[-9] 
           and historico_jogadas[-3] == historico_jogadas[-7] and
           historico_jogadas[-2] == historico_jogadas[-6] == historico_jogadas[-10] 
           and historico_jogadas[-4] == historico_jogadas[-8]):
            return True
    elif len(historico_jogadas) > 99:
        historico = historico_jogadas[-100:]
        presente = []
        for item in historico:
            if "x" in item:
                presente.append(1)
        if presente == []:
            return True

def material(tabuleiro):
    material_brancas = []
    material_pretas = []
    for linha in tabuleiro:
        for peca in linha:
            if isinstance(peca, Peca):
                if peca.cor == "branca":
                    if isinstance(peca, Torre):
                        material_brancas.append(5)
                    if isinstance(peca, Cavalo):
                        material_brancas.append(3)
                    if isinstance(peca, Bispo):
                        material_brancas.append(3)
                    if isinstance(peca, Rainha):
                        material_brancas.append(9)
                    if isinstance(peca, Rei):
                        material_brancas.append(1)
                    if isinstance(peca, Peao):
                        material_brancas.append(9)
                else:
                    if isinstance(peca, Torre):
                        material_pretas.append(5)
                    if isinstance(peca, Cavalo):
                        material_pretas.append(3)
                    if isinstance(peca, Bispo):
                        material_pretas.append(3)
                    if isinstance(peca, Rainha):
                        material_pretas.append(9)
                    if isinstance(peca, Rei):
                        material_pretas.append(1)
                    if isinstance(peca, Peao):
                        material_pretas.append(9)
    if sum(material_brancas) < 5 and sum(material_pretas) < 5:
        return True

def empates(tabuleiro, historico_jogadas):
    if afogamento(tabuleiro, historico_jogadas) or empates_lances(historico_jogadas) or material(tabuleiro):
        print("Empate!")
        return True
