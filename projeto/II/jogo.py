# -*- coding: UTF-8 -*-

# Jogo da Velha
# Marianne Linhares, 26/02/2017

'''
    Versao II
'''

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
elif opcao_menu == '2':
    print 'visualizar histórico'
elif opcao_menu == '3':
    print 'sair do jogo'
else:
    print 'entrada inválida'
