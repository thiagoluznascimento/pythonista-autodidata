# AULA 8 - Split e Join
'''frase = 'Olá , bem-vindo a esse treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'Jhonatan, Thiago, Joao, Antonio'
print(nomes.split(','))
print(nomes.split())
hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split()) 
print(hashtags.split('#')) 
print(hashtags.split('#',3))

# Como concatenar uma string
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))'''


# Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1

# Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2

# Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.

# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.

'''frase1 = 'Desafio manipulação de strings'
print(frase1.split())
palavras1 = frase1.split()
print(palavras1)

frase2 = 'jhonatan,rafael,carol,camilla'
palavras2 = frase2.split()
print(palavras2)

#3
string_separado_por_virgulas = frase1.split()
print(','.join(string_separado_por_virgulas))
#4
string_separado_por_cifrao = frase2.split(',')
print('$'.join(string_separado_por_cifrao))'''

# AULA 9 - Input - Recebendo dados do usuário
senha = input('Digite sua senha: ')
print(senha)
quantidade_de_filmes = input('Quantidade de filmes: ')
print(type(quantidade_de_filmes))
#Como padrão sempre retorna como 'str'
#Para transformar em outro formato
quantidade_de_filmes = int(input('Quantidade de filmes: '))
print(type(quantidade_de_filmes))

