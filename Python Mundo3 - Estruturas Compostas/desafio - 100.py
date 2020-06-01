def sorteia(lista):
    from random import randint
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Sorteando 5 valores para a lista: {lista}')


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista} temos {soma}.')


# Programa Principal
números = list()
sorteia(números)
somaPar(números)
