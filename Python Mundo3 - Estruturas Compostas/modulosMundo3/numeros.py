# mais recomendada para se evitar conflito entre a existencia de modulos com mesmo nome
# exercicios 107 a 112

# Módulos
'''
import uteis
# or: from uteis import fatorial, dobro

num = int((input('Digite um valor: ')))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}')
'''

'''
# Pacotes
from uteisPacote import inteiros

num = int((input('Digite um valor: ')))
fat = inteiros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {inteiros.dobro(num)}')
'''

# ----------------------------------------------------------------------------

'''
import moeda

n = 500
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, formatado=True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, formatado=True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(n, 10, True)}')
print(f'Reduzindo em 13%, temos {moeda.diminuir(n, 13, formatado=False)}')

'''

'''
import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)
'''

from utilidadescev import moeda, dado
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 10, 35)





