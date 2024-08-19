# 3) Você está desenvolvendo um programa para verificar se 
# um ano é bissexto. Escreva um código em Python que solicita 
# ao usuário para inserir um ano e imprime "Bissexto" se o 
# no for (1) divisível por 4 e não for divisível por 100, 
# ou (2) se for divisível por 400. Caso contrário, imprima 
# "Não Bissexto".

    # Teste seu código com os valores: 1900 (não bissexto), 
    # 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 
60
# Entarda de Dados:
    # É solicitado um ano para ser testado
year = int(input("Digite um ano e saiba de ele é bissexto ou não: "))

# Processamento / Saída de Dados:
    # É testado se o ano é bissexto de acordo com as seguintes condições:
        # - (1) For divisível por 4 e não for divisível por 100;
        # - (2) Se for divisível por 400.

    # Caso o ano antender às condições citadas é imprimido a mensagem de
    # que ele é bissexto, caso não, é imprimido que ele não é bissexto.

if ( (year % 4 == 0) and (year % 100 != 0) ) or (year % 400 == 0):
    print(f"O ano {year} é bissexto.")
else:
    print(f"O ano {year} não é bissexto.")
