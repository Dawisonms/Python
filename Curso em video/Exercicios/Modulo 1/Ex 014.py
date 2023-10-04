# Converta ºC para ºF...C/5 = F-32/9

Grau = input('Converter Celsio X Fareiheid (C) ou Fareheid X Celsius (F): ')
if Grau == 'C':
    C = float(input('Dig o ºC'));
else:
    F = float(input('Dif o Grau F: '))

if Grau == 'C':
    print('Grau em Fareihaid e {:.2f}'.format(C * 1.8 + 32));
else:
    print('Grau em  Celsius é {:.2f}'.format((F - 32) / 1.8))
