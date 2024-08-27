# Escreva um programa em Python que utiliza a biblioteca 
# random para gerar um número aleatório entre 1 e 10 e peça 
# ao usuário para adivinhar o número. Forneça feedback se 
# o palpite é muito alto, muito baixo ou correto. Interrompa 
# a execução somente quando o usuário acertar o palpite.

import random

print("Eu irei gerar um número de 1 a 10")
print("Seu objetivo é tentar acertar o meu número")
print("Eu irei te ajudar dizendo se seu palpite foi muito alto ou muito baixo caso erre")
print("Vamos começar!")

# Processamento: É definido um número de 1 a 10 em uma variável e é solicitado
# ao usauário que digite algum número, caso o número digitado pelo usuário seja
# o mesmo definido pela variável é exibida uma mensagem indicando que ele acertou
# e o processo termina, caso o número digitado seja mmaior que o da variável
# isso é informado ao usuário, o mesmo acontece caso seja menor
n = random.randint(1, 10)
while True:
    a = int(input("Digite um número: "))

    if a == n:
        print("Você acertou!")
        break

    elif n < a:
        print("Muito alto")

    else:
        print("Muito baixo")

print("Fim de Jogo!")