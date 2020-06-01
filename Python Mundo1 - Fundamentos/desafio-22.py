nomeCompleto = str(input('Qual seu nome: '))
lista = nomeCompleto.split()
print('Maiúsculo: {}'.format(nomeCompleto.upper()))
print('Minusculo: {}'.format(nomeCompleto.lower()))
print('O tamanho do seu nome com espaços é: {}'.format(len(nomeCompleto)))
nomeCompleto = nomeCompleto.replace(' ','')
print('O tamanho do seu nome sem espaços é: {}'.format(len(nomeCompleto)))
print('O primeiro nome ({}) tem {} letras'.format(lista[0], len(lista[0])))
# Ou usando strip, len e count' ' e find

