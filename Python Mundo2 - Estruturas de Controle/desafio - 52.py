# Número primo

''' FORMA 1
contador = 0
numero = int(input('Digite o NÚMERO que deseja analisar: '))

# Verifica só ele é divisível somente por um e por ele mesmo:
for i in range(1, numero+1):
    if (numero % i) == 0:
        contador = contador + 1
        # print('{}/{}'.format(numero, i))
if contador == 2:
    print('O NÚMERO É PRIMO!')
'''

''' FORMA 2 '''
núm = int(input('Digite um número: '))
total = 0
for i in range(1, núm + 1):
    if núm % i == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[m0 número {} foi divisível {} vezes'.format(núm, total))
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')
