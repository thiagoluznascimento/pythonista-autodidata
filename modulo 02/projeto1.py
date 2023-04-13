#Login. Modulo1 - gerar registro do funcionário
from datetime import datetime
import random

print('________________________Olá, bem vindo a nossa empresa!____________________________')

nome = input('Olá Digite seu nome: ') 
idade = input('Olá Digite sua idade: ') 

data_atual = datetime.now()
data_cadastro = data_atual.strftime('%d/%m/%Y')

cartoes = ['R$50,00', 'R$250,00','R$120,00']

data_aniversaro = datetime.strptime(input('Informa a sua data de aniversario: '),'%d/%m/%Y')

# Modulo2 Gerar apresentação
# Funcionalidades do módulo 2 - Mensagem de boas vindas!
print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro}.')
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {random.choice(cartoes)}')