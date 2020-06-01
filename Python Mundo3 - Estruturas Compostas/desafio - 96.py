def área(largura, altura):  # terreno retangular
    area = largura*altura
    print(f'A área de um terreno de {largura}x{altura} é de {area}m².')


# Programa Principal
print('\nControle de Terrenos', '\n', '-'*10)
largure = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largure, comprimento)
