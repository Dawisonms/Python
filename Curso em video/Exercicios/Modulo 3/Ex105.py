'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
 dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

def notas(*n, sit=False):
    turma = dict()
    turma['quant'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n)/len(n)
    if sit:
        if sum(n)/len(n) < 5:
            turma['situação'] = 'RUIM'
        elif sum(n)/len(n) >= 7:
            turma['situação'] = 'BOA'
        else:
            turma['situação'] = 'RAZOÁVEL'
    return turma

resp = notas(5, 7, 4, 8, 8, 10)
print(resp)
