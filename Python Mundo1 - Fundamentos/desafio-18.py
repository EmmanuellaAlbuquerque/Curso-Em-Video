# Ângulos
# 1rad × 180
# num  × π
# num = pi/180

import math
angulo = float(input('Escreva um ângulo em graus: '))
# seno = math.sin(math.radians(angulo))
num = angulo*(math.pi)/180
print('o seno de {} é {:.2f} \n' 'o cosseno de {} é {:.2f} \n' 'a tangente de {} é {:.2f}'.format(angulo, math.sin(num), angulo, math.cos(num), angulo, math.tan(num)))
