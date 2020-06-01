gasto = mil = maisBarato = count = 0
nomeBarato = '[VAZIO]'
print('---------------- LOJÃO BARATÃO ---------------')

while True:
    nome = str(input('Digite o NOME do produto: ')).strip()
    preço = float(input('Digite o PREÇO do produto: R$ '))
    gasto += preço
    if preço > 1000:
        mil += 1
    if count == 0 or preço < maisBarato:
        maisBarato = preço
        nomeBarato = nome
    desejaContinuar = str(input('Digite s p/ continuar e n p/ parar\: ')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('Digite s p/ continuar e n p/ parar\: ')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^50}'.format(' PROGRAMA ENCERRADO COM SUCESSO! '))
        break
    count += 1
print(f'''------------------- ANÁLISE ------------------
TOTAL GASTO: R$ {gasto:.2f}
{mil} produtos custam MAIS de R$1000
O produto mais barato é o {nomeBarato} que custa R${maisBarato:.2f}
''')
