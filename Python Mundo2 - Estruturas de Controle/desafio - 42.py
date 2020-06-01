# Pode ou não formar um triângulo
# a + b > c
# b + c > a
# a + c > b

primeiraReta = float(input('Digite o comprimento da primeira reta: '))
segundaReta = float(input('Digite o comprimento da segunda reta: '))
terceiraReta = float(input('Digite o comprimento da terceira reta: '))

if primeiraReta+segundaReta > terceiraReta and \
    segundaReta + terceiraReta > primeiraReta and \
    primeiraReta + terceiraReta > segundaReta:
        print('Existe um triângulo com essas medidas.')

    # O tipo de triangulo que será formado: Equilátero, Isoceles, Escaleno
        if primeiraReta == segundaReta == terceiraReta:
            print('Triângulo equilátero: todos os lados são iguais!')
        # Ou troca para o final e deixa como else, para não ser necessário comparações
        elif (primeiraReta == segundaReta and primeiraReta != terceiraReta) or \
             (primeiraReta == terceiraReta and primeiraReta != segundaReta) or \
             (segundaReta == terceiraReta and segundaReta != primeiraReta):
            print('Triângulo isósceles: dois lado são iguais!')
        # No caso de igualdade não precisa, quando diferente sim
        elif primeiraReta != segundaReta != terceiraReta != primeiraReta:
            print('Triângulo escaleno: todos os lados são diferentes!')

else:
    print('Não existe um triângulo com essas medidas.')
