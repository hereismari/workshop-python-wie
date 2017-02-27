# -*- coding: UTF-8 -*-

# Jogo da Velha
# Marianne Linhares, 27/02/2017

'''
    Versao X
'''

from matriz import MatrizJogoDaVelha

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

def jogar(jogador, nome, matriz):

    if jogador == 1:
        simbolo = 'X'
    else:
        simbolo = 'O'

    print
    print '------------------------- Esperando jogada.... ----------------------'
    print '%s (Jogador %d), insira 2 números entre 0 e 2. O primeiro para a linha e o segundo para a coluna:' % (nome, jogador),

    linha, coluna = map(int, raw_input().split())

    res = matriz.mudar(linha, coluna, simbolo)
    if res:
        print 'Jogada realizada!'
        matriz.desenhar()
    else:
        print 'Linha ou coluna inválida! Tente novamente!'
        jogar(jogador, nome, matriz)

def iniciar_jogo(matriz):

    nome_jogador1, nome_jogador2 = perguntar_nome_jogadores()

    while True:
        matriz.desenhar()

        jogar(1, nome_jogador1, matriz)
        if matriz.ganhou('X') or matriz.empate():
            break
        jogar(2, nome_jogador2, matriz)
        if matriz.ganhou('O') or matriz.empate():
            break

    resultado = matriz.get_resultado()

    if resultado == 'empate':
        print 'Deu velha, Empate!!!'
    elif resultado == 'X':
        print 'Parabéns %s!!!' % nome_jogador1
    elif resultado == 'O':
        print 'Parabéns %s!!!' % nome_jogador2

def jogo_da_velha(matriz):

    imprimir_menu()

    opcao_menu = opcoes_menu()
    if opcao_menu == '1':
        print 'iniciar jogo'
        iniciar_jogo(matriz)
    elif opcao_menu == '2':
        print 'visualizar histórico'
    elif opcao_menu == '3':
        print 'sair do jogo'
    else:
        print 'entrada inválida'

if __name__ == '__main__':
    matriz = MatrizJogoDaVelha()
    jogo_da_velha(matriz)
