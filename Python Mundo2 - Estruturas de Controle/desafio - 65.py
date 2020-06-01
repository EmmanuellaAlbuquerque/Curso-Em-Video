i = 1
media = soma = count = menorValor = maiorValor = 0
desejaContinuar = 'S'
while desejaContinuar in 'Ss':
    numero = float(input('Digite o {}° número: '.format(i)))
    # Calcula a soma de todos os números inseridos
    soma = soma + numero

    # Analisa o MAIOR e MENOR valor lido
    if i == 1:
        maiorValor = numero
        menorValor = numero
    elif numero > maiorValor:
        maiorValor = numero
    elif numero < menorValor:
        menorValor = numero

    desejaContinuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    i += 1
    count += 1
print('A MÉDIA dos {} números é {}'.format(i - 1, soma/count))
print('O MAIOR valor é {} e o MENOR valor é {}'.format(maiorValor, menorValor))
