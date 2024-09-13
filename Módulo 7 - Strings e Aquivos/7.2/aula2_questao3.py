# 3) Desenvolva um programa que verifique se uma frase fornecida pelo 
# usuário é um palíndromo (ou seja, lida da mesma forma de trás para 
# frente). Ignore espaços em branco ou sinais de pontuação, e considere 
# maiúsculas e minúsculas da mesma forma. Seu programa deve continuar 
# rodando até que o usuário digite "Fim".Ex:

    # Digite uma frase (digite "fim" para encerrar): Radar
    # "Radar" é palíndromo
    # Digite uma frase (digite "fim" para encerrar): Bom dia!
    # "Bom dia!" não é palíndromo
    # Digite uma frase (digite "fim" para encerrar): Ame o poema
    # "Ame o poema" é palíndromo
    # Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
    # "A Daniela ama a lei? Nada!" é palíndromo
    # Digite uma frase (digite "fim" para encerrar): fim


while True:
    frase_original = input("Digite uma frase (digite 'fim' para encerrar): ")
    if frase_original.lower() == "fim":
        break

    frase_modificada = ''.join([i for i in frase_original if i.isalpha()])
    frase_modificada = frase_modificada.lower()

    if frase_modificada == frase_modificada[::-1]:
        print(f"'{frase_original}' é um palíndromo!")
    else:
        print(f"'{frase_original}' não é um palíndromo!")