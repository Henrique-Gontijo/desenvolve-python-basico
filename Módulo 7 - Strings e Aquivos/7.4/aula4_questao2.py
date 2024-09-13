# 2) Escreva um script que leia o arquivo salvo no exercício anterior e 
# salva em um novo arquivo "palavras.txt", removendo todos os espaços em 
# branco e caracteres não alfabéticos, e separando cada palavra em uma linha. 
# Ao final, imprima o conteúdo do arquivo "palavras.txt".

# Ex:
    # Bom
    # dia
    # meu
    # nome
    # é
    # Davi

import re

with open('frase.txt', 'r') as file:
    phrase = file.read()
    words = re.findall(r'[a-zA-Z]+', phrase)

with open('palavras.txt', 'w') as f1:
    for i in words:
        f1.write(str(i) + "\n")

with open('palavras.txt', 'r') as f2:
    text = f2.read()
    print(text)