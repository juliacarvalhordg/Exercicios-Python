#operadores_aritmeticos
# + adição                  # ** potencia
#   5+2==7                           5**2==25 (aqui o numero esta ao quadrado)
# - subtração               # // divisao inteira
#   5-2==3                           5//2==2 (divisao sem usar virgula)
# * multiplicação           # % resto da divisao
#   5*2==10                          5%2==1 (resto da divisao inteira)
# / divisão
#   5/2=2.5

#ordem de procedencia (qual será executado primeiro?)
#1 () parenteses
#2 ** potencia
#3 *, /, //, % (se aparecer mais de uma, fazer pela ordem que aparecer)
#4 +, -

#praticando: 
#nome = input('Qual seu nome? ') #colocar o string aqui é opcional, quando nao colocado entende-se que é str
#print('Prazer em te conhecer {}!'.format(nome)) #é possivel alinhar o resultado do {} usando >,<, e etc

#praticando_2

n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d_i = n1//n2
e = n1 ** n2
print ('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='') #o :3.f na chave faz com que o número quebrado apareça com somente tres casas: 0.123 e não completo: 0.12347569078575658~
print ('Divisão inteira {} e potência {}'.format(di, e)) # na linha acima, foi inserido end='' no final do código, isso faz com que o proximo print consitunue na mesma linha que ele.
# utilizando \n quebra a linha dentro do print,  não sendo necessário um print para cada
