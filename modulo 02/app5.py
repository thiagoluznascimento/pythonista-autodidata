# 12 - Valores aleatórios com Random
import random

#Gera um valor de 0.0 a 1.0
##print(random.random())
#Gera um valor decimal de valor mínimo ao valor máximo 
##print(random.uniform(1,10))
#Gera um valor inteiro
'''print(random.randint(0,10))

#Gerar um valor aleatório de dentro de uma lista de cores ou nomes
cores = ['verde','azul','amarelo','vermelho']
print(random.choice(cores))
print(random.choices(cores, k=2))
#Embaralhando uma lista
cartas_de_baralho = ['carta1','carta2','carta3','carta4','carta5']
random.shuffle(cartas_de_baralho)
print(cartas_de_baralho)
'''
#DESAFIO 1: Simular a opcao de jogar uma moeda e resultar em cara ou coroa. Jogue as opçoes dentro de uma lista e depois
#crie um programa que imprime 'cara' ou 'coroa' na tela.

moeda = ['cara','coroa']
print(random.choice(moeda))

#DESAFIO 2: Fazer um sorteio entre 5 nomes em uma lista de nomees. Crie uma lista de 5 nomes e sorteie um nome de dentro
#dessa lista e exiba na tala.

nomes = ['Thiago','Joao','Murillo','Maria','Joaquin']
print(random.choice(nomes))

#DESAFIO 3: Escolha aleatoriamente um numero de 10 - 100. ou seja imprima na tela um valor aleatorio de 10 a 100
print(random.randint(10,100))





