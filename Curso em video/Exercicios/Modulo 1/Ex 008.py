# Programa que leia o valor em metros e exiba convertido em centimetros e milimetros

m = float(input('Metros: '))
cm = m * 100
mm = cm * 10

print('Metro {} \n Centimetro {} \n Milimetro {}'.format(m, cm, mm))
