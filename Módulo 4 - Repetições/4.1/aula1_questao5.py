# Entrada: Número de participantes
n = int(input("Digite o número de respondentes da pesquisa: "))
cont = 1
idades = 0

# Processamento / Entrada: É solicitada a idade de cada um dos n participantes
# que são somadas em uma variável e é somando 1 à contagem. O proceso se  repete até
# a contagem se torne maior que o número de participantes
while cont <= n:
    idades += int(input(f"Digite a idade do {cont}⁰ respondente: " ))
    cont += 1

# Processamento / Saída: É imprimida a média das idades de todos os participantes
print (f"A média de idade dos respondentes é {idades / n:.0f}")
