import urllib.request
try:
    urllib.request.urlopen("http://pudim.com.br/")
except:
    print('\033[0;33mO site pudim não está acessível no momento!', end='\033[m')
else:
    print('\033[0;34mConsegui acessar o site pudim com sucesso!', end='\033[m')
