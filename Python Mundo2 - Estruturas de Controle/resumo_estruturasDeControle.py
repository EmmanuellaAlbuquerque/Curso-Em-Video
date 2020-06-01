# Condições simples:
'''
nome = str(input('Qual seu nome? '))
if nome == 'Manu':
    print('Que nome bonito!')
print('Tenha um bom dia, {}'.format(nome))

# Condições compostas:
nome = str(input('Qual seu nome? '))
if nome == 'Manu':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))

# Condições alinhadas:
nome = str(input('Qual seu nome? '))
if nome == 'Manu':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Joao Jose Juliana':
    print('Belo nome')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))
'''

# Estruturas de repetição: Com variável de controle
''' LAÇO FOR: Quando se sabe o limite. ''' '''

for i in range(1, 6):
    print(i)
print('\n')
# iterando com -1
for i in range(5, 0, -1):
    print(i)
print('\n')
# pulando de 2 em 2
n = int(input('Digite quantas vezes deseja iterar: '))
for i in range(0, n+1, 2):
    print(i)
'''

# Estruturas de repetição: Com teste lógico no início
''' LAÇO WHILE: Quando não se sabe o limite. '''

''' 
i = 1
while i < 10: # flag
    print(i)
    i += 1
print('FIM')

# Flag: condição de parada
r = 'S'
while r == 'S':
    valor = int(input('Digite um valor: '))
    r = str(input('Quer consinuar? [s/n] ')).upper()
print('FIM')
'''

# Estruturas de repetição: Repetições infinitas com interrupção no meio
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
# f string, interpolação:
print(f'A soma vale {s:.2f}')
