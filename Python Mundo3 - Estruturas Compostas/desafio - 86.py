# matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('----- MATRIZ 3X3 -----')

# PREENCHIMENTO DA MATRIZ
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Valor [{i},{j}]: '))

# EXIBIÇÃO DA MATRIZ
print('-='*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^3} ]', end=' ')
    print()
