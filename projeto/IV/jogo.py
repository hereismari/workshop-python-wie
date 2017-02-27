# -*- coding: UTF-8 -*-

# Jogo da Velha
# Marianne Linhares, 26/02/2017

'''
    Versao IV - Eita giovanaaaaaa!

'''

def iniciar_jogo():

    nome_jogador1 = raw_input('Insira o nome do jogador 1 (X): ')
    nome_jogador2 = raw_input('Insira o nome do jogador 2 (O): ')

    print 'nome do jogador 1:', nome_jogador1
    print 'nome do jogador 2:', nome_jogador2

    print 'digite:'
    print 'I - Iniciar partida'
    print 'X - Trocar nome do jogador 1 (X)'
    print 'O - Trocar nome do jogador 2 (O)'

    opcao = raw_input()
    if opcao == 'I':
        print 'iniciar partida'
    elif opcao == 'X':
        print 'trocar nome do jogador 1 (X)'
    elif opcao == 'O':
        print 'trocar nome do jogador 2 (O)'
    else:
        print 'Opção inválida'
        # inserir novamente

print '------------------------', 'JOGO DA VELHA', '-------------------------------'

print ('coloque aqui informações sobre o jogo, '
       'e explicação sobre o menu...')

print '----------------------------------------------------------------------'
print 'digite:'
print '----------------------------------------------------------------------'
print '1 - Iniciar nova partida'
print '2 - Visualizar histórico de partidas'
print '3 - Sair'
print '----------------------------------------------------------------------'

opcao_menu = raw_input()

if opcao_menu == '1':
    print 'iniciar jogo'
    iniciar_jogo()
elif opcao_menu == '2':
    print 'visualizar histórico'
elif opcao_menu == '3':
    print 'sair do jogo'
else:
    print 'entrada inválida'
