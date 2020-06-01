# CADASTRO DE PESSOA
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

'''
from datetime import date
pessoa = dict()

nome = str(input('Nome: '))
anoNasc = int(input('Ano de Nascimento: '))
# Or datetime.now().year
idade = date.today().year - anoNasc
carteiraTrab = int(input('Carteira de Trabalho: (0 se não têm)'))
pessoa['nome'] = nome
pessoa['idade'] = idade
pessoa['ctps'] = carteiraTrab

if carteiraTrab != 0:
    anoContrato = int(input('Ano de Contratação: '))
    pessoa['contratação'] = anoContrato
    salário = float(input('Salário: '))
    pessoa['salário'] = salário
    # 35 anos de contribuição
    contribuição = date.today().year - anoContrato
    anosPAposentar = 35 - contribuição
    idadeApo = idade + anosPAposentar
    pessoa['aposentadoria'] = idadeApo
print(pessoa)
print('-='*60)
for chave, valor in pessoa.items():
    print(f'{chave} tem o valor {valor}.')
'''