#fup que faça o computador 'pensar' em um número e o usúario tente adivinhar
from random import choice
d = choice([0, 1, 2, 3, 4, 5])
c = int(input('tente adivinhar qual número de 0 a 5 estou pensando: '))
if d == c:
    print('ISSO MESMO O NÚMERO QUE EU PENSEI É O {}!'.format(d))
else:
    print('Está errado eu pensei no número {}'.format(d))
