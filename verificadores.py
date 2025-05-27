from pecas import Torre, Cavalo, Bispo, Rainha, Rei, Peao, Peca
import xadrez

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
    if not xeque(tabuleiro):
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
            return True

def empates_lances(historico_jogadas):
    if len(historico_jogadas) > 9:
        if(historico_jogadas[-1] == historico_jogadas[-5] == historico_jogadas[-9] 
           and historico_jogadas[-3] == historico_jogadas[-7] and
           historico_jogadas[-2] == historico_jogadas[-6] == historico_jogadas[-10] 
           and historico_jogadas[-4] == historico_jogadas[-8]):
            return True
    elif len(historico_jogadas) > 99:
        if not "x" in historico_jogadas[-1: -100]:
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
    if afogamento(tabuleiro) or empates_lances(historico_jogadas) or material(tabuleiro):
        print("Empate!")
        return True
#roque
def espaco_livre_pretas(tabuleiro):                    
    return all(tabuleiro[7][i] is None for i in [1,2,3])#checagem de espaço liberado das pretas na parte à esquerda do rei

def espaco_livre_pretas2(tabuleiro):                    
    return all(tabuleiro[7][i] is None for i in [5,6])#checagem de espaço liberado das pretas na parte à direita do rei

def espaco_livre_brancas(tabuleiro):                    
    return all(tabuleiro[0][i] is None for i in [1,2,3])#checagem de espaço liberado das brancas na parte à esquerda do rei

def espaco_livre_brancas2(tabuleiro):                    
    return all(tabuleiro[0][i] is None for i in [5,6])#checagem de espaço liberado das brancas na parte à direita do rei

def posicao_torre_brancas(tabuleiro): #checa se a torre está na posição inicial, mas não se ocorreu alguma movimentação nela, tem que ver isso dps
     return tabuleiro[0][0] == xadrez.torre_3 or tabuleiro[0][7] == xadrez.torre_4

def posicao_torre_pretas(tabuleiro): #mesma coisa que a de cima
     return tabuleiro[7][0] == xadrez.torre_1 or tabuleiro[7][7] == xadrez.torre_2

def posicao_rei_brancas(tabuleiro): #checa se o rei está na posição inicial para fazer o roque, mas não se ele se moveu, tem que ver isso dps
     return tabuleiro[0][4] == xadrez.rei_2

def posicao_rei_pretas(tabuleiro): #mesma coisa que a de cima
     return tabuleiro[7][4] == xadrez.rei_1

def permissao_roque_pretas(tabuleiro): #checagem de condições para ocorrer o roque
    if espaco_livre_pretas(tabuleiro) or espaco_livre_pretas2(tabuleiro) and posicao_torre_pretas(tabuleiro) and posicao_rei_pretas(tabuleiro):
        return True  

def mover_roque_pretas(peca, linha, coluna, tabuleiro): #Roque das pretas (movimento)
    Permissao = permissao_roque_pretas(tabuleiro)
    if Permissao == True and xadrez.mover_peca == tabuleiro[7][6]: #checa a posição que o jogador tentou mover o rei, se a posição ultrapassa o movimento padrão do rei então é uma tentativa de roque (creio que do jeito que fiz o código isso não funcione ainda, tem que ser implementado essa possibilidade)
        tabuleiro[7][6] = xadrez.rei_1 #movimenta o rei para a posição do roque curto
        tabuleiro[7][5] = xadrez.torre_2 #movimenta a torre para a posição de roque curto
    elif Permissao == True and tabuleiro[7][2]: #repetição do que houve acima
        tabuleiro[7][2] = xadrez.rei_1 #movimenta o rei para a posição do roque longo
        tabuleiro[7][3] = xadrez.torre_1 #movimenta a torre para a posição de roque longo
    else:
        print("Movimento Inválido!") #caso o movimento seja inválido, não sei se funciona, foi só pra tentar mostrar o que eu planejo fazer
        xadrez.mover_peca(peca, linha, coluna)

def permissao_roque_brancas(tabuleiro): #checagem de condições para ocorrer o roque
    if (espaco_livre_brancas(tabuleiro) or espaco_livre_brancas2(tabuleiro)) and posicao_torre_brancas(tabuleiro) and posicao_rei_brancas(tabuleiro):
        return True    
    
def mover_roque_brancas(peca, linha, coluna, tabuleiro): #Roque das brancas (movimento)
    permissao = permissao_roque_brancas(tabuleiro)
    if permissao == True and xadrez.mover_peca == tabuleiro[0][6]: #checa a posição que o jogador tentou mover o rei, se a posição ultrapassa o movimento padrão do rei então é uma tentativa de roque (creio que do jeito que fiz o código isso não funcione ainda, tem que ser implementado essa possibilidade)
        tabuleiro[0][6] = xadrez.rei_2 #movimenta o rei para a posição do roque curto
        tabuleiro[0][5] = xadrez.torre_4 #movimenta a torre para a posição de roque curto
    elif permissao == True and tabuleiro[0][2]: #repetição do que houve acima
        tabuleiro[0][2] = xadrez.rei_2 #movimenta o rei para a posição do roque longo
        tabuleiro[0][3] = xadrez.torre_3 #movimenta a torre para a posição de roque longo
    else:
        print("Movimento Inválido!") #caso o movimento seja inválido, não sei se funciona, foi só pra tentar mostrar o que eu planejo fazer
        xadrez.mover_peca(peca, linha, coluna)
#tudo isso só pra ter uma ideia base de como fazer o roque, tem mta coisa errada nesse código kkkkk

#verificador de en passant
def se_peao_linha(tabuleiro):#checa se algum peão branco ou preto se moveu 3 casas, independentemente de quantos turnos usou pra isso
    for peca in tabuleiro[4]:
        if isinstance (peca, Peao):
            if peca.cor == "branca":
                permissao_en_passant_B = 'tem permissão para o en passant'
                return permissao_en_passant_B
    for peca in tabuleiro[3]:
        if isinstance (peca, Peao):
            if peca.cor == "preta":
                permissao_en_passant_P = 'tem permissão para o en passant'
                return permissao_en_passant_P

#agr vai checar se há um peão inimigo ao lado do peão que está retornando permissao_en_passant_P/B. Acho que dá pra fazer isso usando uma function que é chamada com o retorno de se_peao_linha, essa function vai checar se o peão que retornou permissao_en_passant_P/B tem algum peão inimigo ao lado, se tiver um peão inimigo ao lado então deve checar se esse peão inimigo chegou na casa onde está em um só turno (usando o histórico). Tem que ver uma forma de fazer com que além de retornar permissao_en_passant_P/B meio que retorne a posição do peão que foi detectado, se mudar o que a variável permissao_en_passant_P/B aloca dá pra fazer de boa.