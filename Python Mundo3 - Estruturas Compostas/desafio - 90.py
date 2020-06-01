nome = str(input('Nome: '))
média = float(input('Média: '))
situação = ' '
aluno = dict()
if média >= 7:
    situação = 'Aprovado(a)'
elif 5 <= média < 7:
    situação = 'Recuperação'
else:
    situação = 'Reprovado'
aluno['Nome'] = nome
aluno['Média'] = média
aluno['Situação'] = situação
print('-=' * 20)
for key, value in aluno.items():
    print(f'{key}: {value}')
