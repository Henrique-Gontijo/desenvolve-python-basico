# 2) Desenvolva um programa que solicite ao usuário inserir uma frase 
# e substitua todas as ocorrências de vogal por "*".

# Ex:
    # Digite uma frase: O rato roeu a roupa do rei
    # Frase modificada: * r*t* r*** * r**p* d* r**


vogais =  ["A", "E","I", "O", "U", "a", "e", "i", "o", "u"]
frase = input("Digite uma frase: ")

for i in vogais:
    if i in frase:
        frase = frase.replace(i, "*")

print(f"Frase modificada: {frase}")

