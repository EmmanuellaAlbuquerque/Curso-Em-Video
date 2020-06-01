# Produtos disponíveis
'''
cores = {'limpa': '\033[1m',
         'azul': '\033]34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'branco': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m',
         'lilas': '\033[1;35m',
         'babe': '\033[1;36m',
         'cinza': '\033[1;37m',
         }

print('{}-=-{}'.format(cores['azul'],cores['limpa'])*20)
print('{}    Qual produto você deseja saber a disponibilidade? {}'.format(cores['branco'], cores['limpa']))
print('{}-=-{}'.format(cores['azul'], cores['limpa'])*20)

produto = str(input('\n{}    Digite o nome do produto: {}'.format(cores['branco'],cores['limpa'])))

res = 5*3**2
print(res)

num = 4.9999
print(int(num))
'''
'''
n1 = '7'
n2 = 4
print(n1+str(n2))

nome = 'João dos Anjos Moura'
print(nome[1:10:2].upper())

a = 4
b = 3
c = 2
d = a + b * c
e = d % c + 1
print('{} e {}'.format(d, e))

texto = 'Tres Pratos de Trigo para Tigres Tristes '
total = texto.upper().count(texto[0])
print(total)

frase = 'Curso em Video de Python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())

'''

from random import  randint
num = randint(1, 6)
res = num // 2
print(res)
