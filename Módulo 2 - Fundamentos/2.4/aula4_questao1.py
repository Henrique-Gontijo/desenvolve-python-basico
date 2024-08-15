# 1) Faça um programa para ler as dimensões de um terreno em inteiros 
# (comprimento e largura), bem como o preço do metro quadrado da região 
# em ponto flutuante. Calcule o valor do terreno e imprima o resultado 
# com a formatação apresentada a seguir.

# O terreno possui 250m2 e custa R$512,490.50

# Comente na linha acima de cada instrução uma breve descrição da instrução.
# Fórmulas:

    # - area_m2 = comprimento * largura
    # - preco_total = preco_m2 * area_m2



#Entarada de Dados: comprimento do terreno
comprimento = int(input("Em metros, qual o comprimento do terreno? "))
#Entrada de Dados: largura do terreno
largura = int(input("Em metros, qual a largura do terreno? "))
#Entrada de Dados: preço do m² do terreno
preco_m2 = float(input("Qual é o preço do metro quadrado da região? "))
#Processamento: Cálculo da área do terreno
area_m2 = comprimento * largura
#Processamento: Cálculo do valor do terreno
preco_total = preco_m2 * area_m2
#Saida de Dados: Tamanho e valor do terreno
print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}")