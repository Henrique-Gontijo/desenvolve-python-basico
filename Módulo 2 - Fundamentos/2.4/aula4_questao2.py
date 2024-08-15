#2) Leia um valor inteiro correspondente a uma temperatura em graus 
# Fahrenheit e apresente-a convertida em graus Celsius.

# Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus 
# Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o 
# valor em Celsius para inteiro. 

# A mensagem deve estar formatada da seguinte maneira:

# 86 graus Fahrenheit são 30 graus Celsius.

#Entrada de Dados: Valor da temperatura em graus Fahrenheint
fahrenheint = int(input("Qual a temperatura em graus Fahrenheint? "))
#Processamento: Cálculo da temperatura em graus Celsius
celsius = (fahrenheint - 32) * (5/9)
#Saída de Dados: Impressão da temperatura em Fahrenheit e em Celsius
print(f"{fahrenheint:.0f} graus Fahrenheint são {int(celsius)} graus Celsius.")