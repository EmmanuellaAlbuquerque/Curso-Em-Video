nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2
print('A média foi: {:.1f}'.format(media))

if media < 5:
    print('Reprovado!')
# OU: (7 > media >= 5)
elif media >= 5 and media <= 6.9:
    print('Recuperação')
elif media >= 7 :
    print('Aprovado!')