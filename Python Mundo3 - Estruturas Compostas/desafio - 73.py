# Classificação, Listas de Times

classificação = ('Flamengo', 'Santos', 'Palmeiras', 'São Paulo', 'Corinthias', 'Atlético', 'Internacional', 'Bahia', 'Botafogo', 'Athetico PR',
                 'Goias', 'Grêmio', 'Ceará', 'Vasco da Gama', 'Fortaleza', 'Cruzeiro', 'Chapecoense', 'Fluminense', 'CSA', 'Avaí')
# print(classificação)

count = 1
print('Os 5 PRIMEIROS colocados são:')
for i in range(0, 5):
    print(f'{count}°: {classificação[i]}')
    count += 1

print(f'\nOs ÚLTIMOS 4 colocados são: {classificação[-4:]}')

print(f'\nTimes em ORDEM ALFABÉTICA: {sorted(classificação)}')

# Interpolação precisa de aspas duplas:
print(f'A CHAPECOENSE se encontra na posição: {classificação.index("Chapecoense")+1}')
