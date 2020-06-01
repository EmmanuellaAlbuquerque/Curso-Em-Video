from datetime import date
nascimeto = int(input('Digite sua data de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimeto
print('O atleta tem {} anos.'.format(idade))

# Categoria de natação
if idade <=9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14: # Ou somente idade <=14
    print('Categoria Infantil')
elif idade > 14 and idade <= 19:
    print('Categoria Junior')
elif idade > 19 and idade <= 25:
    print('Categoria Sênior')
elif idade > 25:
    print('Categoria Master')