# Sequência de Fibonacci
print('-='*30, '\n', ' '*20, 'SEQUÊNCIA DE FIBONACI\n', '-='*30)
n = int(input('>>>> Quantidade da sequência que você deseja ver: '))
i = 0
anterior = 0
atual = 1
print('{} -> {} -> '.format(anterior, atual), end='')

i = 3  # caso 0 + 1 + 1
while i <= n:
    proximo = atual + anterior
    print('{} -> '.format(proximo), end='')
    anterior = atual
    atual = proximo
    i += 1
print('ACABOU!')
