# AULA 1 VARIAVEIS
'''velocidade_internet = 10
print(velocidade_internet)
# Quais os tipos de dados podemos armazenar na memória do computador?
# Numeros
velocidade_internet = 10
# Valores Boleanos
esta_aberta = True
# Strings
slogan = 'Feito é melhor que pereito!'
# atribuindo valores
variavel_1 = 25.85
a, b, c, d = 1, 2, 3, 4
print(a)
print(b)
print(c)
print(d)
# para saber o tipo da variavel
print(type(a))
print(type(velocidade_internet))
print(type(slogan))
print(type(esta_aberta))
print(type(variavel_1))
'''
# AULA 2     ENSINA RODAR O ARQUIVO NO TERMINAL SHELL
#################################################################################################
# AULA - 2.2         Como resolver QUALQUER erro com GOOGLE ou CHATGPT

# Erro genérico (1- Leia o erro, 2- copie a mensagem e cole no google trautor)
'''nome = 'amanda'''
# [012345]
# print(nome[6])

# Erro especifico (inclui dados da sua aplicação)
"""with open('senhas.txt','r') as arquivo:
    for linha in arquivo:
        print(linha)"""
# IndentationError: expected an indented block after 'for' statement on line 36
# FileNotFoundError: [Errno 2] No such file or directory: 'senhas.txt'  (para pesquisar no google, retiramos o que é especifico da nossa aplicação) no nosso caso retirariamos o "senhas.txt"

###################################################################################################
# AULA 3 - Indentação
'''if 10 > 5:
    print('10 é maior que 5')


class Bemvindo():
    print('BemVindo')
'''

################################################################################################
# AULA 4 - Strings
'''print('codar todos os dias')
print("este exemplo é com aspas duplas")
print(Desta forma podemos escrever mais de uma linha
quebrando o texto.
)
# Caracteres de escape geralmente, para ter o escape usamos a \
print('Olá meu nome é \nThiago')
print('Codar todos \'os dias')
print('Caminho: c:drive\\pasta\\arquivo')  # add outra \ para escape
nome = 'Carol'
print(len(nome))'''

# atalho para comentar uma linnha ctrl + k + c
# atalho para descomentar uma linnha ctrl + k + u 
# atalho para comentar um bloco shift + alt + a 

###########################################################################################################
# AULA 5 - Strings Dinâmicos
#desafio
'''nome = 'Thiago'
hobby = 'Academia'
print(f'Olá sou o {nome}, meu hobby é {hobby}.')
b = 'ba'
parte2 = 'nica'
a = 'a'
r = 'ri'
parte1 = 'eletrô'
t = 'te'
#imprima 'bateria eletronica'
print(f'{b}{t}{r}{a} {parte1}{parte2}')'''

##########################################################################################
# AULA 6 - Métodos comuns de um string
# Para debugar o codigo (executar linha por linha), usamos o f9 para marcar a linha, depois o f5(primeira op na caixa que abrir)
# depois f10 para executar
'''nome_curso = ' Edição de vídeo '
print(nome_curso.upper())
print(nome_curso.lower())
print(nome_curso.strip()) #remove espaços em branco
print(nome_curso.lstrip()) #remove espaços em branco do lado esquerdo
print(nome_curso.rstrip()) #remove espaços em branco do lado direito
print(nome_curso.find('ção')) #percorre a string e mostra em qual posição está começando(como se fosse um vetor)
print(nome_curso.replace('video', 'muscica'))
print('https://www.olx.com.br/estado-ma?q=moto'.replace('moto', 'carro'))
'''
'''# DESAFIO
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

#Escreva esta frase "É melhor FEITO que PERFEITO"
print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')'''

#######################################################################################
# AULA 7 - Slice(extraindo partes de um string
'''teclado = 'teclado'
print(teclado[2])
#OUTRO EXEMPLO, VAMOS DIZER QUE TU QUEIRA ACESSAR A ULTIMA LETRA = ultilizamos o -1 para acessar de trás para frente.
teclado = 'teclado teclado teclado teclado'
print(teclado[-1])

# ACESSANDO OS INDICES DE FORMA DINAMICA
print(teclado.index('l')) #imprime o 3 , que é a posição que o l está
print(teclado[teclado.index('l')]) #teclado indexado de teclado.'''
# acessando partes de uma string
'''link = 'facebook.com/thiagoluz'
print(link[0])
print(link[-1])
print(link[0:5]) #acessando partes de uma string, 0 onde vai iniciar e 5 onde vai se finalizar.
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])
# podemos tbm buscar caracteres que estao se repetindo dentro de uma frase
frase = 'Clean Code'
print(frase.rindex('C'))
'''
# DESAFIO: Encontre o indice de 'o' dentro da variavel biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))
print(biblioteca[biblioteca.index('o')])
# DESAFIO 2:  usando a frase ; imprima apenas a palávra 'de aplicações'
frase = 'Desenvolvimento de aplicações'
print(frase.index('de'))
print(frase[16:])
