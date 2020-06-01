# Maior e Menor peso lido: Análise de Dados

maiorPeso = 0
# menorPeso = 1000000000 gambiarra
menor = 0

for i in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(i)))
    if i == 1:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso
print('O MAIOR peso é {}Kg\nO MENOR peso é {}Kg'.format(maiorPeso, menorPeso))

'''
OU
pesos = [float(input('Informe o peso da pessoa {}: '.format(c+1))) for c in range(5)]
print('Maior peso: {}'.format(max(pesos)))
print('Menor peso: {}'.format(min(pesos)))
'''