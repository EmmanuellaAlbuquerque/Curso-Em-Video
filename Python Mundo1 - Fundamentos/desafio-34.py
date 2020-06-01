salario = float(input('Digite o valor do seu salário: '))

cores = {'limpa': '\033[m',
         'azul': '\033]34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'branco': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'azul': '\033[1;34m',
         'lilas': '\033[1;35m',
         'babe': '\033[1;36m',
         'cinza': '\033[1;37m',
         }

if salario > 1250:
    salario = salario + (salario*(10/100))
    print('salario > 1250')
else:
    salario = salario + (salario * (15 / 100))
    print('salario <= 1250')
print('O aumento foi de {}{}{}.'.format(cores['amarelo'], salario, cores['limpa']))
