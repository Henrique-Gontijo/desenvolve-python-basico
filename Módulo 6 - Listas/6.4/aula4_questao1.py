#   1) Escreva um script python que use compreensão de listas para 
# criar as seguintes listas:

    # - Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
    # - Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
    # - Todos os números entre 1 e 100 que sejam divisíveis por 7
    # - Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" 
    # dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 

pares = [ i for i in range(20,50,2)]
print(pares)
quadrados = [i ** 2 for i in range(1,10,)]
print(quadrados)
divisores_7 = [i for i in range(1,101) if i % 7 == 0 ]
print(divisores_7)
paridade = ["par" if i % 2 == 0 else "ímpar" for i in range(0,30,3)]
print(paridade)