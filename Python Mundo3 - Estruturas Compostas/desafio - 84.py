pessoa = list()
grupoPessoas = list()
menor = maior = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append((float(input('Peso: '))))
    grupoPessoas.append(pessoa[:])
    pessoa.clear()  # Se não der clear o próximo elemento add o novo e o anterior

    desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^51}'.format(' FORAM ADICIONADAS TODAS AS PESSOAS '))
        break
print(grupoPessoas)
print(f'No TOTAL foram {len(grupoPessoas)} pessoas.')

for i, p in enumerate(grupoPessoas):
    if i == 0:
        maior = p[1]
        menor = p[1]
    else:
        if p[1] > maior:
            maior = p[i]
        elif p[1] < menor:
            menor = p[1]
print(f'O maior peso foi de {maior:.2f}Kg. Peso de', end=' ')
for i, p in enumerate(grupoPessoas):
    if p[1] == maior:
        print(f'{p[0]},', end=' ')
print(f'\nO menor peso foi de {menor:.2f}Kg. Peso de', end=' ')
for i, p in enumerate(grupoPessoas):
    if p[1] == menor:
        print(f'{p[0]},', end=' ')
