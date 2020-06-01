# Fatorial de um número
from math import factorial
from time import sleep

# FORMA 1
numero = int(input('Digite o número que deseja saber o fatorial: '))
fatorial = 1
i = numero

print('Calculando {}! ='.format(numero), end=' ')
while i > 0:
    print(i, end='')
    print(' X ' if i > 1 else ' = ', end='')
    fatorial = fatorial*i
    i -= 1
    sleep(1)
print('{}'.format(fatorial))

''' FORMA 2
n = int(input('Digite o NÚMERO que deseja saber o FATORIAL: '))
print('O fatorial de {} é {}'.format(n, factorial(n)))
'''