# Validação de Dados
# strip - Se digitou vários espaços

sexo = str(input('Sexo {M or F}: ')).strip().upper()[0]
# while sexo != 'M' and sexo != 'F':
while sexo not in 'MmFf':
    print('Você digitou um sexo inválido. Tente novamente: ')
    sexo = str(input('Sexo {M or F}: ')).strip().upper()[0]
print(sexo)
