''' FORMA 1
numero = int(input('Digite um número inteiro: '))
baseDeConversao = int(input('Digite a base de conversão:\n1 - para binário\n2 - para octal\n3 - para hexadecimal\n'))

if baseDeConversao == 1:
    print('Conversão para binário: ')

    binario = []
    dividendo = numero
    divisor = 2

    resultTemp = int(dividendo / divisor)

    while resultTemp != 0:
        resto = dividendo % divisor
        dividendo = resultTemp
        binario.insert(0, resto)
        resultTemp = int(dividendo / divisor)
    binario.insert(0, dividendo % divisor)
    print(binario)

elif baseDeConversao == 2:
    print('Conversão para octal: ')

    octal = []
    dividendo = numero
    divisor = 8

    resultTemp = int(dividendo / divisor)

    while resultTemp != 0:
        resto = dividendo % divisor
        dividendo = resultTemp
        octal.insert(0, resto)
        resultTemp = int(dividendo / divisor)
    octal.insert(0, dividendo % divisor)
    print(octal)

elif baseDeConversao == 3:
    print('Conversão para hexadecimal')

    hexadecimal = []
    dividendo = numero
    divisor = 16

    resultTemp = int(dividendo / divisor)
    resto = dividendo % divisor

    while resultTemp != 0:
        hexadecimal.insert(0, resto)
        dividendo = resultTemp
        resultTemp = int(dividendo / divisor)
        resto = dividendo % divisor
    hexadecimal.insert(0, dividendo % divisor)

    for i in range(len(hexadecimal)):
        if hexadecimal[i] == 10:
            hexadecimal[i] = 'A'
        elif hexadecimal[i] == 11:
            hexadecimal[i] = 'B'
        elif hexadecimal[i] == 12:
            hexadecimal[i] = 'C'
        elif hexadecimal[i] == 13:
            hexadecimal[i] = 'D'
        elif hexadecimal[i] == 14:
            hexadecimal[i] = 'E'
        elif hexadecimal[i] == 15:
            hexadecimal[i] = 'F'
    print(hexadecimal)
else:
    print('Opção inválida!')
'''

# FORMA 2
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    # Tirando os 2 termos da string que especifica o tipo. Ex.: 0o, 0b, 0x(indica hexadecimal)
    print('{} convertido para BINÁRIO  é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL  é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida! Tente novamente!')