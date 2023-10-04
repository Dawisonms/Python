# O professor quer sortear um de seus 4 alunos para apagar o quadro
#programa que ajude ele com nomes...
import  random

a1 = str(input('Aluno 1:'))
a2 = str(input('Aluno 2 '))
a3 = str(input('Aluno 3 '))
a4 = str(input('Aluno 4 '))
sorteio = (random.choice([a1, a2, a3, a4]))

print('Hoje quem irá apagar o quadro é {}'.format(sorteio))

