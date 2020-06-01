'''
def leiaDinheiro(msg):
    # Validação de dados
    while True:
        valor = input(msg)
        valor = valor.replace(',', '.')
        if not isFloat(valor) and not valor.isnumeric():
            print(f'ERRO. <{valor}> é um preço inválido!')
        else:
            break
    return float(valor)


def isFloat(valor):  # or: isinstance(y, float)-> retorna True ou False
    try:
        float(valor)
    except ValueError:
        return False
    return True
'''

def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mErro! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor
