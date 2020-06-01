# COMPILADOR/ANÁLISADOR SINTÁTICO COM LISTA

expr = str(input('Digite a expressão: '))
pilha = []
for símbolo in expr:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

''' aceita parêntesis na do lado errado )6+5(
lista = list()
countParentesis = 0
expressão = str(input('Digite a expressão[com parênteses] a ser analisada: '))
# Quebra a expressão em vários pedaços
for letra in expressão:
    lista.append(letra)
# Analisa a cada pedaço da expressão
for i,elemento in enumerate(lista):
    if elemento in '()':
        countParentesis += 1
if countParentesis % 2 == 0:  # Se a quantidade de parênteses for par
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
'''