anagrama = []
frase = [input("Digite uma frase: ")]
palavra = sorted(input("Digite a palavra objetivo: "))
n = len(palavra)

for i in range(len(frase) - n + 1):
    substring = frase[i: i + n]
    if sorted(substring) == palavra :
        anagrama.append(substring)

print(f"Anagramas: {anagrama}")