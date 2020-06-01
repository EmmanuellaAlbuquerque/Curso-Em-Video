#matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaColuna3 = maiorLinha2 = 0
print('----- MATRIZ 3X3 -----')

# PREENCHIMENTO DA MATRIZ
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Valor [{i},{j}]: '))

# EXIBIÇÃO DA MATRIZ
print('-='*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end=' ')
        if matriz[i][j] % 2 == 0:  # SOMA DOS VALORES PARES
            somaPar += matriz[i][j]
        if j == 2:  # SOMA DOS ELEMENTOS DA COLUNA 3
            somaColuna3 += matriz[i][j]
        if i == 1:  # MAIOR VALOR DA LINHA 2
            if j == 0:  # SE FOR PRIMEIRO ELEMENTO
                maiorLinha2 = matriz[i][j]
            if matriz[i][j] > maiorLinha2:
                maiorLinha2 = matriz[i][j]
    print(' ')
print(f'A soma dos valores PARES é {somaPar}.\n'
      f'A soma dos valores da terceira coluna é {somaColuna3}.\n'
      f'O maior valor da segunda linha é {maiorLinha2}.')
