# Analisador Completo

somaIdade = 0
maiorIdade = 0
qMulheres = 0
nomeMaiorIdade = ''

for i in range(1, 5):
    print('-='*5, ' DADOS DA {}° PESSOA '.format(i), '-='*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [f/m]: '))
    somaIdade = somaIdade + idade
    if idade > maiorIdade and sexo in 'Mm':
        maiorIdade = idade
        nomeMaiorIdade = nome
    if idade < 20 and sexo in 'Ff':
        qMulheres += 1
print('\nA MÉDIA DE IDADE do grupo é {}'.format(somaIdade/4))
print('O homem MAIS VELHO tem {} e seu nome é {}'.format(maiorIdade, nomeMaiorIdade))
print('{} mulheres têm MENOS DE 20 ANOS'.format(qMulheres))
