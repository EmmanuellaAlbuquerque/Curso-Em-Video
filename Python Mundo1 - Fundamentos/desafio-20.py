# Sorteio
# 4 alunos
import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
sequencia = [aluno1,aluno2,aluno3,aluno4]
# random.shuffle(sequencia)  # Embaralha a lista
print('A ordem da apresentação é: {}'.format(random.sample(sequencia,4)))
