# -*- coding: UTF-8 -*-

# Jogo da Velha
# Marianne Linhares, 26/02/2017

'''
    Versao III
'''

def iniciar_jogo():

    nome_jogador1 = raw_input('Insira o nome do jogador 1 (X): ')
    nome_jogador2 = raw_input('Insira o nome do jogador 2 (O): ')

    print 'jogador1', nome_jogador1
    print 'jogador2', nome_jogador2


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
