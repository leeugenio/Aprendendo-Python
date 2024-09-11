# fup que leia o nome de uma cidade e diga se começa ou não com 'santo'
c = str(input('digite o nome da sua cidade')).strip()
print(c.find('santo',0,5))

print(c[:5].upper() == 'santo')
