cidade = str(input('Digite o nome de uma cidade: '))
cidade = cidade.upper()
lista = cidade.split()
print('Começa com SANTO?, {}!'.format('SANTO'in lista[0]))