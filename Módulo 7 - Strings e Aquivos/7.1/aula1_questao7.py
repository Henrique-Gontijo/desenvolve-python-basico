import random

def encrypt(lista):
    lst_cripto = []
    for nome in lista:
        novo_nome = ""
        for letra in nome: 
            letra_cripto = chr((ord(letra) + chave_aleatoria))
            novo_nome += letra_cripto
        lst_cripto.append(novo_nome)
    return lst_cripto

nomes = []
n = int(input("Digite o número de nomes: "))
for i in range(n):
    nomes.append(input(""))

chave_aleatoria = random.randint(1, 10)


lista_letras = encrypt(nomes)
print(lista_letras)