distancia = int(input('Digite a distância de uma viagem em km: '))
# passagem =  distancia * 0.50 if distancia <= 200 else distancia * 0.45
if distancia > 200:
    passagem = distancia * 0.45
    print('O preço da passagem é {:.2f} real(is).'.format(passagem))
else:
    passagem = distancia * 0.50
    print('O preço da passagem é {:.2f} real(is).'.format(passagem))