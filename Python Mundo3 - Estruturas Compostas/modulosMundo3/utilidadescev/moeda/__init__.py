def aumentar(num, porcentagem, formatado=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param num: o preço que se quer reajustar.
    :param porcentagem: qual é a porcentagem do aumento.
    :param formatado: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    numero = num + (num*(porcentagem/100))
    return numero if formatado is False else moeda(numero)


def diminuir(num, porcentagem, formatado=False):
    numero = num - (num * (porcentagem / 100))
    return numero if formatado is False else moeda(numero)


def dobro(num, formatado=False):
    numero = num * 2
    return numero if formatado is False else moeda(numero)


def metade(num, formatado=False):
    numero = num/2
    return numero if formatado is False else moeda(numero)


def moeda(num, tipo='R$'):
    return f'{tipo}{num:>.2f}'.replace('.', ',')


def resumo(num=0, aumento=10, redução=5):
    print('-' * 30, '\n', 'RESUMO DE VALOR'.center(30))
    print('-' * 30)
    print(f' Preço analisado: \t{moeda(num)}\n',
          f'Dobro do Preço: \t{dobro(num, True)}\n',
          f'Metade do preço: \t{metade(num, True)}\n',
          f'{aumento}% de aumento: \t{aumentar(num, aumento, True)}\n',
          f'{redução}% de redução: \t{diminuir(num, redução, True)}',
          )
    print('-'*30)
