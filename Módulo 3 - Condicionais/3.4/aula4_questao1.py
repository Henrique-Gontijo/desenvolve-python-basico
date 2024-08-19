# 1) Escreva um programa que lê dois números e informa se a sua 
# soma é par ou ímpar. Critério: se o resto da divisão do número 
# por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se 
# do operador do python % que retorna o resto de uma divisão.

# Entrada de Dados: 
    # São solicitados dois números para serem somados
print("Me entregue dois números e eu irei dizer se a soma deles é par ou ímpar.")
x = int(input("Digite um número: "))
y = int(input("Agora digite outro número: "))

# Processamento:
    # Cálculo da Soma dos dois núemeros coletados
soma = x + y

# Processamento / Saída de Dados:
    # É testado se a soma é par ou ímpar
    # É imprimida a soma e se ela é par ou ímpar
if (x + y) % 2 == 0:
    print(f"A soma de {x} com {y} é {x + y}, que é par.")

else:
    print(f"A soma de {x} com {y} é {x + y}, que é ímpar.")