# JOGO PAR OU ÍMPAR
from random import randint
count = 0
while True:
    print('-='*20)
    print('JOGO DO PAR OU ÍMPAR')
    print('-=' * 20)
    entradaUsuario = int(input('Diga um valor: '))
    while entradaUsuario < 0 or entradaUsuario > 10:
        entradaUsuario = int(input('Tente Novamente, entrada inválida. Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('>>> Escolhe PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    entradaComputador = randint(0, 10)
    soma = entradaUsuario + entradaComputador
    if escolha == 'P':
        if (soma % 2) == 0:
            print(f'Você jogou {entradaUsuario} e o computador jogou '
                  f'{entradaComputador}. TOTAL deu {soma} '
                  f'[PAR]. Você VENCEU!')
        else:
            print(f'Você jogou {entradaUsuario} e o computador jogou '
                  f'{entradaComputador}. TOTAL deu {soma} '
                  f'[ÍMPAR]. Você PERDEU!')
            print(f'GAME OVER! Você VENCEU {count} vezes.')
            break
    elif escolha == 'I':
        if (soma % 2) == 0:
            print(f'Você jogou {entradaUsuario} e o computador jogou '
                  f'{entradaComputador}. TOTAL deu {soma} '
                  f'[PAR]. Você PERDEU!')
            print(f'GAME OVER! Você VENCEU {count} vezes.')
            break
        else:
            print(f'Você jogou {entradaUsuario} e o computador jogou '
                  f'{entradaComputador}. TOTAL deu {soma} '
                  f'[ÍMPAR]. Você VENCEU!')
    print('VAMOS JOGAR NOVAMENTE...')
    count += 1
