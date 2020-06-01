# ADICIONAR ELEMENTOS NA LISTA SEM DUPLICAR E ORDENAR

lista = list()
while True:
    valor = int(input('Digite o valor NUMÉRICO: '))
    if valor in lista:
        print('Esse valor já se encontra na LISTA')
    else:
        lista.append(valor)
    desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^51}'.format(' PROGRAMA ENCERRADO COM SUCESSO! '))
        break
lista.sort()
print(f'CONTEÚDO DA LISTA: {lista}')
