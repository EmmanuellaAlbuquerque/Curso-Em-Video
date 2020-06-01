print('-='*30)
print(' '*13, 'GERADOR DE PROGRESSÃO ARITMÉTICA')
print('-='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
i = primeiro

quantidade = total = 10
qtermos = i + (quantidade - 1) * razão
while quantidade != 0:
    while i < (qtermos + razão):
        print('{} '.format(i), end='-> ')
        i += razão
    print('PAUSA', end='')
    quantidade = int(input('\nDeseja ver mais termos? Digite a quantidade de termos a mais: '))
    total += quantidade
    qtermos = i + (quantidade - 1) * razão
print('FIM')
print('Progressão finalizada com {} termos mostrados!'.format(total))
