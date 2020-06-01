# LISTA COMPOSTA DE ALUNOS E NOTAS

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

'''
aluno = list()
notas = list()
totAlunos = list()
while True:

    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Nota1: ')))
    notas.append(float(input('Nota2: ')))
    aluno.append(notas[:])
    totAlunos.append(aluno[:])
    aluno.clear()
    notas.clear()

    desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    while desejaContinuar not in 'SN':
        desejaContinuar = str(input('S para continuar e N para sair do programa!')).strip().upper()
    if desejaContinuar == 'N':
        print('-='*5, ' BOLETIK LETIVO ', '-='*5)
        break
# BOLETIM
print('N° NOME   MÉDIA')
print('-'*20)
for i, alu in enumerate(totAlunos):
    print(f'{i}  {alu[0]}   {((alu[1][0] + alu[1][1])/2):.1f}')
print('-'*20)

entrada = int(input('Deseja mostrar a NOTA de qual aluno [999 interrompe]'))
while entrada != 999:
    for i, alu in enumerate(totAlunos):
        if entrada == i:
            print(f'Notas de {alu[0]} são {alu[1]}')
            break
    entrada = int(input('Deseja mostrar a NOTA de qual aluno [999 interrompe]'))
'''