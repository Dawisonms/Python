'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
 como parâmetro e mostre uma mensagem com tamanho adaptável.
 Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~'''

def msg(txt):
    print('~'*(len(txt)+2))
    print(f' {txt}')
    print('~'*(len(txt)+2))


msg('To ficando bom nessa coisa')
msg('Não é que deu certo!')
msg('Mano!')


