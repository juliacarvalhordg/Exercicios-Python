#desafio_13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, 
# com aumento de 15%
sal = float(input('Qual o seu salário atual? '))
aum = sal + (sal*0.15)

print('O seu salário com 15% de aumento é: {}.'.format(aum))