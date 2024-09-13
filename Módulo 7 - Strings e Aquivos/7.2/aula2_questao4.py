# 4) Implemente uma função em Python chamada validador_senha() que 
# verifica se uma senha fornecida atende todos os seguintes critérios:

    # Pelo menos 8 caracteres de comprimento.
    # Contém pelo menos uma letra maiúscula e uma letra minúscula.
    # Contém pelo menos um número.
    # Contém pelo menos um caractere especial (por exemplo, @, #, $).

# Complete o seguinte código:
# def validador_senha(senha):
    #### Escreva a função

# Exemplo de uso:
# senha1 = "Senha123@"
# senha2 = "senhafraca"
# senha3 = "Senha_fraca"
# print(validador_senha(senha1))  # Saída esperada: True
# print(validador_senha(senha2))  # Saída esperada: False
# print(validador_senha(senha3))  # Saída esperada: False

lista_numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lista_letras_M = [chr(i) for i in range(65,91)]
lista_letras_m = [chr(i) for i in range(97,123)]
lista_especiais = [chr(i) for i in range(32,127) if (32 <= i <= 47) or 
                   (58 <= i <= 64) or (91 <= i <= 96) or (123 <= i <= 126)]


def validador_senha(senha):
    numeros = False
    letras_M = False
    letras_m = False
    especiais = False
    tamanho = len(senha) >= 8

    for i in senha:
        if i in lista_numeros:
            numeros = True
            break

    for i in senha:
        if i in lista_letras_M:
            letras_M = True
    
    for i in senha: 
        if i in lista_letras_m:
            letras_m = True
            break
    
    for i in senha:
        if i in lista_especiais:
            especiais = True
            break

    return tamanho and numeros and letras_M and letras_m and especiais

entrada = input("Digite a uma senha: ")
if validador_senha(entrada) == True:
    print("Sua senha é forte!")

else:
    print("Sua senha é fraca, tente outra senha.")