# 1) Faça um programa que gere aleatoriamente 20 valores inteiros entre 
# -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

    # - A lista ordenada, sem modificar a lista original
    # - A lista original
    # - O índice do maior valor da lista
    # - O índice do menor valor da lista

import random

numbers = list()

for i in range(20):
    numbers.append(random.randint(-100, 100))

max_index = numbers.index(max(numbers)) 
min_index = numbers.index(min(numbers))

print("Lista em ordem crescente:")
print(sorted(numbers))
print("")
print("Lista Original")
print(numbers)
print("")
print("Índice do maior número:")
print(max_index)
print("")
print("Índice do mnor número:")
print(min_index)