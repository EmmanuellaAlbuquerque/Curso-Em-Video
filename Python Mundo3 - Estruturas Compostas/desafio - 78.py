# MENOR E MAIOR ELEMENTO DE UMA LISTA

lista = list()
for i in range(0, 5):
    lista.append(int(input(f'Digite o {i+1}° valor: ')))
print(f'O conteúdo da LISTA é : {lista}')

# Define o MENOR e MAIOR valor e suas posições
maior = max(lista)
menor = min(lista)
print(f'MAIOR valor: {maior} se encontra nas POSIÇÕES', end=' ')
for k, valor in enumerate(lista):
    if valor == maior:
        print(f'{k+1}', end=' ')
print(f'\nMENOR valor: {menor} se encontra nas POSIÇÕES', end=' ')
for k, valor in enumerate(lista):
    if valor == menor:
        print(f'{k+1}', end=' ')
