# Hipotenusa
# a²=b²+c² -- H = raiz(b²+c²)
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
# hipotenusa =  math.sqrt(pow(co,2) + pow(ca,2))
hipotenusa = hypot(ca,co)
print('Seja o CA {} e o CO {}, a hipotenusa vale: {:.2f}.'.format(ca,co,hipotenusa))
