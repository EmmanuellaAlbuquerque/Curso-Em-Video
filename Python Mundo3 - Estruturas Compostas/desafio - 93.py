# APROVEITAMENTO DE UM JOGADOR DE FUTEBOL
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

'''
jogador = dict()
aproveitamento = list()
nomeJogador = str(input('Nome do Jogador: '))
qPartidas = int(input('Quantidade de partidas: '))
jogador['Nome'] = nomeJogador
somaGols = 0
for i in range(0, qPartidas):
    qGols = int(input(f'Quantidade de Gols na {i}° partida: '))
    aproveitamento.append(qGols)
    somaGols += qGols
jogador['Gols'] = aproveitamento[:]  # sempre uma cópia [:]
jogador['Total de Gols'] = somaGols
print('-='*30)
print(jogador)
print('-='*30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {qPartidas} partidas.')
i = 0
for i in range(0, qPartidas):
    print(f'=> Na partida {i}, fez {jogador["Gols"][i]} gols.')
    i += 1
print(f'Foi um total de {jogador["Total de Gols"]} gols.')
'''