# Percorrido: Preço a pagar = 60*dias + 0,15*km
# R$ 60 - 1 dia
# R$0,15 - 1 Km

percorrido = float(input('Descreva a quantidade de Km percorridos por um carro alugado: '))
dias = int(input('Descreva a quantidade de dias pelos quais ele foi alugado: '))
preco = 60*dias + 0.15*percorrido
print('O preço total a pagar é de: {:.2f}'.format(preco))
