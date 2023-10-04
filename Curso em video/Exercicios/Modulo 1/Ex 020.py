#Sortear ordem de 4 apresentaçõe

import random

a1 = str(input('aluno 1 '))
a2 = str(input('aluno 2 '))
a3 = str(input('aluno 3 '))
a4 = str(input('aluno 4 '))
alunos = [a1, a2, a3, a4]

#print(random.choices(['Pedro', 'Alfredo', 'Maria', 'Juliana'],k=4))

random.shuffle(alunos)

print('A ordem de apresentação é {}'.format(alunos))