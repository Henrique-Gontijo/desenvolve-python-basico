# 5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e 
# seu tempo de serviço (em anos) e escreva uma expressão que imprima 
# True se a pessoa já pode se aposentar, ou False caso contrário, 
# de acordo com as seguintes regras:

    # - A: Para mulheres, ter mais de 60 anos. Para homens, 65.
    # - B: Ou ter trabalhado pelo menos 30 anos
    # - C: Ou ter 60 anos  e trabalhado pelo menos 25.


# Entrada de Dados: É perguntado gênero, idade e tempo de serviço ao usuário
genero = input ("Qual o seu gênro? Digite 'M' para 'masculino' e 'F' para 'feminino': ")
idade = int(input("Digite sua idade: "))
t_servico = int(input(" Digite seu tempo de serviço em anos: "))
aposentadoria = bool(False)

# Processamento: São testadas diferentes condições para a aposentadoria 
# em relação aos dados obtidos:

a = (genero == "F" and idade > 60) or (genero == "M" and idade > 65)
b = (t_servico >= 30)
c = (idade == 60 and t_servico >= 25)
aposentadoria = a or b or c

# Saída de Dados: Possibilidade da pessoa aposentar ou não de acordo com 
# os dados coletados
print(f"Aptidão para aposentar: {aposentadoria}")