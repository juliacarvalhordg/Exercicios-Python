#desafio_12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
pre = float(input('Digite o preço do produto: '))
des = pre*0.05
fin = pre-des
print('O valor do produto com 5% de desconto é: {} '.format(fin))