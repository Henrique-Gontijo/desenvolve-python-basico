# 2) Dando continuidade à questão anterior, um outro bar permite 
# a entrada de grupos onde pelo menos uma pessoa é maior de idade 
# (ficando responsável pelas outras). Ajuste sua resposta da questão 
# anterior, ainda solicitando as idades de Juliana e Cris, mas 
# ajustando a expressão para esse novo cenário, imprimindo True se 
# puderem entrar no bar, e False caso contrário.


# Entrada de Dados: Idades de Cris e Juliana
idade_C = int(input("Qual é a idade de Cris? "))
idade_J = int(input("Qual é a idade de Juliana? "))

# Processamento: Cris ou Julina têm 18 anos ou mais?
# Saída de Dados: Se Cris e Juliana Podem entrar no bar
print("Permissão de entrada no bar:", idade_C > 17 or idade_J > 17)