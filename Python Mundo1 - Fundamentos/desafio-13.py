# Desconto salarial
# Valor do desconto = Preço original x Desconto em % / 100.

preco = float(input('Digite o preço do produto: '))
novoPreco = preco*(15/100)

print('O salário com 15% de aumento é: {:.2f}'.format(preco+novoPreco))
print('Logo, o aumento em si foi de: {:.2f}'.format(novoPreco))
