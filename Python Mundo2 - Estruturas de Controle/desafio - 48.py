# Soma dos ímpares múltiplos de 3

# FORMA 1
soma = 0
for i in range(1, 501):
    # Se ele é ímpar
    if (i % 2) != 0:
        # Um número é múltiplo de 3 quando o resto de sua divisão por 3 é zero
        if (i % 3) == 0:
            soma = soma + i
print('A soma DOS ÍMPARES MULTIPLOS de 3 é: {}'.format(soma))

soma = 0
count = 0
# FORMA 2 - diminui processamento:
for i in range(1, 501, 2):
    if i % 3 == 0:
        count = count + 1
        soma = soma + i
print('A soma de todos os {} valores solicitados é {}'.format(count, soma))
