# PRODUTOS EM UM TUPLA
produtos = ('Pão', 2, 'Chocolate', 5, 'Arroz', 3, 'Nissin', 3.50,
            'Macarrão', 3, 'Bolacha', 1, 'Chocolate', 5)

# FORMA TABULAR
print('-'*10, 'LISTAGEM DE PREÇOS', '-'*10)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:  # O nome dos produtos sempre está no lado PAR
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>5.2f}')
print('-'*40)
'''
for i in range(0, len(produtos), 2):
    # print(f'{produtos[i]}:.^10', 'R$ {produtos[i+1]}')
    print('{}{:.^20}R${:.2f}'.format(produtos[i], '', produtos[i+1]))
print('-'*42)
'''