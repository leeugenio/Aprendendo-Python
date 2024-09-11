#fup que leia a largura e a altura de uma parede e calcule sua área para pinta-lá, sabendo que cada  litro de tinta pinta 2m²
l = int(input('quanto a parede mede de largura? '))
a = int(input('quanto a parede mede de altura? '))
print('a parede mede {} m²'.format(l*a), 'e precisa de {} litros de tinta.'.format((l*a)/2))
