# Tupla com valores do teclado

#tuplaValor = (int(input('Digite o 1° valor: ')), int(input('Digite o 2° valor: ')),
# int(input('Digite o 3° valor: ')), int(input('Digite o 4° valor: '))) OU
tuplaValor = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))

# A: Quantas vezes o valor 9 apareceu?
print(f'O valor 9 apareceu {tuplaValor.count(9)} VEZES.')

# B: Em que posição foi digitado o primeiro valor 3?
if tuplaValor.count(3) > 0:  # OU if 3 in tuplaValor
    pos = tuplaValor.index(3)
    print(f'Primeira aparição do 3 na POSIÇÃO {pos+1}.')
else:
    pos = 0
    print('O VALOR 3 não foi digitado em nenhuma POSIÇÃO')

# C: Quais foram os números pares?
print(f'PARES da tupla: ', end='')
for valor in tuplaValor:
    if valor % 2 == 0:
        print(f'{valor}', end=' ')
