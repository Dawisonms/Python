#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
import emoji
cores = {'limpar': '\0033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'magenta': '\033[35m'}

casa = float(input(emoji.emojize('Qual valor da casa :house:: ')))
salario = float(input(emoji.emojize('Qual seu salário :euro_banknote:: ')))
anos = float(input(emoji.emojize('Quantos anos vai financiar?:calendar:: ')))


prestacao: float = casa / (anos * 12)
if prestacao > salario * 30/ 100:
    print(emoji.emojize('{} Infelizmente não será possível o financiamento :frowning_face:'.format(cores['vermelho'])))
else:
    print(emoji.emojize("{}Pode nos enviar as documentações necessárias, \nA prestação da sua casa será de {} {:.2f} {}mensais :smiling_face_with_sunglasses:".format(cores['azul'], cores
    ['amarelo'], prestacao, cores['azul'])))

