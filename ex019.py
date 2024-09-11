#um professor quer sortear um dos seus 4 alunos para apagar o quadro fça um programa lendo o nome deles e escrevendo o nome escolhido
import random
print('Para realizar o sorteio digite os nomes dos alunos: ')
a = str(input('aluno 1: '))
b = str(input('aluno 2: '))
c = str(input('aluno 3: '))
d = str(input('aluno 4: '))
alunos = (a,b,c,d)
print(random.choice(alunos))
