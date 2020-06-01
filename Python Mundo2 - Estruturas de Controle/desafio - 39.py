from datetime import date

nascimento = int(input('Digite em que ano você nasceu: '))
data_atual = date.today()
idade = data_atual.year - nascimento

print('Como a idade do jovem é {} anos, temos que: '.format(idade))
if idade > 1 and idade < 18:
    print('Você ainda vai se alistar no serviço militar!')
    tempo = 18 - idade
    print('Falta {} anos para você se alistar!'.format(tempo))
elif idade == 18:
    print('Está na hota de você se alistar no serviço militar!')
elif idade > 18:
    print('Já passou do tempo de você se alistar no serviço militar!')
    tempo = idade - 18
    print('Você deveria ter se alistado a  {} anos atrás!'.format(tempo))
else:
    print('Idade inválida!')
