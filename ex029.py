#fup que leia qual a velocidade de um carro e se passar de 80km/h a multa é de 7$ por km acima do limite
v = int(input('qual a velocidade do carro? '))
if v>80:
    m = (v-80) * 7
    print('Você ultrapassoua a velocidade máxima da via, o valor da multa é de ${}'.format(m))
else:
    print('Você estava dentro do limite de velocidade da via')
