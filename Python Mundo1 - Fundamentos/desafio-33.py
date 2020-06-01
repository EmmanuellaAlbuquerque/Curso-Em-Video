# Número maior e menor

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
maior = n1
menor = n1
if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é: {}'.format(maior))
if n1 < menor:
    menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O menor número é: {}'.format(menor))

'''
# Verificando quem é o menor:
menor =  n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
'''