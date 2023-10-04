# Algoritimo que leia o preço e de um desconto de 5%

pv = float(input('preço de venda:'))
desc = 5
novo_preco: float = pv - (pv * desc / 100)

print(novo_preco)
