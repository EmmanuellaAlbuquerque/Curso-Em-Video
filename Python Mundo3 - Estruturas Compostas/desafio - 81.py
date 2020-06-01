lista = list()

while True:
    lista.append(int(input('Digite o NÚMERO desejado: ')))

    desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^51}'.format(' PROGRAMA ENCERRADO COM SUCESSO! '))
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.\n'
      f'Lista em Ordem decrescente{lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
