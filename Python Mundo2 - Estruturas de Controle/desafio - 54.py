from datetime import date

anoAtual = date.today().year
maiores = 0
menores = 0

for i in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento - {}°pessoa: '.format(i)))
    idade = anoAtual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas atingiram a MAIORIDADE!'.format(maiores))
print('{} são MENORES de idade!'.format(menores))
