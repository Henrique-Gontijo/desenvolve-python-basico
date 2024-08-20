# Entrada: Notas 1, 2 e 3
n1 = int(input(" Digite a nota 1: "))
n2 = int(input(" Digite a nota 2: "))
n3 = int(input(" Digite a nota 3: "))

# Processamento: É feita a média das notas
m = (n1 + n2 +n3)/3

# Processamento / Saída: Se a nota for = ou > 600 imprime aprovado
# Se for > ou = 40 é recuperação, já se for < que 40 é reprovado
if m >= 60:
    print("Aprovado")

elif m >= 40:
    print ("Recuperação")

else:
    print("Reprovado")

print("Fim")