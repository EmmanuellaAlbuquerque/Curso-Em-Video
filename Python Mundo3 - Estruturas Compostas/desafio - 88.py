# PALPITES MEGA SENA
from random import randint
palpite = list()
jogo = list()
print('-='*5, ' GERADOS VALORES PARA JOGO DA MEGA SENA', '-='*5)
qJogos = int(input('>>> Quantos jogos devem ser gerados? '))
# GERA OS VALORES PARA O JOGO
for i in range(0, qJogos):
    for elemento in range(0, 6):
        if elemento == 0:
            valor = randint(1, 60)
        else:
            valor = randint(1, 60)
            while valor in palpite:
                valor = randint(1, 60)
        palpite.append(valor)
    jogo.append(palpite[:])
    palpite.clear()
# APRESENTA OS VALORES GERADOS
for i, elemento in enumerate(jogo):
    print(f'Jogo {i+1}: {elemento}')
print('-='*5, 'VALORES GERADOS COM SUCESSO BOA SORTE ', '-='*5)
