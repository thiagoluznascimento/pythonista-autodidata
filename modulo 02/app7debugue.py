# 14 - Como debugar seu código - Errar é humano
# para analisarmos linha por linha, temos que marca-la com o brack-point e para acionar o brack-point, utilizamos o f9
# para ativar o modo debug, utilizamos o f5 depois de ter marcado a linha com o f9. shift+f5 para sair do modo debug
# para acessar linha por linha, utilizamos o f10 e assim que acessa-la, ele executa.
# para entrar dentro de uma função, utilizamos o f11
#

print('Olá')

def calcular_preco_combo(pizza, refrigerante):
    total = pizza + refrigerante
    print('total')

calcular_preco_combo(20,10)
print('Programa finalizado')