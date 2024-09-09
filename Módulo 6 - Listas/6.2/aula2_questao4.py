# 4) Crie um programa em Python que receba duas listas de números do 
# usuário, podendo cada lista ter uma quantidade diferente de valores. 
# Em seguida, combine essas duas listas de forma alternada para formar 
# uma terceira lista. Intercale os elementos até o final da primeira 
# lista, adicionando ao final os elementos remanescentes da maior lista.

# Exemplo de interação via terminal (entradas em negrito):
    # Digite a quantidade de elementos da lista 1: 4
    # Digite os 4 elementos da lista 1:
    # 1
    # 2
    # 3
    # 4
    # Digite a quantidade de elementos da lista 2: 6
    # Digite os 6 elementos da lista 2:
    # 5
    # 6
    # 7
    # 8
    # 9
    # 10
    # Lista inter: 1 5 2 6 3 7 4 8 9 10


lista1 = list()
lista2 = list()
inter = list()

def lista(tamanho, lista):
    for i in range(tamanho):
        (lista).append(int(input("")))

x = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {x} elementos da lista 1:")
lista(x, lista1)

y = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {y} elementos da lista 2:")
lista(y, lista2)

for item in range(min(len(lista1), len(lista2))):
    inter.append(lista1[item])
    inter.append(lista2[item])

if len(lista1) > len(lista2):
    inter.extend(lista1[len(lista2):])
else:
    inter.extend(lista2[len(lista1):])

print(inter)