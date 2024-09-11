#fup que leia o cateto oposto e o adjacente depois calcule o comprimento da hipotenusa
from math import pow,sqrt
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('digite o valor do cateto adjacente: '))
h = pow(a,2) + pow(b,2)
print('o comprimento da hipotenusa é de {}.'.format(sqrt(h)))
