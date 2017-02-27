# -*- coding: UTF-8 -*-

# Jogo da Velha
# Marianne Linhares, 27/02/2017

'''
    Versao IX
'''

NUM_LINHAS = 3
NUM_COLUNAS = 3

def imprimir_menu():
    print
    print
    print '------------------------', 'JOGO DA VELHA', '-------------------------------'

    print ('coloque aqui informações sobre o jogo, '
           'e explicação sobre o menu...')

def opcoes_menu():
    print
    print
    print '----------------------------------------------------------------------'
    print 'digite:'
    print '----------------------------------------------------------------------'
    print '1 - Iniciar nova partida'
    print '2 - Visualizar histórico de partidas'
    print '3 - Sair'
    print '----------------------------------------------------------------------'

    opcao_menu = raw_input()
    return opcao_menu

def opcoes_nome_jogadores(nome_jogador1, nome_jogador2):
    print
    print
    print '----------------------------------------------------------------------'
    print 'nome do jogador 1:', nome_jogador1
    print 'nome do jogador 2:', nome_jogador2
    print '----------------------------------------------------------------------'
    print 'digite:'
    print '----------------------------------------------------------------------'
    print 'I - Iniciar partida'
    print 'X - Trocar nome do jogador 1 (X)'
    print 'O - Trocar nome do jogador 2 (O)'
    print '----------------------------------------------------------------------'

    opcao_nome_jogador = raw_input()
    return opcao_nome_jogador

def perguntar_nome_jogadores():

    opcao = None

    while opcao != 'I':

        if opcao is None or opcao == 'X':
            nome_jogador1 = raw_input('Insira o nome do jogador 1 (X): ')
        if opcao is None or opcao == 'O':
            nome_jogador2 = raw_input('Insira o nome do jogador 2 (O): ')

        opcao = opcoes_nome_jogadores(nome_jogador1, nome_jogador2)
        if opcao == 'I':
            print 'iniciar partida'
        elif opcao == 'X':
            print 'trocar nome do jogador 1 (X)'
        elif opcao == 'O':
            print 'trocar nome do jogador 2 (O)'
        else:
            opcao = None
            print 'Opção inválida'

    return nome_jogador1, nome_jogador2

def criar_matriz():
    # matriz inicialmente vazia
    matriz = []
    for i in range(NUM_LINHAS):
        matriz.append([])
        for j in range(NUM_COLUNAS):
            matriz[i].append(' ')

    return matriz

def desenhar_matriz(matriz):
    print
    print 'Matriz:'
    for i in range(NUM_LINHAS):
        for j in range(NUM_COLUNAS):
            print '|', matriz[i][j], '|',
        print
    print

def mudar_matriz(matriz, x, y, simbolo):
    matriz[x][y] = simbolo

def vazia(matriz, linha, coluna):
    return matriz[linha][coluna] == ' '

def ganhou(matriz, simbolo):

    # verifica colunas
    for i in range(NUM_LINHAS):
        res = True # inicialmente consideramos que é verdade
        for j in range(NUM_COLUNAS):
            res = res and matriz[i][j] == simbolo # so continuará sendo verdade se a coluna inteira for igual ao simbolo
        if res:
            return True

    # verifica linhas
    for j in range(NUM_COLUNAS):
        res = True # inicialmente consideramos que é verdade
        for i in range(NUM_LINHAS):
            res = res and matriz[i][j] == simbolo # so continuará sendo verdade se a linha inteira for igual ao simbolo
        if res:
            return True

    # verifica diagonal 1
    i = 0
    j = 0
    res = True
    while i < NUM_LINHAS and j < NUM_COLUNAS:
        res = res and matriz[i][j] == simbolo
        i += 1
        j += 1
    if res:
        return True

    # verifica diagonal 2
    i = 0
    j = NUM_COLUNAS - 1
    res = True
    while i < NUM_LINHAS and j >= 0:
        res = res and matriz[i][j] == simbolo
        i += 1
        j -= 1
    if res:
        return True

    return False

def empate(matriz):

    if not ganhou(matriz, 'X') and not ganhou(matriz, 'O'):

        cont = 0
        for i in range(NUM_LINHAS):
            for j in range(NUM_COLUNAS):
                if not vazia(matriz, i, j):
                    cont += 1

        return cont == 9

def terminou(matriz):
    return ganhou(matriz, 'X') or ganhou(matriz, 'O') or empate(matriz)

def get_resultado(matriz):
    if ganhou(matriz, 'X'):
        return 'X'
    elif ganhou(matriz, 'O'):
        return 'O'
    else:
        return 'empate'

def validar(linha, coluna, matriz):
    return linha >= 0 and linha < NUM_LINHAS and coluna >= 0 and coluna < NUM_COLUNAS and vazia(matriz, linha, coluna)

def jogar(jogador, nome, matriz):

    if jogador == 1:
        simbolo = 'X'
    else:
        simbolo = 'O'

    print
    print '------------------------- Esperando jogada.... ----------------------'
    print '%s (Jogador %d), insira 2 números entre 0 e 2. O primeiro para a linha e o segundo para a coluna:' % (nome, jogador),

    linha, coluna = map(int, raw_input().split())

    if validar(linha, coluna, matriz):
        print 'Jogada realizada!'
        mudar_matriz(matriz, linha, coluna, simbolo)
        desenhar_matriz(matriz)
    else:
        print 'Linha ou coluna inválida! Tente novamente!'
        jogar(jogador, nome, matriz)

def iniciar_jogo():
    nome_jogador1, nome_jogador2 = perguntar_nome_jogadores()

    matriz = criar_matriz()

    while not terminou(matriz):
        desenhar_matriz(matriz)

        jogar(1, nome_jogador1, matriz)
        jogar(2, nome_jogador2, matriz)

    resultado = get_resultado(matriz)

    if resultado == 'empate':
        print 'Deu velha, Empate!!!'
    elif resultado == 'X':
        print 'Parabéns %s!!!' % nome_jogador1
    elif resultado == 'O':
        print 'Parabéns %s!!!' % nome_jogador2

def jogo_da_velha():

    imprimir_menu()

    opcao_menu = opcoes_menu()
    if opcao_menu == '1':
        print 'iniciar jogo'
        iniciar_jogo()
    elif opcao_menu == '2':
        print 'visualizar histórico'
    elif opcao_menu == '3':
        print 'sair do jogo'
    else:
        print 'entrada inválida'

if __name__ == '__main__':
    jogo_da_velha()