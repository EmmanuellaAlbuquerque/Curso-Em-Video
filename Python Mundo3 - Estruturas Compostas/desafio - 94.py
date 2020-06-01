# UNINDO DICIONÁRIOS E LISTAS
pessoa = dict()
galera = list()
soma = média = 0
# ENTRADA DOS DADOS
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)

# ANÁLISE DOS RESULTADOS
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma/len(galera)
# 5.2f = 5 casas ao todo e 2 decimais
print(f'B) A média de idade é de {média:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


'''
pessoa = dict()
listaDePessoas = list()
countP = 0

while True:
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] '))
    while sexo not in 'MFmf':
        sexo = str(input('ERRO. Tente novamente. Sexo: [M/F] '))
    idade = int(input('idade: '))
    pessoa['Nome'] = nome
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = idade
    listaDePessoas.append(pessoa.copy())
    countP += 1

    desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    if desejaContinuar == 'N':
        print('{:-^51}'.format(' PESSOAS ADICIONADAS COM SUCESSO '))
        break

print(listaDePessoas)
print('-='*30)
print(f'- Foram cadastradas {countP} pessoas.')

# Média Idade do Grupo
soma = 0
for item in listaDePessoas:
    soma += item['Idade']
médiaIdade = soma/countP
print(f'- A média das idades é {médiaIdade} anos.')

# Lista com todas as Mulheres
listaMulheres = list()
for item in listaDePessoas:
    if item['Sexo'] == 'F' or item['Sexo'] == 'f':
        listaMulheres.append(item.copy())
print(f'- As mulheres cadastradas foram: ', end='')
for item in listaMulheres:
    print(f'{item["Nome"]}', end=' ')

# Lista com todas as pessoas com idade acima da média
listaIdade = list()
for item in listaDePessoas:
    if item['Idade'] > médiaIdade:
        listaIdade.append(item.copy())
print(f'\n- Lista de pessoas que estão acima da média: ')
for item in listaIdade:
    print(f'Nome: {item["Nome"]}, Sexo: {item["Sexo"]}, Idade: {item["Idade"]}')
'''