# 5) A extensão ".csv" significa "comma-separated values" ou "valores 
# separados por vírgula". É a extensão utilizada por sistemas de gerência 
# de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos 
# criar uma planilha com dados sobre livros que você já leu ou gostaria de 
# ler. Siga as instruções.

    # - Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você 
        # deve reunir as seguintes informações: título, autor, ano de publicação 
        # e número de páginas.

    # - No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.

    # - Na primeira linha escreva os títulos da planilha separados por vírgula 
        # (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de 
        # publicação" e "Número de páginas". Lembre de finalizar a linha com uma 
        # quebra de linha.

    # - A partir da segunda linha escreva as informações de cada livro que você 
        # levantou, separando cada informação por uma vírgula (sem espaço em 
        # branco). Lembre de finalizar cada linha com uma quebra de linha.

    # - Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de 
        # sua escolha. Como você já tem conta no Google, sugiro abrir com o 
        # Google Sheets.

# Seu arquivo deve ser aberto como uma planilha parecida com a imagem anexada 
# neste exercício.

with open("meus_livros.csv", "w") as arquivo:
    arquivo.write("Título, Autor, Ano de Publicação, Número de Páginas \n")
    arquivo.write("A Torre Negra: O Pistoleiro, Stephen King, 1982, 262  \n")
    arquivo.write("O Iluminado, Stephen King, 1977, 464 \n")
    arquivo.write("A Árvore que Dava Dinheiro, Domingos Pellegrini, 1981, 128 \n")
    arquivo.write("Eragon, Christopher Paolini, 2002, 468 \n")
    arquivo.write("Jogos Vorazes, Suzanne Collins, 2008, 400 \n")
    arquivo.write("Harry Potter e a Pedra Filosofal, J. K. Rowling, 1997, 264 \n")
    arquivo.write("Como viver para sempre, Colin Thompson, 1995, 240 \n")
    arquivo.write("Portugal e Espanha, Geraldo Rodrigues da Costa, 2016, 188 \n")
    arquivo.write("O Cavaleiro Andante, George R. R. Martin, 1998, 400 \n")
    arquivo.write("O Poço e o Pêndulo, Edgar Allan Poe, 1842, 72 \n")
    arquivo.write("O Código Da Vinci, Dan Brown, 2003, 432 \n")