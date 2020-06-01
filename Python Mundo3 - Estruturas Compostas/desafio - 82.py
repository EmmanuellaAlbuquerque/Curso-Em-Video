lista = list()
listaPar = list()
listaImpar = list()
while True:
    lista.append(int(input('Digite o valor a ADD na lista: ')))
    desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^51}'.format(' PROGRAMA ENCERRADO COM SUCESSO! '))
        break
for numero in lista:
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
print(f'LISTA ORIGINAL: {lista}\n'
      f'LISTA PAR: {listaPar}\n'
      f'LISTA ÍMPAR: {listaImpar}')
