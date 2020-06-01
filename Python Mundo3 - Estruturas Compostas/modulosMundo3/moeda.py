def aumentar(num, porcentagem, formatado=False):
    numero = num + (num*(porcentagem/100))
    if formatado:
        return moeda(numero)
    else:
        return numero


def diminuir(num, porcentagem, formatado=False):
    numero = num - (num * (porcentagem / 100))
    if formatado:
        return moeda(numero)
    else:
        return numero


def dobro(num, formatado=False):
    numero = num * 2
    if formatado:
        return moeda(numero)
    else:
        return numero


def metade(num, formatado=False):
    numero = num/2
    if formatado:
        return moeda(numero)
    else:
        return numero


def moeda(num):
    return f'R${num:.2f}'


def resumo(num, aumento, redução):
    print('-' * 30, '\n', '       RESUMO DE VALOR')
    print('-' * 30)
    print(f' Preço analisado: {moeda(num)}\n'.replace('.', ','),
          f'Dobro do Preço: {dobro(num, formatado=True)}\n'.replace('.', ','),
          f'Metade do preço: {metade(num, formatado=True)}\n'.replace('.', ','),
          f'{aumento}% de aumento: {aumentar(num, aumento, formatado=True)}\n'.replace('.', ','),
          f'{redução}% de redução: {diminuir(num, redução, formatado=True)}'.replace('.', ','),
          )
    print('-'*30)
