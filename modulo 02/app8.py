# COMO RESOLVER QUALQUER ERRO USANDO O GOOGLE E CHAT-GPT
# Essa é a Habilidade mais importante que precisa dominar 

#Erro genérico 
nome = 'amanda'
print(nome[1]) #usamos para acessar o indice da letra m
#print(nome[6]) #ocasionando um erro propozital para pesquisar o erro que vai dar.
# Copia o erro "string index out of range" cole no google e pesquise em ingles para ver o que é esse erro. obs: colocar python na frente
#para o google saber que é um erro de python.
#podemos tbm usar o chat-gpt para saber qual é o erro que está dando. (atualmente o chat gpt só está com dados até 2021) então é importante 
#pesquisarmos no google primeiro, pra só depois pesquisarmos no chat-gpt.

#Erro específico(inclui dados da sua aplicação)
with open('senhas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

# ERRO:  FileNotFoundError: [Errno 2] No such file or directory: 'senhas.txt'
#para pesquisarmos o erro, devemos tirar o que é especifico da aplicação e pesquise somente a parte generica do erro

