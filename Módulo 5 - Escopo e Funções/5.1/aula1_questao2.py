# Escreva um código que gere n valores inteiros aleatórios 
# entre 0 e 100 e calcule a raíz quadrada da soma dos valores. 
# Peça ao usuário o valor de n

    # Biblioteca random: Função randint()
    # Biblioteca math: Função sqrt()

import random
import math

n = int(input("Digite um número: "))
sum = 0

for i in range(n):
    sum += random.randint(0, 100)

print(f"Raíz quadrada: {math.sqrt(sum)}")