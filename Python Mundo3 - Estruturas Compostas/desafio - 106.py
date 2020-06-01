from time import  sleep

c = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m',     # 6 - branco
);


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)



'''
# MINI-SISTEMA COM INTERACTIVE HELP


def interactivehelpo():
    print('-='*15)
    print('   SISTEMA DE AJUDA PyHELP  ')
    print('-=' * 15)
    while True:
        print('DIGITE <FIM> SE DESEJA SAIR')
        cmd = str(input('Função ou Biblioteca > '))
        if cmd == 'FIM':
            break
        print('-=' * 20)
        print(f'  Acessando o MANUAL do comando {cmd}  ')
        print('-=' * 20)
        help(cmd)


interactivehelpo()
'''
