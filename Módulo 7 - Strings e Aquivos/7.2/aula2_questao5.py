# 5) De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano 
# consegue ler palavras com as letras embaralhadas, contanto que a primeira 
# e a última letra estejam no lugar correto. Implemente uma função chamada 
# embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. Sua 
# função vai receber uma frase, embaralhar as letras internas de cada palavra 
# e retornar a frase modificada. Dica: use a biblioteca random.

# Complete o seguinte código:
# def embaralhar_palavras(frase):
    #### Escreva a função

# Exemplo de uso:
    # frase = "Python é uma linguagem de programação"
    # resultado = embaralhar_palavras(frase)
    # print(resultado)
    ### Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

import random

def embaralhar_palavras(phrase):
    letter_list = []
    broken_phrase = phrase.split()
    word_list = [list(i) for i in broken_phrase]
    for word in word_list:
        letter_list.append(list(word))
    
    ordened_frags = [[i[0], "".join(sorted(i[1:-1], key=lambda x: random.random())), i[-1]] if len(i) 
                                    > 3 else i for i in word_list]
    
    ordened_words = ["".join(i) for i in ordened_frags]
    ordened_phrase = " ".join(ordened_words)
    return ordened_phrase

print("Digite uma frase: ")
frase = input("")
result = embaralhar_palavras(frase)
print("Frase embaralhada: ")
print(result)
                     