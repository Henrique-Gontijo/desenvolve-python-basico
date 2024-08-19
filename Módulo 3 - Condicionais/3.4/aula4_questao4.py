# 4) Você está implementando um sistema de entrega expressa 
# e precisa calcular o valor do frete com base na distância 
# e no peso do pacote. Escreva um código que solicita a distância 
# da entrega em quilômetros e o peso do pacote em quilogramas. 
# O programa deve calcular e imprimir o valor do frete de 
# acordo com as seguintes regras:

    # - Distância até 100 km: R$1 por kg.
    # - Distância entre 101 e 300 km: R$1.50 por kg.
    # - Distância acima de 300 km: R$2 por kg.
    # - Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg


# Entrada de Dados: Distãncia da entrega e massa do pacote
distance = float(input("Digite a distância da entrega em quilômetros: "))
mass = float(input("Digite o peso da entrega em Kg: "))
freight = 0

# Processamento: 
    # Se a distâcia for até 100km, o frete é correspodente a 1 real a cada quilo
    # Se a distância for entre 101 e 300km, o frete é 1.5 a cada quilo
    # Se a disância for maior que 300km, o frete é 2 reais a cada quilo
    # Se o pacote pesar mais de 10kg é adicionada uma taxa de 10 reais

if distance <= 100:
    freight = mass

if 101 <= distance <= 300:
    freight = mass * 1.5

if distance > 300:
    freight = mass * 2

if mass > 10.0:
    freight += 10

# Saída de Dados: Valor do Frete

print(f"O valor do frete ficará em R${freight:,.2f}")