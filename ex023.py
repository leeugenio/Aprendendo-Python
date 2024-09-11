#fup que leia um número de 0 a 9999 e mostre na telacada um dos digitos separados
n = int(input('digite um número de 0 a 9999:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('unidade: {}\ndezena: {}'.format(u,d))
print('centena: {}\nmilhar: {}'.format(c,m))
