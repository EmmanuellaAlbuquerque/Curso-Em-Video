#
soma = 0
count = 0
for i in range(1, 7):
    numero = int(input('Digite o {}° numero: '.format(i)))
    # Caso seja um número par:
    if (numero % 2) == 0:
        soma = soma + numero
        count = count + 1
print('A soma DOS {} NÚMEROS PARES é: {}'.format(count, soma))
