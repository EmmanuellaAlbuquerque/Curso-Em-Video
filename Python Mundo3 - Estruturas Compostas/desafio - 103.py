def ficha(nome='', ngols=0):
    if ngols.isnumeric():
        ngols = int(ngols)
    else:
        ngols = 0
    # verifica se ao tirar todos os espaços o nome fica vazio
    if nome.strip() == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {ngols} gol(s) no campeonato.'


print('-'*15)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
print(ficha(n, g))


