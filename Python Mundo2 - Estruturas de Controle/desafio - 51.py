''' Mostra os termos de uma PA(progressão aritmética)
    FORMULA: primeiroTermo+(n-1)*razao
'''

''' FORMA 1
print('-='*15)
print('      10 TERMOS DE UMA PA')
print('-='*15)

primeitoTermo = int(input('Digite o primeiro termo da sequência: '))
razao = int(input('Digite a razão da sequência: '))
termo = primeitoTermo

# Mostra os 10 primeiros termos da progressão:
for i in range(1, 11):
    print('{}° termo: {}'.format(i, termo))
    termo = termo + razao
'''

''' FORMA 2 '''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for i in range(primeiro, décimo + razão, razão):
    print('{} '.format(i), end='-> ')
print('ACABOU')
