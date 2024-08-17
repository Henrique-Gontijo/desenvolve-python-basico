# 1) Juliana e Cris querem entrar em um bar, mas só podem se 
# ambos forem maiores de idade (>17). Escreva um programa que 
# solicite as idades de Juliana e Cris e imprima True se ambas 
# forem maiores de 17 anos, indicando que podem entrar no bar, 
# e False caso contrário.

# Entrada de Dados: Idades de Cris e Juliana
idade_C = int(input("Qual é a idade de Cris? "))
idade_J = int(input("Qual é a idade de Juliana? "))

# Processamento: Cris e Julina têm 18 anos ou mais?
# Saída de Dados: Se Cris e Juliana Podem entrar no bar
print("Permissão de entrada no bar:", idade_C > 17 and idade_J > 17)