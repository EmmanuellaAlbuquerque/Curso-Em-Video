
'''
print('================= SEÇÃO TIPOS PRIMITIVOS ================')
dataStr = str(input('Digite o str:'))  # tipo string
dataInt = int(input('Digite o inteiro:'))  # tipo inteiro
dataFloat = float(input('Digite o float:'))  # tipo de ponto flutuante
dataBool = bool(input('Digite o boleano:'))  # tipo boleano

print('Dado o teste temos: {}'.format(dataStr))
print('Dado o teste temos: {}'.format(dataInt))
print('Dado o teste temos: {}'.format(dataFloat))
print('Dado o teste temos: {}'.format(dataBool))
print('O formato é: {}'.format(type(dataInt)))
'''

'''
print('================= SEÇÃO SOMA ================')
num1 = int(input('Digite o primeiro número:'))  # tipo inteiro
num2 = int(input('Digite o segundo número:'))  # tipo inteiro
soma = num1 + num2
print('A soma entre {} e {} vale {}.'.format(num1, num2, soma))
'''

'''
print('================= SEÇÃO TIP ================')
escolha = input('Digite algo: ')
print('É alfanúmerico? ', escolha.isalnum())
print('É decimal? ', escolha.isdecimal())
print('Todas as letras são maiúsculas? ', escolha.isupper())
print('É uma letra? ', escolha.isalpha())
print('É um digito? ', escolha.isdigit())
print('Todas as letras são minúsculas? ', escolha.islower())
print('É identifier? ', escolha.isidentifier())
print('É printable? ', escolha.isprintable())
print('É capitalizada ? Ex.: Pão ', escolha.istitle())
'''

'''
print('================= Operadores Aritméticos ================')
print('='*20,'Operadores Aritméticos','='*20)
# ** : potência, // : divisão inteira
# ordem de precedência:
# parênteses,
# potência, (pow(4,3))
# divisão, multiplicação, resto, divisão inteira
# subtração, multiplicação
# raiz quadrada de 81: 81**(1/2)
nome = input('Qual \n seu nome?')
print('Prazer {:=^20}!'.format(nome))
print('Prazer {:>20}!'.format(nome))
print('Prazer {:<20}!'.format(nome))
print('Prazer {:^20}!'.format(nome))
numb = float(input('Digite um numéro:'))
print('numero {:.2f}!'.format(numb), end='>>>')
'''

'''
print('================= Trabalhando com módulos ================')
# https://docs.python.org/3/
# https://pypi.org/search/
import emoji
print(emoji.emojize('Olá Mundo! :earth_americas:', use_aliases=True))
'''

'''
print('================= Manipulando Texto ================')

# Fatiamento
frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:13])  # Inclue 9, remove 13
print(frase[9:21:2])  # Pulando de 2 em 2
print(frase[:5])  # De 0 a 5
print(frase[15:])  # De 15 até o final
print(frase[9::3], '\n')  # De 9 até o final, mas de 3 em 3

# Análise
print(len(frase))  # Comprimento da frase
print(frase.count('o'))  # Quantidade de 'o's
print(frase.count('o', 0, 13))
print(frase.find('deo'))  # Indica onde a frase começa
print(frase.find('android')) # Retorna -1, string não existe na frase
print('Curso' in frase, '\n')  # Se curso existe em frase

# Transformação
print('Replace:', frase.replace('Python', 'Android'))  # Não altera frase
print('Upper:', frase.upper())  # Deixa tudo em letras maiúsculas
print('Lower:', frase.lower())  # Deixa tudo em letras minúsculas
print('Capitalize:', frase.capitalize()) # Deixa somente a primeira letra de uma palavra em maiúsculo
print('Title:', frase.title())  # Deixa todas as 1° letras da frase em maiúsculas

frase = '   Aprenda Python  '
print('Strip:', frase.strip())  # Tira os espaços antecedentes e sucedentes desnecessários
print('RightStrip:', frase.rstrip())  # Remove somente os espaços do lado direito
print('LeftStrip:', frase.lstrip(), '\n')  # Remove somente os espaços do lado esquerdo

# Divisão
frase = 'Curso em Video Python'
print('Split:', frase.split(), '\n')  # Divide a frase onde tem espaços

# Junção
lista = frase.split()
print(lista)
print('-'.join(lista))  # Junta todos os elementos de frase, com o separador '-'
print('Primeira palavra da lista:', lista[0])  # Apresenta a primeira palavra da lista
print('Mostra terceira letra da segunda palavra:', lista[2][3])  # Apresenta a primeira palavra da lista

print("""Para textos grandes. Para textos grandes.
Para textos grandes. Para textos grandes.
Para textos grandes. Para textos grandes.""")
'''

'''
print('================= Condições (Parte 1) ================')
nome = str(input('Digite seu nome: '))
if nome == 'Manu':
    print('Que nome bonito! ')
else:
    print('Seu nome é tão normal! ')
print('Bom dia! ')  # Só pelo fato de não estar identado faz com que seja exibido

print('Manu te amo' if nome == 'Manu' else 'Manu te odeio')
'''

print('================= Cores no Terminal ================')
# Módulo colorize procurar
# \033[0:33:44m style, text, back
# cores == Dicionário:
cores = {'limpa': '\033[m',
         'azul': '\033]34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('{}Olá Mundo{}!'.format(cores['amarelo'], cores['limpa']))

print('\033[31mOlá Mundo!')
print('\033[0;30;41mOlá Mundo!\033[m') # Se quiser pode colocar o próprio .format --> sendo {para cor começo}{texto}{para cor fim}
print('\033[4;33;44mOlá Mundo!')
print('\033[1;35;43mOlá Mundo!')
print('\033[30;42mOlá Mundo!')
print('\033[0;33;44mOlá Mundo!')
print('\033[mOlá Mundo!')
print('\033[7;30mOlá Mundo!')






