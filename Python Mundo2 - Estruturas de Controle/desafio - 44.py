print(' {:=^40}' .format(' GERENCIANDO PAGAMENTO '))
preco = float(input('Digite o preço do produto: '))

print(' {:=^40}' .format(' FORMAS DE PAGAMENTO '))
print('[ 1 ] - à vista dinheiro/cheque\n'
      '[ 2 ] - à vista no cartão\n'
      '[ 3 ] - 2x no cartão\n'
      '[ 4 ] - 3x ou mais no cartão\n')

condicaoDePagamento = int(input('Digite a condição de pagamento do menu: '))

if condicaoDePagamento == 1:
    # 10% de desconto
    desconto = (preco*10)/100
    novoPreco = preco - desconto
elif condicaoDePagamento == 2:
    # 5% de desconto
    desconto = (preco*5)/100
    novoPreco = preco - desconto
elif condicaoDePagamento == 3:
    novoPreco = preco
    parcela = novoPreco/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))

elif condicaoDePagamento == 4:
    # juros de 20%
    juros = (preco*20)/100
    novoPreco = preco + juros
    qparcelas = int(input('Deseja dividir em quantas parcelas? '))
    parcelas = novoPreco/qparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qparcelas, parcelas))
else:
    novoPreco = preco
    print('Condição Inválida!')
print('Sua compra terá o novo valor de R${:.2f}'.format(novoPreco))
