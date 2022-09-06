#desafio_8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros a milímetros
n1 = int(input('Insira quantos metros deseja converter: '))
cm = (n1*100)
ml = (n1*1000)
print('O valor em centímetros é: {}. E em milímetos é: {}'.format(cm, ml))
