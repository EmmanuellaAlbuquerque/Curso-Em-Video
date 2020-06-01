primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))

if primeiro > segundo:
    print('O primeiro é maior que o segundo!')
elif segundo > primeiro:
    print('O segundo é maior que o primeiro!')
elif primeiro == segundo:
    print('Não existe valor maior, os 2 são iguais')
