#fup que leia o nome de alguém e mostre: com maiusculas, minusculas quantas letras sem considerar espaços
nom =str(input('digite seu nome: '))
print('MAIÚSCULAS: {}'.format(nom.upper()))
print('minuscúlas: {}'.format(nom.lower()))
nom = nom.split()
print('tem {} letras'.format(len(''.join(nom))))
print('seu 1° nome é {} e tem {} letras.'.format(nom[0],len(nom[0])))
