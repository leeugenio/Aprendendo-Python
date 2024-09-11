#fup que leia um angulo e mostre seu seno cosseno e tangente
from math import sin,cos,tan,radians
n = float(input('digite o valor de um angulo para descobrir seu seno, cosseno e tangente:'))
print('seno: {:.2f}\ncosseno: {:.2f}\ntangente: {:.2f}'.format(sin(radians(n)),cos(radians(n)),tan(radians(n))))
