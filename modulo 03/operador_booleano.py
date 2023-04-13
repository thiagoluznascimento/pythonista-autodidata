# Comparações c/ Operadores Booleanos
# Vamos pensar no seguinte exemplo

""" # A pessoa somente pode entrar no evento caso ela tenha mais de 21 anos e que possua um convite
idade = 21
possui_convite = True
filho_do_dono = True
print((idade > 21) and (possui_convite == True))  # condição 'E' . Se a idade for maior que 21 'E' possuir convite
print((idade >= 21) or (possui_convite == True))  # condição ' ou '. Se idade for maior ou igual a 21  'OU' possuir convite

# Maior de 21 e possui convite ou seja filho do dono
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))
 """
 #OUTRO EXEMPLO
 # Voce só pode trabalhar aqui se tiver carteira de trabalho e for maior de idade 
maior_de_idade = True
possui_carteira_trabalho = False
esta_trabalhando_atualmente = True
possui_veiculo_propio = False

print((maior_de_idade == True) and (possui_carteira_trabalho == True))
# outra forma de fazer
print(maior_de_idade and possui_carteira_trabalho)

# Queremos contratar pessoas que ainda não possuem um veiculo própio, mas já possua um carteira de trabalho.
print((possui_veiculo_propio == False) and (possui_carteira_trabalho == True))
# Outra forma de fazer, seria.
print(possui_carteira_trabalho == True and not possui_veiculo_propio)