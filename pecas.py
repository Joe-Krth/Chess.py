class Peca:
    def __init__(self, nome, cor, posicao):
        self.nome = nome
        self.cor = cor
        self.posicao = posicao

class Torre(Peca):
    def __str__(self):
        return "R" if self.cor == "branca" else "r"

    def movimento_torre(self, tabuleiro):
        jogadas = []
        direcoes = [(1,0),
                    (-1,0),
                    (0,1),
                    (0,-1)]
        linha, coluna = self.posicao

        for mov_linha, mov_coluna in direcoes:
            nova_linha = linha + mov_linha
            nova_coluna = coluna + mov_coluna

            while 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                casa = tabuleiro[nova_linha][nova_coluna]
                
                if casa == " ":
                    jogadas.append((nova_linha, nova_coluna))
                elif isinstance(casa, Peca):
                    if casa.cor != self.cor:
                        jogadas.append((nova_linha, nova_coluna))
                        break
                    else:
                        break
                nova_linha += mov_linha
                nova_coluna += mov_coluna
        return jogadas

class Cavalo(Peca):
    def __str__(self):
        return "N" if self.cor == "branca" else "n"
    
    def movimento_cavalo(self, tabuleiro):
        jogadas = []
        direcoes = [(2,-1),
                    (2,1),
                    (-2,-1),
                    (-2,1),
                    (-1,-2),
                    (1,-2),
                    (-1,2),
                    (1,2)]
        linha, coluna = self.posicao

        for mov_linha, mov_coluna in direcoes:
            nova_linha = linha + mov_linha
            nova_coluna = coluna + mov_coluna

            if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                casa = tabuleiro[nova_linha][nova_coluna]

                if casa == " ":
                    jogadas.append((nova_linha, nova_coluna))
                elif isinstance(casa, Peca):
                    if casa.cor != self.cor:
                        jogadas.append((nova_linha, nova_coluna))
        return jogadas

class Bispo(Peca):
    def __str__(self):
        return "B" if self.cor == "branca" else "b"

    def movimento_bispo(self, tabuleiro):
        jogadas = []
        direcoes = [(1,-1),
                    (1,1),
                    (-1,-1),
                    (-1,1)]
        linha, coluna = self.posicao

        for mov_linha, mov_coluna in direcoes:
            nova_linha = linha + mov_linha
            nova_coluna = coluna + mov_coluna

            while 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                casa = tabuleiro[nova_linha][nova_coluna]

                if casa == " ":
                    jogadas.append((nova_linha, nova_coluna))
                elif isinstance(casa, Peca):
                    if casa.cor != self.cor:
                        jogadas.append((nova_linha, nova_coluna))
                        break
                    else:
                        break
                nova_linha += mov_linha
                nova_coluna += mov_coluna
        return jogadas

class Rainha(Peca):
    def __str__(self):
        return "Q" if self.cor == "branca" else "q"
    
    def movimento_rainha(self, tabuleiro):
        jogadas = []
        direcoes = [(1,-1),
                    (1,0),
                    (1,1),
                    (0,-1),
                    (0,1),
                    (-1,-1),
                    (-1,0),
                    (-1,1)]
        linha, coluna = self.posicao

        for mov_linha, mov_coluna in direcoes:
            nova_linha = linha + mov_linha
            nova_coluna = coluna + mov_coluna

            while 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                casa = tabuleiro[nova_linha][nova_coluna]

                if casa == " ":
                    jogadas.append((nova_linha, nova_coluna))
                elif isinstance(casa, Peca):
                    if casa.cor != self.cor:
                        jogadas.append((nova_linha, nova_coluna))
                        break
                    else:
                        break
                nova_linha += mov_linha
                nova_coluna += mov_coluna
        return jogadas

class Rei(Peca):
    def __str__(self):
        return "K" if self.cor == "branca" else "k"
    
    def movimento_rei(self, tabuleiro):
        jogadas = []
        direcoes = [(1,-1),
                    (1,0),
                    (1,1),
                    (0,-1),
                    (0,1),
                    (-1,-1),
                    (-1,0),
                    (-1,1)]
        linha, coluna = self.posicao

        for mov_linha, mov_coluna in direcoes:
            nova_linha = linha + mov_linha
            nova_coluna = coluna + mov_coluna

            if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                casa = tabuleiro[nova_linha][nova_coluna]

                if casa == " ":
                    jogadas.append((nova_linha, nova_coluna))
                elif isinstance(casa, Peca):
                    if casa.cor != self.cor:
                        jogadas.append((nova_linha, nova_coluna))
        return jogadas

class Peao(Peca):
    def __str__(self):
        return "P" if self.cor == "branca" else "p"
    
    def movimento_peao(self, tabuleiro):
        jogadas = []
        if self.cor == "branca":
            direcoes = [(-1,-1),
                        (-1,1)]
        else:
            direcoes = [(1,-1),
                        (1,1)]
        linha, coluna = self.posicao

        for mov_linha, mov_coluna in direcoes:
            nova_linha = linha + mov_linha
            nova_coluna = coluna + mov_coluna

            if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
                casa = tabuleiro[nova_linha][nova_coluna]

                if isinstance(casa, Peca):
                    if casa.cor != self.cor:
                        jogadas.append((nova_linha, nova_coluna))
        if self.cor == "branca":
            nova_linha = linha + (-1)
            nova_coluna = coluna + (0)

            casa = tabuleiro[nova_linha][nova_coluna]
            if self.posicao[0] == 6:
                inicial = tabuleiro[nova_linha - 1][nova_coluna]
                if casa == " ":
                    jogadas.append((nova_linha, nova_coluna))
                    if inicial == " ":
                        jogadas.append((nova_linha - 1, nova_coluna))
            elif casa == " ":
                jogadas.append((nova_linha, nova_coluna))
        else:
            nova_linha = linha + (1)
            nova_coluna = coluna + (0)

            casa = tabuleiro[nova_linha][nova_coluna]
            if self.posicao[0] == 1:
                inicial = tabuleiro[nova_linha + 1][nova_coluna]
                if casa == " ":
                    jogadas.append((nova_linha, nova_coluna))
                    if inicial == " ":
                        jogadas.append((nova_linha + 1, nova_coluna))
            elif casa == " ":
                jogadas.append((nova_linha, nova_coluna))
        return jogadas
