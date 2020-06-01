def leiaint(msg=''):
    print(msg, end='')
    número = input()
    while True:
        if not número.isnumeric():
            print('\033[0;31mERRO!', msg, end='\033[m')
            número = input()
        else:
            return número


# Programa Principal
print('-'*15)
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
