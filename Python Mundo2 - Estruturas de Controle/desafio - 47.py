# Números pares de 1 a 50

''' FORMA 1 '''
print('-='*3, ' NUMEROS PARES ', '-='*3)
for i in range(1, 51):
    if (i % 2) == 0:
        print(i)

''' FORMA 2 '''
print('-='*3, ' NUMEROS PARES ', '-='*3)
# Assim, faz menos repetições usando metade de tempo do processador:
for i in range(2, 51, 2):
    print('.', end='')
    print(i, end=' ')
