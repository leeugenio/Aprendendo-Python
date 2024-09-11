#fup que leia o seguimento de 3 retas e diga se elas podem formar um triândulo
a = float(input('Digite o valor do lado a: '))
b = float(input('Digite o valor do lado b: '))
c = float(input('Digite o valor do lado c: '))

if a + b > c and b + c > a and a + c > b:
    print('As retas podem formar um triâgulo.')
else:
    print('As retas não podem formar um triângulo.')
