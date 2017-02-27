# -*- coding: UTF-8 -*-

# Jogo da Velha
# Marianne Linhares, 27/02/2017

'''
    Versao XI
'''

class MatrizJogoDaVelha():

    matriz = []

    NUM_LINHAS = 3
    NUM_COLUNAS = 3

    def __init__(self):
        self._criar()

    def _criar(self):
        for i in range(self.NUM_LINHAS):
            self.matriz.append([])
            for j in range(self.NUM_COLUNAS):
                self.matriz[i].append(' ')

    def limpar(self):
        self.matriz = []
        self._criar()

    def desenhar(self):
        print
        print 'Matriz:'
        for i in range(self.NUM_LINHAS):
            for j in range(self.NUM_COLUNAS):
                print '|', self.matriz[i][j], '|',
            print
        print

    def mudar(self, linha, coluna, simbolo):
        if self.validar(linha, coluna):
            self.matriz[linha][coluna] = simbolo
            return True
        else:
            return False

    def vazia(self, linha, coluna):
        if self.validar(linha, coluna):
            return self.matriz[linha][coluna] == ' '
        else:
            return True

    def ganhou(self, simbolo):
        def checa_colunas():
            # verifica colunas
            for i in range(self.NUM_LINHAS):
                res = True # inicialmente consideramos que é verdade
                for j in range(self.NUM_COLUNAS):
                    res = res and self.matriz[i][j] == simbolo # so continuará sendo verdade se a coluna inteira for igual ao simbolo
                if res:
                    return True

            return False

        def checa_linhas():
            # verifica linhas
            for j in range(self.NUM_COLUNAS):
                res = True # inicialmente consideramos que é verdade
                for i in range(self.NUM_LINHAS):
                    res = res and self.matriz[i][j] == simbolo # so continuará sendo verdade se a linha inteira for igual ao simbolo
                if res:
                    return True

            return False

        def checa_diagonais():
            # verifica diagonal 1
            i = 0
            j = 0
            res = True
            while i < self.NUM_LINHAS and j < self.NUM_COLUNAS:
                res = res and self.matriz[i][j] == simbolo
                i += 1
                j += 1
            if res:
                return True

            # verifica diagonal 2
            i = 0
            j = self.NUM_COLUNAS - 1
            res = True
            while i < self.NUM_LINHAS and j >= 0:
                res = res and self.matriz[i][j] == simbolo
                i += 1
                j -= 1
            if res:
                return True

            return False

        return checa_linhas() or checa_colunas() or checa_diagonais()

    def empate(self):
        if not self.ganhou('X') and not self.ganhou('O'):
            cont = 0
            for i in range(self.NUM_LINHAS):
                for j in range(self.NUM_COLUNAS):
                    if not self.vazia(i, j):
                        cont += 1

            return cont == 9
        else:
            return False

    def get_resultado(self):
        if self.ganhou('X'):
            return 'X'
        elif self.ganhou('O'):
            return 'O'
        else:
            return 'empate'

    def validar(self, linha, coluna):
        return linha >= 0 and linha < self.NUM_LINHAS and coluna >= 0 and coluna < self.NUM_COLUNAS and self.vazia(linha, coluna)

    def vazia(self, linha, coluna):
        return self.matriz[linha][coluna] == ' '
