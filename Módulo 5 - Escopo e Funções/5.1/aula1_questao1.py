# Desenvolva um programa em Python que peça ao usuário para 
# inserir dois números decimais e calcule a diferença absoluta 
# entre esses dois números. Utilize a função nativa abs para 
# garantir que o resultado seja sempre positivo e round para 
# arredondar o resultado para duas casas decimais.

# Entrada: São solicitados dois valores para serem subtraidos
x = float(input("Digite um número decimal: "))
y = float(input("Digite outro número decimal: "))

# Processamento: É feita a subtração absoluta do número que é 
# Arredondada para duas casas decimais
sub = abs(x - y)
sub = round(sub, 2)

# Saída: Resultado aproximado da subtração
print(f"Resultado da subtração: {sub}")
