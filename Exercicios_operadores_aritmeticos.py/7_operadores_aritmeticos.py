#desafio_11: Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada 
# litro de tinta pinta uma área de 2m².
lar = int(input('Qual a largura da sua parede?: '))
alt = int(input('Qual a altura da sua parede?: '))
area = lar*alt
tin = area/2
print('Sua parede tem {}m² de area total. Você precisará de {} litros de tinta!'.format(area, tin))