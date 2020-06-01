# Resumo Estruturas Compostas
# Variáveis Compostas:

# ------------------------------------------- Tuplas: AS TUPLAS SÃO IMUTÁVEIS ---------------------------------------------
# tuplas: nome()
''' Para acessar o primeiro elemento pode ser por
por vetor[0] ou vetor[-4], que representa o ultimo elemento
em um vetor[4] '''

'''
tuplaValor = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(4))
#             -5,        -4,     -3,      -2           -1
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#print(lanche[-4])
#print(lanche[1:3])
#print(lanche[2:])
#print(lanche[:2])
#for comida in lanche: # OU for i in range(0, len(lanche)):
for posição, comida in enumerate(lanche):
    print(f'Comida: {comida} na posição {posição}.')
print('\nOrdem Alfabética:', sorted(lanche))  # em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))  # Quantas vezes aparece o número 5 em C
print(c.index(8))  # Em que posição se encontra o 1° 8
print(c.index(5, 1))  # Em que posição se encontra o 5 começando pelo index 1
pessoa = ('Manu', 20, 'F', 54.05)
print(pessoa)
'''

# ------------------------------------------- Listas: AS LISTAS SÃO MUTÁVEIS ---------------------------------------
# listas: nome[]

# PARTE 1

# Iniciando um lista
'''
- list.append(x): Adiciona um item ao fim da lista.
- 
list.insert(i, x): Insere um item em uma dada posição i.
- 
del(): Deleta um elemento da lista ou a própria lista.

- list.pop(i): Remove o item de posição i da lista e o retorna. Caso i não seja especificado, retorna o último elemento da lista.
- 
list.remove(x): Remove o primeiro elemento, cujo valor seja x.

- list.clear(): Remove todos os elementos da lista.

- list.index(x[, start[, end]]): Retorna o índice do primeiro elemento cujo valor seja x.

- list.count(x): Retorna o número de vezes que o valor x aparece na lista.

- list.sort(key=None, reverse=False): Ordena os items da lista (os argumentos podem ser usados para customizar a ordenação).
- 
list.reverse(): Reverte os elementos da lista.
- list.copy(): Retorna uma lista com a cópia dos elementos da lista de origem.
'''

'''
num = [2, 5, 9, 1]
# OU valores = list()

num.append(7)
num.sort()  # ordena a lista
num.insert(2, 3)  # insere 3 na posição 2
print(num)
num.pop()  # remove o ultimo número
print(num)
num.pop(0)  # remove o número na posição 0
print(num)
num.insert(4, 2)  # insere 2 na posição 4
print(num)
num.remove(2)  # remove o primeiro 2 que aparecer
print(num)
if 4 in num:  # primeiro testa se o número está na lista, senão da erro
    num.remove(4)
else:
    print('Não achei o número 4.')
'''

'''
.append()  # add no final da lista
.insert(0, )  # add no inicio da lista
del lanche[3]  # remove pelo índice
lanche.pop(3)  # remove pelo índice

if nome in lanche: # só remove se tiver na lista
    lanche.remove(nome)  # remove pelo conteúdo

valores = list(range(4, 11))
print(valores)
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()  # Ordena os valores da lista: crescentes
print(valores)
valores.sort(reverse=True)  # Ordenados na ordem reversa
print(valores)
print(len(valores))
'''
'''
valores = list()
for count in range(0, 3):
    valores.append(int(input('Digite o valor: ')))

for i, valor in enumerate(valores):
    print(f'Na posição {i} encontrei o valor {valor}!')
print('Cheguei ao final da lista')
'''
'''
# Peculiaridade do PYTHON
a = [2, 3, 4, 7]
# NÃO É UMA CÓPIA
b = a  # ligação de uma lista com outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}\n')

# AGORA SIM É UMA CÓPIA
a = [2, 3, 4, 7]
b = a[:]  # copia a lista a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''

# PARTE 2: UMA LISTA DENTRO DE OUTRA
'''
time = [['João', 19], ['Maria', 20], ['Ana', 15]]
print(time[0])
print(time[0][0])
for pessoa in time:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

teste = list()
teste.append('Manu')
teste.append('20')
galera = list()

# Se fosse append(teste) criaria uma ligação e não uma cópia
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
# ANÁLISE DE PESSOAS MAIOR E MENOR DE IDADE, EM UMA LISTA DENTRO DE OUTRA LISTA
galera = list()
dado = list()
totmaior = totmenor = 0  # não pode fazer isso em estruturas compostas
for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # cópia
    # apaga o dado para add um novo
    dado.clear()  # se fosse append(dado), apagava os dados de galera tb pq estariam ligados

for p in galera:
    if p[1] >= 21:  # Se pessoa tiver mair de 21 anos EUA maior de idade
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
'''

# -------------------------------------------------- Dicionários -----------------------------------------------------
# dicionários: nome{}

'''
# Índices literais
nome = {}
# Value: titanic e romance, Keys: titulo e tipo
filme = dict({'titulo': 'Titanic', 'tipo': 'romance'})
# EXEMPLO LOCADORA, VÁRIOS DICINÁRIOS DENTRO DE UMA LISTA
# PRINT(LOCADORA[0]['ANO'])
print(nome.values())
print(nome.keys())
# PARA TUPLAS E LISTAS TEMOS O ENUMERATE PARA DICIONÁRIOS TEMOS:
print(nome.items())
del filme['tipo']
for chave, valor in filme.items():
    print(f'O {chave} é {valor}')
'''

'''
# DICIONÁRIO DENTRO DE UMA LISTA
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:  # FOR DA LISTA
    for key, value in e.items(): # FOR DO DICIONÁRIO
        print(f'O campo {key} tem valor {value}')

# NO CASO DO DICIONÁRIO NÃO FUNCIONA O append(nome[:]) PARA CÓPIA
# DEVE-SE USAR nome.copy()]
'''

# ------------------------------------------------- Funções ----------------------------------------------------------
'''
Funções->Rotinas
Sistematizar algo trabalhoso ou Repetitivo
Todas as funções são identificadas com parêntesis depois do nome

'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(b=4, a=5)
soma(4, 5)
'''

'''
def contador(*núm):  # *(recebe vários valores) - desempacota dados
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


# EMPACOTAR PARÂMETROS
contador(5, 7, 3, 1, 4)  # cria um tupla
'''

# Para não usar tupla, podemos passar por parâmetro a lista com todos os valores

'''
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

'''
- Interactive Help
- Docsstrings
- Argumentos Opcionais
- Escopo de Variáveis
- Retorno de resultados
'''

# - Interactive Help(Ajuda Interativa)
'''
help()  # in Python Console
help(print())
print(input.__doc__)
'''

# - Docsstrings(Documentação)

'''
def contador(i, f, p):
    '''
# -> Faz uma contatem e mostra na tela.
# :param i: início da contagem
# :param f: fim da contagem
# :param p: passo da contagem
# :return: sem retorno
'''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(1, 10, 1)
help(contador)
'''

# - (Parâmetros)Argumentos Opcionais

'''
def somar(a=0, b=0, c=0):  # se C não for especificado ele vale ZERO
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()
'''

# - Escopo de Variáveis
'''
def teste():
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Ma função de teste, x vale {x}.')


# Programa Principal
n = 2  # Escopo Global
print(f'No programa principal, n vale {n}')
teste()
# print(f'No programa principal, x vale {x}') # Escopo Local. Não funciona, pois X tem o escopo local
'''

'''
def teste(b):
    a = 20  # A: Local, !=
    print(a)


# Programa Principal
a = 5  # A: Global !=
teste(a)
print(f'A fora vale {a}')
'''

'''
def teste():
    lista.append(10)  # se mudar aqui, muda em ambos local e global
    print(f'ESCOPO LOCAL: {lista}')


# Programa Principal
lista = list([[1, 2, 3]])
teste()
print(f'ESCOPO GERAL: {lista}')
'''

'''
def teste(b):
    global a  # palavra reservada
    a = 20  # troca o valor do a GLOBAL
    print(f'A dentro vale {a}')


# Programa Principal
a = 5
teste(a)
print(f'A fora vale {a}')
'''

# - Retorno de resultados

'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


# resp = somar(3, 2, 5)
print(f' s1 = {somar(10, 5)}, s2 = {somar(3, 2, 5)} ')
'''


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

'''
print(f'O fatorial de {5}! = {fatorial(5)}')
'''

'''
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


print(par(8))
if par(10):
    print('---')
'''


# ---------------------------------- Modularização e Pacotes ----------------------------------------------------------
# encontra-se em arquivo sepadado pyCharm; modulosPython



# ---------------------------------- Tratamento de Erro  e Exceções ----------------------------------------------------------

'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado!')
'''


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito Obrigado!')

























