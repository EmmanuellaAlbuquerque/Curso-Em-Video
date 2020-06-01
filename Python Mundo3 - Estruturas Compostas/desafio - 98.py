# CONTADOR INDEPENDENTE
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for i in range(inicio, fim+1, passo):  # Caso: 1, 10, 1
            print(i, end=' ', flush=True)  # não liga o buffer de tela
            #sleep(0.5)
        print('FIM')
    elif inicio > fim:
        for i in range(inicio, fim - 1, - passo):  # Caso: 90, 40, 10
            print(i, end=' ', flush=True)  # não liga o buffer de tela
            #sleep(0.5)
        print('FIM!')
    print('-=' * 30)


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
