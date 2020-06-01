def fatorial(num=1, show=False):  # show: valor lógico opcional
    '''
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.(resultado)
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='' ' X ' if c > 1 else '')
            if c == 1:
                print(' = ', end='')
    return f


# Programa Principal
print(fatorial(6, True))
