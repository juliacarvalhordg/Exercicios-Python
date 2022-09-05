#basico

print('Olá, mundo!') #o print é a fução que será executada, sempre que houver função precisaremos inserir o parentese, dentro dele a mensagem que eu desejo imprimir.

print(7+4) #quando utilizarmos texto, precisamos inserir aspas, já quando falamos de números, não é necessário, pois o texto é a mensagem exibida, mas os números serão base de cálculo

print('7'+'4') #quando colocamos números entre aspas o python somente imprime os números juntos no resultado

#variavel

#toda variável é um objeto no python e pode receber valores, exemplo de variáveis:
nome='Júlia' #o simbolo de igual deve ser lido como recebe, portanto, a variável nome rece Júlia nesse caso
idade=26
peso='Deixa pra lá'
altura='1.56'

print(nome,idade,peso,altura) #print significa escreva e irá retornar todas as variariáveis definidas acima

nome=input('Qual é o seu nome?') #input significa leia
idade=input('Quantos anos você tem?')
peso=input('Quanto você pesa?')
print(nome,idade,peso)
    #desafio_1: Crie um script Python que elia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado.
nome=input('Qual o seu nome?')
print('Olá',nome,'! É um prazer te conhecer!') #quando vamos juntar texto com texto, utilizamos a virgula para imprimir junto, quando tem número, é aconselhado usar o +

    #desafio_2: Crie um script Python que leia o dia, o mês e o ano de uma pessoa e mostre uma mensagem com a data formatada
dia=input('Digite o dia do seu nascimento?')
mes=input('Digite o mês do seu nascimento')
ano=input('Digite o ano do seu nascimento')
print('Você nasceu em '+dia+'/'+mes+'/'+ano+'. Correto?')

    #desafio_3: Crie um script Python que leia dois números e tente mostrar a soma entre eles.
a=int(input('Primeiro número')) #coloca 'int' aqui pq o número que a resposta vai ter é inteiro, nesse caso
b=int(input('Segundo número'))
soma=(a+b) #para que seja somado, você deve definir que soma é o resultado da soma da resposta
print=('A soma dos números é:',soma)

#tipos_primitivos
#int: 7,-4,0,8769
#float: 4.5, 0.0987, -14.768, 7.0
#bool: True, False #sempre em maiúsculo
#str: 'Olá','7.5'

#outra forma de fazer o desafio 3:
#print('Soma vale{}'.format(soma))#o format serve para inserir a soma no texto, sem gambiarra


#resposta (print) simplificado

a = int(input('Digite um número:'))
b = int(input('Digite outro número:'))
s = a+b
#print('A soma de ', a,' e ', b, ' é igual a:', s)
print('A soma entre {0} e {1} vale {2}'.format(n1,n2,s)) #colocando os {} definimos a ordem de sintaxe e ela retorna mais facilmente


#desafio_4: Faça um programa que leia algo pelo teclado e mostre na sua tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = int(input('Ano de nascimento:'))
print(type(a))
