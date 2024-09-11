#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nom = str(input('digite seu nome: ')).split()
print('{} {}'.format(nom[0], nom[-1]))
