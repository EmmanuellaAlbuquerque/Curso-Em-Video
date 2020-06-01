# IMPLEMENTAÇÃO DO SORT(ORDENAÇÃO)

lista = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista[-1]:  # se primeiro elemento ou se 'n' for maior que o ultimo elemento
        lista.append(n)  # ADD no final
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):  # executa o loop 5 vezes
            if n <= lista[pos]:  # se o número for menor ou igual a posição
                lista.insert(pos, n)  # insere na posição do número comparado
                print(f'Adicionado na posição {pos} da lista...')
                break  # para o loop
            pos += 1  # incrementa a posição
print('-='*30, f'\nOs valores digitados em ordem foram {lista}')

'''
lista = list()  # cria a lista
for i in range(0, 5):  # loop para adicionar dados
    valorUsuario = (int(input(f'Digite o {i+1}° valor: ')))  # pede o valor ao usuário
    if i == 0:  # se for o primeiro valor a ser colocado na lista
        lista.append(valorUsuario)  # add o valor
        print(f'{lista}')  # mostra na tela o resultado da adição
    else:  # se não for o primeiro valor a ser adicionado
        k = 0  # inicia o contador com zero
        # Enquanto não chegar ao fim da lista ou O valor inserido pelo usuário não for menor que o da lista
        while k <= (len(lista) - 1) and valorUsuario > lista[k]:   # continua no loop
            k += 1  # quando parar K, vai estar na posição da parada do maior, logo
        lista.insert(k, valorUsuario)  # quando chegar na posição do maior insere e o maior vai pra frente
        print(f'{lista}')  # mostra na tela o resultado passo a passo
print(f'O conteúdo da LISTA é : {lista}')  # apresenta a lista em sua forma final
'''