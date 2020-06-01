# Verifica se é Palíndromo, desconsiderando espaços entre as palavras

''' FORMA 1
palavra = str(input('Digite a palavra a ser analisada: '))
palavra = palavra.replace(" ", "")
novaPalavra = palavra[::-1]

if palavra == novaPalavra:
    print('É UM PALINDROMO!')
else:
    print('NÃO É UM PALÍNDROMO!')
print('A palavra invertida é: {}'.format(novaPalavra))
'''

''' FORMA 2 '''
frase = str(input('Digite uma frase: ')).strip().upper()
# Separa as frases por espaço
palavras = frase.split()
# Junta todas as palavras separadas sem espaço
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO')

