# Soma dos números até condição de parada

numeros = 1.0
soma = 0
i = 1

print('Digite todos os números que deseja SOMAR ')
numeros = float(input('Digite o {}° número, para PARAR digite [999]: '.format(i)))
while numeros != 999:
    soma = soma + numeros
    numeros = float(input('Digite o {}° número, para PARAR digite [999]: '.format(i)))
    i += 1
print('A soma de TODOS os {} números inseridos é {}'.format(i-1, soma))
