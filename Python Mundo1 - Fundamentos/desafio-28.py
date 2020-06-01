# Dado um número aleatória, mostra se vc acertou ou errou o número
import random
from time import sleep

numero = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
escolha = int(input('Digite um número, de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if numero == escolha:
    print('Você venceu!')
else:
    print('Você perdeu!')
print('Randomico: {}, Escolhido: {}'.format(numero, escolha))
