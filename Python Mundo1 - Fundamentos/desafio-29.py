velocidade = int(input('Digite a velocidade do seu carro: '))
if velocidade>80:
    acimaLimite = velocidade - 80
    print('Você foi multado em {} reais '.format(acimaLimite*7))
