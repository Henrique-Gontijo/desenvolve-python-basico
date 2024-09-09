
#1) Escreva um script em Python que solicita do usuário uma quantidade 
# indefinida de números inteiros (pelo menos 4 valores), os armazena em 
# uma lista e, usando fatiamento de listas, imprima:

    # - A lista original
    # - Os 3 primeiros elementos
    # - Os 2 últimos elementos
    # - A lista invertida (do fim para o começo)
    # - Os elementos de índice par (0, 2, 4 … )
    # - Os elementos de índice ímpar (1, 3, 5, … )

lista = []

a = int(input("Escreva o tamanho da lista (mínimo = 4): "))
if a < 4:
    a = 4


for i in range(a):
    lista.append(int(input("")))

print(lista)
print(lista[:2:])
print(lista[(a - 2)::])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])