# 10 - Números e Operações Matemáticas
#Tipos de numeros que podem ser usados no python 
a = 20
b = 20.6
print(type(a))
print(type(b))
# operacoes matematicas com python
print(10 + 6)
print(10 - 6)
print(10 * 6)
print(10 / 6)
print(10 // 6) #divisão de inteiro. Diz quantas vezes um numero pode ser inserido dentro de outro
print(10 % 6) #modulus. Resto da divisão
print(10 ** 6) #exponecial 
# Atalho para atribuição mais rápida
a = 10
a = a + 5
print(a)
a += 5
print(a)

b = 30
b = b - 2
print(b)
b -= 2
print(b)

# Arredondamento
print(round(7.5))

#como arredondar para valores maiores ou seja, pra cima, no nosso caso seria 3 . para isso import a bibli math
import math
print(round(2.2))
print(math.ceil(2.2))
