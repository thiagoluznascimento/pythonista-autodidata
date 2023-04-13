# 11 - Datetime e Tempo
from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
# Como criar uma data
data_lancamento_app = datetime(2023,6,15)
print(data_lancamento_app)
#Quero receber uma data do usuario e transformando em format de dadatime
#dia , mes e ano = Br
data_lancamento = datetime.strptime(input('Qual é a data do seu aniversario?'),'%d/%m/%Y')
print(data_lancamento)
print(type(data_lancamento))

#Calculando um intervalo entre uma data e outra
data_atual = datetime.now()
prazo = data_lancamento - data_atual
print(f'Faltam apenas {prazo.days} para o seu aniversario.')