# APROVEITAMENTO DE UM JOGADOR DE FUTEBOL
time = list()
jogador = dict()
partidas = list()

# ENTRADA DE DADOS
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)

# CABEÇALHO
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

# TABELA COM TODOS AS ENTRADAS/KEYS E VALORES
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')  # k - (i)iterador
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-'*40)

# EXIBE DADOS ESPECÍFICOS
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i , gols in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {gols} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')

'''
jogador = dict()
jogadores = list()
aproveitamento = list()
qQuatJogadores = 0

while True:
    nomeJogador = str(input('Nome do Jogador: '))
    qPartidas = int(input('Quantidade de partidas: '))
    jogador['Nome'] = nomeJogador
    somaGols = 0
    for i in range(0, qPartidas):
        qGols = int(input(f'Quantidade de Gols na {i}° partida: '))
        aproveitamento.append(qGols)
        somaGols += qGols
    jogador['Gols'] = aproveitamento[:]
    jogador['Total de Gols'] = somaGols
    print('-='*30)
    jogadores.append(jogador.copy())
    qQuatJogadores += 1
    aproveitamento.clear()

    desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^51}'.format(' PROGRAMA ENCERRADO COM SUCESSO! '))
        break

print('-='*30)
print(f'{"Cod.":<5}{"Nome.":<10}{"Gols.":<10}{"Total."::<10}')  # alinha a esquerda e dá 10 espaços
i = 0
for item in jogadores:
    print(f'{i}    {item["Nome"]:<6} {item["Gols"]}    {item["Total de Gols"]:}')
    i += 1
while True:
    escolha = int(input('>>> Mostrar dados de qual jogador? [999 p/ sair] '))
    if escolha == 999:
        break
    while escolha > (qQuatJogadores-1) or escolha < 0:
        print('Escolha inválida!')
        escolha = int(input('>>> Mostrar dados de qual jogador? '))
        if escolha == 999:
            break
    print(f'---- Levantamento do jogador {jogadores[escolha]["Nome"]}: ')
    for item in jogadores:
        if item['Nome'] == jogadores[escolha]["Nome"]:
            for i in range(0, len(item['Gols'])):
                print(f'No jogo {i} fez {item["Gols"][i]} gols.')
print('PROGRAMA ENCERRADO')
'''