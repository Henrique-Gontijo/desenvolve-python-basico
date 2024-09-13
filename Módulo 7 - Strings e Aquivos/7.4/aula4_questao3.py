# 3) Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" 
# (link a seguir) e salve em seu computador com o nome "estomago.txt". 

# Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt

# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 

    # - O texto das primeiras 25 linhas
    # - O número de linhas do arquivo
    # - A linha com maior número de caracteres
    # - O número de menções aos nomes dos personagens "Nonato" e "Íria" 
        # inclua todas as variações de maiúsculas e minúsculas e atenção 
        # para não incluir a substring "iria" se ela fizer parte de outras palavras).

with open('estomago.txt', 'r') as f:
    linhas = f.readlines()

for i in range(0, 26):
    print(linhas[i].rstrip())

n_linhas = 0
nonato = 0
iria = 0

linha_max = ""
for linha in linhas:
    n_linhas += 1
    linha_quebrada = linha.split()

    if len(linha) > len(linha_max):
        linha_max = linha
    
    for palavra in linha_quebrada:
        palavra_normalizada = palavra.strip(',.!?;').lower()
        if palavra_normalizada == "nonato":
            nonato += 1
        elif palavra_normalizada == "íria":
            iria += 1

print("")
print(f"Número total de linhas: {n_linhas}")
print("Linha com maior número de caracteres:")
print("")
print(linha_max)
print("")
print(f"Número de menções a Nonato: {nonato}")
print(f"Número de menções a Íria: {iria}")
