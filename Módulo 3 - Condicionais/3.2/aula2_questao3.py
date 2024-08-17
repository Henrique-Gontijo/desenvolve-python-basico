# 3) Você está desenvolvendo um sistema de admissão para um clube 
# juvenil de jogos de tabuleiro. Escreva um programa em Python que 
# pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de 
# tabuleiro (resposta deve ser True ou False) e quantas vezes venceu 
# um jogo. O programa deve imprimir True, permitindo o ingresso do 
# participante no clube, se:

    # - tiver entre 16 e 18 anos
    # - já tiver jogado pelo menos 3 jogos
    # - já ter vencido pelo menos 1 jogo, 

# Sua expressão deve imprimir False caso contrário. Aqui está um 
# exemplo de interação com seu código no terminal, com entradas de 
# dados destacadas em negrito e as impressões de seu código em itálico 
# (apenas para facilitar sua visualização).

    # - Digite sua idade: 17
    # - Já jogou pelo menos 3 jogos de tabuleiro? True
    # - Quantos jogos já venceu? 2
    # - Apto para ingressar no clube de jogos de tabuleiro: True


# Entrada de Dados: É solicitada ao usuário algumas informações:

    # - Sua idade;
idade = int(input("Digite sua idade: "))

    # - Se já jogou pelo menos 3 jogos de tabuleiro;
print("Você já jogou, pelo menos, três jogos de tabuleiro? ")
experiencia = bool(input("Responda 'True' caso sim, ou 'False' caso não: "))

    # - Número de jogos que venceu.
vitorias = int(input("Quantos jogos você já venceu? "))


# Processamento: A admissão do usário é permitida caso os seguintes sejam verdadeiros

    # - O usuário tem entre 16 e 18 anos;
    # - O usuário já jogou pelo menos 3 jogos de tabulero;
    # - O usuário venceu pelo menos 1 partida

# Saída de dados: Se o usuário é apto ou não para ingressar no clube
print(f"Apto para ingressar no clube de jogos de tabuleiro: {15 < idade < 19 and experiencia == True and vitorias >= 1}")


