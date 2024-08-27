# Escreva um programa em Python que utiliza a biblioteca 
# datetime para exibir a data e hora atuais com a 
# formatação apresentada a seguir:
    # - Data: 15/03/2023 
    # - Hora: 14:05


# Você pode consultar esse tutorial da Alura sobre a biblioteca 
# datetime. Existem várias maneiras de resolver essa questão. 
# Uma sugestão é:

    # - Função datetime.datetime.now() cujo retorno possui os 
    # atributos: day, month, year, hour, minute

    # - Usar a formatação com f-strings no momento de imprimir. 
    # Atenção para os atributos que devem sempre ter 2 dígitos 
    # precedidos por zero se necessário.

# Entrada: È difinida em uma variável a data e hora em que o script é 
# executado.
import datetime
data_hora = datetime.datetime.now()

# Saída: É imprimida a data e a hora definidas na varíavel, com formatação
print(f"Data: {data_hora.strftime('%d/%m/%Y')}")
print(f"Hora: {data_hora.strftime('%H:%M')}")