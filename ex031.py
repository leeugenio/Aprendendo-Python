#fup que leia a distancia e calcule o preço da viagem $0,5/km pra viagens até 200km e
# $0,45 para viagens mais longas
v = float(input('digite a distancia da sua viagem: '))
if v<=200:
    print('sua viagem custará ${:2}'.format(v*0.50))
else:
    print('sua viagem custará ${:2}'.format(v*0.45))
