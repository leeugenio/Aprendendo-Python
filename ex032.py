#fup que leia se o ano é bissexto
from datetime import date
a = int(input('digite o ano: '))
if a == 0:
    a = date.today().year #pega o ano atual
if (a % 4 == 0) and (a % 100 != 0) or (a % 4 == 0) and (a % 100 == 0) and (a % 400 == 0): #calculo do ano bissexto
 print('O ano de {} é bissexto.'.format(a))
else:
    print('O ano de {} não é bissexto.'.format(a))
