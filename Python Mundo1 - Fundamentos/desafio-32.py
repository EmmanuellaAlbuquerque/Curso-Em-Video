# Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
# Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
# Pode ser que seja divisível por 400.
from datetime import date

ano = int(input('Digite um ano qualquer: Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto! '.format(ano))
else:
    print('O ano de {} não é bissexto! '.format(ano))



'''  
if (ano % 4) == 0:
    if ano % 100 != 0:
        print('O ano é bissexto! ')
    else:
        print('O ano não é bissexto! ')
else:
    if (ano % 400) == 0:
        print('O ano é bissexto! ')
    else:
        print('O ano não é bissexto! ')
'''
