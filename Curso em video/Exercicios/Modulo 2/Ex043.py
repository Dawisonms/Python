'''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))
IMC = peso / pow(altura,2)

if IMC < 18.5:
    print('Seu IMC é {:.2f} e você está ABAIXO DO PESO'.format(IMC))
elif 18.5 <= IMC < 25:
    print('Seu IMC é {:.2f} e seu peso esta IDEAL'.format(IMC))
elif 25 <= IMC < 30:
    print('Seu IMC é {:.2f} e você está com {}SOBREPESO!{}'.format(IMC,'\033[33m', '\033[m'))
elif 30 <= IMC < 40:
    print('Seu IMC é {:.2f} e você está com {}OBESIDADE!!{}'.format(IMC, '\033[4;31m', '\033[m'))
else:
    print('Seu IMC é {:.2f} e você está com {}OBESIDADE MORBIDA!!!{}'.format(IMC, '\033[7;31;40m', '\033[m'))