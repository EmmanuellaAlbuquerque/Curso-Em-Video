# Pode ou não formar um triângulo
# a+b > c
# b+c > a
# a+c > b

primeiraReta = float(input('Digite o comprimento da primeira reta: '))
segundaReta = float(input('Digite o comprimento da segunda reta: '))
terceiraReta = float(input('Digite o comprimento da terceira reta: '))

if primeiraReta+segundaReta > terceiraReta:
    if segundaReta + terceiraReta > primeiraReta:
        if primeiraReta + terceiraReta > segundaReta:
            print('Existe um triângulo com essas medidas.')
else:
    print('Não existe um triângulo com essas medidas.')


if primeiraReta+segundaReta > terceiraReta and segundaReta + terceiraReta > primeiraReta and primeiraReta + terceiraReta > segundaReta:
    print('Existe um triângulo com essas medidas.')
else:
    print('Não existe um triângulo com essas medidas.')