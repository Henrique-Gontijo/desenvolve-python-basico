# 4) Você é mestre de uma mesa de RPG e vai criar um sistema para 
# validar uma ficha de personagem. Cada personagem tem uma classe 
# específica com requisitos de atributos. Escreva um script que 
# solicita a classe de personagem escolhida (guerreiro, mago ou 
# arqueiro), os pontos de força e os pontos de magia atribuídos ao 
# personagem. O programa deve imprimir True se os pontos de atributo 
# são consistentes com a classe escolhida, seguindo as seguintes regras:

    # - Guerreiro: Força deve ser igual ou superior a 15, Magia 
    # deve ser 10 ou menos.

    # - Mago: Força deve ser 10 ou menos, Magia deve ser igual 
    # ou superior a 15.

    # - Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum 
    # deles pode ser superior a 15.

# O programa deve imprimir False se os pontos de atributo não são 
# consistentes com a classe escolhida. Segue um exemplo de interação 
# com seu código no terminal, com entradas de dados destacadas em negrito 
# e as impressões de seu código em itálico.

    # - Escolha a classe (guerreiro, mago ou arqueiro): mago
    # - Digite os pontos de força (de 1 a 20): 8
    # - Digite os pontos de magia (de 1 a 20): 17
    # - Pontos de atributo consistentes com a classe escolhida: True


# Entrada de Dados: Classe pontos de força e pontos de magia do personagem
print("Escolha a classe (guerreiro, mago ou arquiro)")
classe = input("Digite o nome com todas as lestras em caixa baixa: ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))


# Processamento: Classificação se o personagem é válido ou não de acordo com
# a classe e as características ca classe

guerreiro = classe == "guerreiro" and forca >= 15 and magia <= 10
mago = classe == "mago" and forca <= 10 and magia >= 15
arqueiro = "arqueiro" and (5 <= forca <= 15) and (5 <= magia <= 15)


# Saída de Cados: O personagem é válido ou não
print (f"Pontos de atributo consistentes com a classe escolhida: {(guerreiro or mago or arqueiro)}")
