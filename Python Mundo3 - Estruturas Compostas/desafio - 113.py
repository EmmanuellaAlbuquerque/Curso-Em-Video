def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


numInteiro = leiaInt('Digite um valor \033[32mINTEIRO\033[m: ')
print(f'O valor \033[31mINTEIRO\033[m digitado foi {numInteiro}')
numFloat = leiaFloat('Digite um valor \033[32mREAL\033[m: ')
print(f'O valor \033[31mREAL\033[m digitado foi {numFloat}')




























'''
def leiaInt(msg=''):
    print(msg, end='')
    try:
        numero = str(input())
        while True:
            if not isInt(numero):
                print('\033[0;31mERRO!', msg, end='\033[m')
                numero = input()
            else:
                print(f'O valor inteiro digitado foi {numero}')
                return numero
    except KeyboardInterrupt:
        print('\033[0;31mUsuário preferiu não digitar esse número.\n', end='\033[m')
        print(f'O valor inteiro digitado foi 0')


def leiaFloat(msg=''):
    print(msg, end='')
    try:
        numero = str(input())
        while True:
            if not isFloat(numero):
                print('\033[0;31mERRO!', msg, end='\033[m')
                numero = input()
            else:
                print(f'O valor inteiro digitado foi {numero}')
                return numero
    except KeyboardInterrupt:
        print('\033[0;31mUsuário preferiu não digitar esse número.\n', end='\033[m')
        print(f'O valor inteiro digitado foi 0')


def isFloat(valor):  # or: isinstance(y, float)-> retorna True ou False
    try:
        float(valor)
    except ValueError:
        return False
    return True


def isInt(valor):  # or: isinstance(y, float)-> retorna True ou False
    try:
        int(valor)
    except ValueError:
        return False
    except KeyboardInterrupt:
        return False
    return True


# Programa Principal
print('-'*15)
n = leiaInt('Digite um número inteiro : ')
n = leiaFloat('Digite um número float : ')
'''