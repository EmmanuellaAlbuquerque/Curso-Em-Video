primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

i = primeiro
while i < (décimo + razão):
    print('{} '.format(i), end='-> ')
    i += razão
print('ACABOU')