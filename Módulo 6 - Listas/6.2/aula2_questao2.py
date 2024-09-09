# 2) Faça um programa que gere aleatoriamente um valor entre 5 
# e 20 e armazene em uma variável chamada num_elementos. Em seguida 
# gere aleatoriamente valores entre 1 e 10 em quantidade correspondente 
# a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:

    # - A lista elementos
    # - A soma dos valores da lista
    # - A média dos valores da lista

import random
nums = list()
x = random.randint(5, 20)
for i in range(x):
    nums.append(random.randint(1, 10))

print("Lista:")
print(nums)
print(f"Soma dos itens da lista: {sum(nums)}")
print(f"Média dos números da lista: {sum(nums)/len(nums)}")
