#desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Condesere $1.00=R$3,27
ct = int(input('Quanto você tem em reais? '))
dol = ct/3.27
print('Com o valor em reais de {}, você conseguirá comprar {:.2f} dólares'.format(ct,dol))