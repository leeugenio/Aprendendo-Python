#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dd = int(input('o carro foi alugado por quantos dias? '))
km = float(input('quantos km rodados? '))
print('o valor de {} dias e {}km rodados é de R${:.2f}'.format(dd, km, (dd*60)+(km*0.15)))