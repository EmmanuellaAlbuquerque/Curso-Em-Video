núm = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')

'''
listaCompleta = list()
listaPar = list()
listaImpar = list()
for i in range(0, 7):
    valor = int(input('Digite o inteiro: '))
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
listaPar.sort()
listaImpar.sort()
listaCompleta.append(listaPar[:])
listaCompleta.append(listaImpar[:])
print(listaCompleta)
'''