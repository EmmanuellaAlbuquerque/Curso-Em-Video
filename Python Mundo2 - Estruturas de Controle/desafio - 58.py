# Dado um número aleatória, mostra se vc acertou ou errou o número

import random
from time import sleep

numero = random.randint(0, 10)
count = 0
escolha = 15

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
print('-=-' * 20)
# while not acetou/ acertou = false /

while numero != escolha:
    escolha = int(input('Digite um número, de 0 a 10: '))
    print('PROCESSANDO...')
    if escolha > numero:
        print('Menos... Tente novamente!')
    elif escolha < numero:
        print('Mais... Tente Novamente!')
    count += 1
print('Foram necessários {} PALPITES para VENCER!'.format(count))
