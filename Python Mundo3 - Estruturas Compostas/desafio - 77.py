# Vogais em palavras sem acentuação

palavras = ('Prato', 'Colher', 'Chocolate', 'Bolacha', 'OzOnio')
for i, p in enumerate(palavras):
    palavra = p.upper()
    print('-'*10, f'{i+1}° PALAVRA', '-'*10)
    print(f'Na Palavra {palavra} temos', end=' ')

    for letra in p:
        if letra.upper() in 'AEIOU':  # com acentuação é so add á, â...
            print(letra, end=' ')
    print('\n')
'''
    if palavra.count('A') > 0:
        print('{}a'.format(palavra.count('A')))
    if palavra.count('E') > 0:
        print('{}e'.format(palavra.count('E')))
    if palavra.count('I') > 0:
        print('{}i'.format(palavra.count('I')))
    if palavra.count('O') > 0:
        print('{}o'.format(palavra.count('O')))
    if palavra.count('U') > 0:
        print('{}u'.format(palavra.count('U')))
'''
