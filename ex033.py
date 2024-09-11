#fup que calcule aumento de 10% pra salarios maiores que 1250 e de 15% para menores
s = float(input('qual o valor do salário? '))
if s >= 1250:
   print('Com aumento de 10% o valor do seu salário fica em ${}'.format(s+(s*0.1)))
else:
    print('Com o aumento de 15% o valor do seu salário fica em ${}'.format(s+(s*0.15)))