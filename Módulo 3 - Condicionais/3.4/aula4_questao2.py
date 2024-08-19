# 2) Você está criando um sistema de classificação de filmes 
# com base nas avaliações dos usuários. Escreva um programa em 
# Python que solicita ao usuário para inserir a avaliação de 
# um filme em uma escala de 1 a 5. O programa deve imprimir uma 
# mensagem correspondente à classificação do filme:

    # - Se a avaliação for 5, imprima "Excelente!"
    # - Se a avaliação for 4, imprima "Muito Bom!"
    # - Se a avaliação for 3, imprima "Bom!"
    # - Se a avaliação for 2, imprima "Regular."
    # - Se a avaliação for 1, imprima "Ruim."

# Entrada de Dados:
    # Nome do Filme
    # Nota de 1 a 5 sobre o filme
film = input("Qual é o nome do filme? ")
grade = int(input("Em uma escala de 1 a 5, qual é sua opnião sobre o filme? "))

# Processamento / Saída de Dados:
    #  É imprimida uma mensagem diferente dependendo da nota dada ao filme
print(f"Sua classificação para {film} é:")
if grade == 1:
    print("Ruim.")

if grade == 2:
    print("Regular.")

if grade == 3:
    print("Bom!")

if grade == 4:
    print("Muito Bom!")

if grade == 5:
    print("Excelente!")
