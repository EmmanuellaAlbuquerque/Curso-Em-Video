from random import randint

tuplaNume = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# for numero in tuplaNume:
    #print(f'{numero}', end=' ')
print(f'\nOu NÚMEROS GERADOS: {tuplaNume}\n')
# Menor valor da Tupla
print(f'O MAIOR valor da TUPLA é: {max(tuplaNume)}')

# Maior valor da Tupla
print(f'O MENOR valor da TUPLA é: {min(tuplaNume)}')
'''
maior = menor = tuplaNume[0]
for i in range(0, len(tuplaNume)):
    if tuplaNume[i] > maior:
        maior = tuplaNume[i]
    if tuplaNume[i] < menor:
        menor = tuplaNume[i]
'''
