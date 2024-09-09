# 2) Solicite uma frase do usuário e usando compreensão de listas imprima:

    # - A lista de vogais da frase, ordenada alfabeticamente
    # - A lista de consoantes da frase

# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 
# 'y', 't', 'h', 'n']

def del_space(x):
    while " " in x:
        x.remove(" ")
vogais = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

frase = input("Digite uma frase: ")
frase = list(frase)
del_space(frase)
frase_vogais = [i for i in frase if i in vogais]
frase_consoantes = [i for i in frase if i not in vogais]
print(f"Vogais: {frase_vogais}")
print(f"Consoantes: {frase_consoantes}")