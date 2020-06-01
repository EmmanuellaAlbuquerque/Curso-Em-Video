# Desconto
# Valor do desconto = Preço original x Desconto em % / 100.

preco = float(input('Digite o preço do produto: '))
novoPreco = preco*(5/100)
print('O novo preço com 5% de desconto é: {:.2f}'.format(preco - novoPreco))
