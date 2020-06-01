import sys

escolha = 1
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

while escolha != 5:

    print('-='*20,
'''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] para sair do programa
''',
'-='*20)
    escolha = int(input('>>>> Digite a operação que deseja realizar: '))

    if escolha == 1:
        soma = valor1 + valor2
        print('Soma: {}+{} = {}'.format(valor1, valor2, soma))
    elif escolha == 2:
        mul = valor1 * valor2
        print('Multiplicação: {}X{} = {}'.format(valor1, valor2, mul))
    elif escolha == 3:
        print('Verificando maior: ')
        maior = menor = valor1
        if valor2 > maior:
            maior = valor2
        print('Entre {} e {} o maior valor é {}'.format(valor1, valor2, maior))
    elif escolha == 4:
        print('Escolha seus novos números ')
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
sys.exit('PROGRAMA ENCERRADO! ')
