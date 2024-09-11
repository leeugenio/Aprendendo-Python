#fup que leia 4 nomes e mostre uma lista aleatória
import random
from random import sample
print('digite quatro nomes para sortear uma lista aleatória:')
a = str(input('1: '))
b = str(input('2: '))
c = str(input('3: '))
d = str(input('4: '))
lista = [a, b, c, d]
random.shuffle(lista)
print(lista)
