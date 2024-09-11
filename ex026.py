#fup que leia uma frase e mostre: quantos 'a',posição que aparece primeiro,e em ultimo
f = (str(input('digite uma frase: '))).strip().upper()
print('tem:', f.count('A'))
print('primeira posição:', f.find('A')+1)
print('ultima posição:', f.rfind('A')+1)
