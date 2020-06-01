# Tabuada

numero = int(input('Digite o número que deseja ver a tabuada: '))
print('-'*12)
for i in range(0, 11):
    print('{} x {:2} = {}'.format(numero, i, numero*i))
print('-'*12)
