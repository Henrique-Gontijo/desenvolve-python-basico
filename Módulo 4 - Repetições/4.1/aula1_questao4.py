# Entrada: Valor n
n = int(input("Digite um número: "))
maior = 0

# Processamento / Entrada: Se n for mairo que 0 é solictado um valor x que será definido como ""maior" 
# x seja maior que o "maior" anterior. Indpendente de x ser maior ou não, é subtraido 1 de n
# O processo se repete até que n = 0
while n > 0:

    x = int(input("Digite outro número: "))
    if x > maior: 
        maior = x
    n -= 1

# Saída: Valor de "maior"
print (maior)