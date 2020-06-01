# GAME JOKENPÔ

''' FORMA 1
import random

lista = ['pedra', 'papel', 'tesoura']
palavra = random.choice(lista)

escolhaDoUsuario = str(input('Digite sua escolha: pedra, papel ou tesoura: '))
print('A escolha do computador foi {}.'.format(palavra))

if escolhaDoUsuario != 'pedra' and escolhaDoUsuario != 'papel' and escolhaDoUsuario != 'tesoura':
    print('Você escolheu uma entrada inválida!')

# Entrada Usuário - Computador
# Caso entradas iguais:
if escolhaDoUsuario == palavra:
    print('Entradas iguais!')

# Caso Pedra - Papel:
elif escolhaDoUsuario == 'pedra' and palavra == 'papel':
    print('COMPUTADOR GANHOU!')
elif escolhaDoUsuario == 'papel' and palavra == 'pedra':
    print('USUÁRIO GANHOU!')

# Caso Papel - Tesoura
elif escolhaDoUsuario == 'papel' and palavra == 'tesoura':
    print('COMPUTADOR GANHOU!')
elif escolhaDoUsuario == 'tesoura' and palavra == 'papel':
    print('USUÁRIO GANHOU!')

# Caso Pedra - Tesoura
elif escolhaDoUsuario == 'tesoura' and palavra == 'pedra':
    print('COMPUTADOR GANHOU!')
elif escolhaDoUsuario == 'pedra' and palavra == 'tesoura':
    print('USUÁRIO GANHOU!')
'''

''' FORMA 2 '''
from random import randint
import sys
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PÔ!!!')
# computador jogou PEDRA
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        sys.exit('JOGADA INVÁLIDA!')
# computador jogou PAPEL
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        sys.exit('JOGADA INVÁLIDA!')
# computador jogou TESOURA
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        sys.exit('JOGADA INVÁLIDA!')
print('-='*15)
print(' Computador jogou {}'.format(itens[computador]))
print(' Jogador jogou {}'.format(itens[jogador]))
print('-='*15)
