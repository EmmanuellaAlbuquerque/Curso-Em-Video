# Cálculo do IMC - Indice de Massa Corpórea

peso = float(input('Digite seu peso:(Kg) '))
altura = float(input('Digite sua altura:(m) '))

imc = peso/(pow(altura, 2))
print('Seu IMC é {:.1f}'. format(imc))

if imc < 18.5:
    print('Você se encontra abaixo do peso!')
# Ou 18.5 <= imc < 25
elif imc >=18.5 and imc < 25:
    print('Você se encontra no peso ideal!')
elif imc >=25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obsidade mórbita!')