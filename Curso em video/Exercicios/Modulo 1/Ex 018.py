# Ler um angulo qualquer e calcule o seno,cosseno e tangente
import math
angulo = float(input('Valor do angulo:  '))
Sen = math.sin(math.radians(angulo))
Con = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))


print('Para um angulo de {} temos: \n Seno {:.2f} \n Cosseno {:.2f} \n Tangente {:.2f}'.format(angulo, Sen, Con,tang))