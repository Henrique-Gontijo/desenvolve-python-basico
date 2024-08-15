# 4) Escreva um programa que leia um valor inteiro referente a uma quantia 
# em reais e calcule a menor quantidade possível de notas necessárias 
# para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 
# A saída deve estar formatada exatamente como indicado. 

# Entrada:
# 576

# Saída:
    # 5 nota(s) de R$100,00
    # 1 nota(s) de R$50,00
    # 1 nota(s) de R$20,00
    # 0 nota(s) de R$10,00
    # 1 nota(s) de R$5,00
    # 0 nota(s) de R$2,00
    # 1 nota(s) de R$1,00


# Entrada de Dados: Solicitação do valor em reais
valor = int(input("Digite o valor em reais a ser pago: "))

# Processamento: Cálculo das notas necessárias para pagar o valor indicado

# Processo do Cálculo: É feita a divisão inteira para descobrir a quantidade 
# necessária de notas de 100 para pagar a dívida, depois é feito o módulo (resto)
# para descobrir qual é o valor restante para ser pago com as notas de 50,
# assim o processo se repete com as notas com valores menores

# Notas de R$100.00
notas_100 = valor // 100
valor %= 100

# Notas de R$50.00
notas_50 = valor // 50
valor %= 50

# Notas de R$20.00
notas_20 = valor // 20
valor %= 20

# Notas de R$10.00
notas_10 = valor // 10
valor %= 10

# Notas de R$5.00
notas_5 = valor // 5
valor %= 5

# Notas de R$2.00
notas_2 = valor // 2
valor %= 2

# Notas de R$1.00
notas_1 = valor // 1
valor %= 1


# Saída de dados: Quantidade de notas de 100, 50, 20, 10, 5, 2 e 1 real necessárias
# para pagar a dívida
print("Quantidade de notas necessárias para pagar a dívida:")
print(f"{notas_100} nota(s) de R$100.00")
print(f"{notas_50} nota(s) de R$50.00")
print(f"{notas_20} nota(s) de R$20.00")
print(f"{notas_10} nota(s) de R$10.00")
print(f"{notas_5} nota(s) de R$5.00")
print(f"{notas_2} nota(s) de R$2.00")
print(f"{notas_1} nota(s) de R$1.00")