from random import  randint
from time import  sleep
from operator import  itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# key=itemgetter()- 0 para ordem de chaves
# key=itemgetter()- 1 para ordem de valores
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
# SORTED RETORNA UMA LISTA, assim pode tratar como uma
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

'''
from random impo'rt randint

# GERA VALORES ALEATÓRIOS PARA 4 JOGADORES
jogador1 = randint(1, 6)
jogador2 = randint(1, 6)
jogador3 = randint(1, 6)
jogador4 = randint(1, 6)

# INICIA O DICIONÁRIO
jogadores = {'Jogador1': jogador1, 'Jogador2': jogador2,
             'Jogador3': jogador3, 'Jogador4': jogador4}
temp = dict()
print(jogadores)
print('-='*30)

print('Ranking dos jogadores: ')
maior = jogador1
i = 0

for i in range(0, 4):  # loop repete 4 vezes p/ 4 jogadores
    for key, value in jogadores.items():  # loop para determinar o maior valor de dado jogado
        if value >= maior:
            maior = value
    # print(maior)
    for key, value in jogadores.items():  # loop p/ encontrar novamente esse valor
        if value == maior:
            temp[key] = value  # adiciona-lo na lista temporária
            del jogadores[key]  # deleta-lo da lista principal
            break
    maior = 0  # zera o maior p/ iniciar uma nova busca

i = 0
for key, value in temp.items():  # loop para percorrer a nova lista temporária com os valores em ordem
    print(f'{i+1}° lugar: {key} com {value}')
    i += 1
'''