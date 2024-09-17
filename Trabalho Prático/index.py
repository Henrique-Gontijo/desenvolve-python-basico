import csv

# Função para fechar o programa
def fechar_programa():
    # A função deste loop (e de outros semelhantes) é repetir o processo
        # caso a resposta recebida não corresponda a nenhuma das opções
    while True:
        resposta = input("Você tem certeza que quer sair do programa? (S/N): ").lower()
        # Verificação: Se a resposta for sim, o progrma é fechado, caso não, a função 
            # termina e o menu anteriror é executado novamente
        if resposta == "s":
            print("")
            print("Obrigado por utilizar nosso software!")
            print("Lembre-se, isso é apenas um protótipo para testar as funcionalidades do programa!")
            print("O projeto final pode ser muito diferente da versão atual.")
            exit()
        elif resposta == "n":
            print("")
            break
        else:
            print("Resposta inválida! Tente novamente")
            continue

# Função de criação de novos usuários
def criar_conta():
    # Primeiro o arquivo é aberto
    arquivo_usuarios = open("usuarios.csv", "a")

    # É solicitado o CPF, senha, nome completo e cargo do novo usuário
    print("Digite o CPF:")
    cpf = input("")
    print("Digite a senha:")
    senha = input("")
    print("Digite o nome completo:")
    nome = input("")
    teste = False
    while teste == False:
        print("digite o cargo (gerente/funcionário)")
        cargo = input("").lower()
        # Esse loop verifica se o cargo digitado está nas opções disponíveis, caso não,
            # é informado que o cargo está errado e o loop exige o cargo novamente
        if cargo == "gerente" or cargo == "funcionário":
            teste = True
            print("")
            break
        else:
            print("Cargo inválido! Tente novamente")

    # Por fim as informações são armazenadas em uma lista, que é convertida em string e adicionada ao arquivo
    conta = [ cpf, senha, nome, cargo, "\n"]
    conta = ",".join(conta)
    arquivo_usuarios.write(conta)
    arquivo_usuarios.close()

# Função de qesquida de conta
def pesquisar_conta():
    # Primeiro a função lê o arquivo e armazena as linhas em uma lista
    with open("usuarios.csv", "r") as file:
        contas = file.readlines()
        contas = [i.split(",") for i in contas]
    
    # É solicitado o CPF ou nome completo do funcionário
    print("Digite o CPF ou nome completo do funcionário:")
    pesquisa = input("").lower()
    encontrado = False

    # O for testa linha por linha se a entrada está contida no campo de nome ou de CPF, enumerando
        # cada uma das linhas
    for indice, conta in enumerate(contas):
        # Quando a conta é encontrada, a função retorna o índice em que está a conta
        if pesquisa == conta[0] or pesquisa == conta[2].lower():
            print(f"CPF: {conta[0]}")
            print(f"Nome: {conta[2]}")
            print(f"Senha: {conta[1]}")
            print(f"Cargo: {conta[3]}")
            print("")
            indice_encontrado = indice
            encontrado = True
            return indice_encontrado
    
    # Caso a conta não seja ecotrada, é imprimida uma mensagem dizendo isso e é retornado o valor None
    if encontrado == False:
        print("Conta não encontrada")
        print("")
        return None

# Função para eibir todas as contas existentes
def exibir_contas():
    # O arquivo das contas é lido e as linhas são armazenadas em uma lista
    with open("usuarios.csv", "r") as file:
        contas = file.readlines()
        contas = [i.split(",") for i in contas]
    
    # Para cada conta existente, é imprimido o CPF e o nome completo
    for conta in contas:
        print(f"{conta[0]} - {conta[2]}")
    print("")



# Função para adicionar produtos
def adicionar_produto():
    # É solicitado o nome, preço e quantidade do produto
    arquivo_produtos = open("produtos.csv", "a")
    print("Digite o nome do Produto:")
    produto_nome = input("")
    print("Digite o preço (R$):")
    preco = input("")
    print("Digite a quantidade:")
    quantidade = input("")
    print("")

    # As informações coletadas são armazenadas na lista, que se transforma em string para assim ser adicionada
        # no arquivo
    produto = [produto_nome, str(preco), quantidade, "\n"]
    produto = ",".join(produto)
    arquivo_produtos.write(produto)
    arquivo_produtos.close()

def pesquisar_produto():
    # Primeiro as linhas do arquivo são lidas e armazenadas em uma lista
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = arquivo_produtos.readlines()
        produtos = [i.split(",") for i in produtos]

    # É solicitado o nome do produto
    print("Digite o nome do produto:")
    pesquisa = input("").lower()
    print("")

    encontrado = False
    # O for identifica cada linha com um índice e passa por cada uma delas
    for indice, produto in enumerate(produtos):
        # Quando o produto é encontrado, são exibidos nome, preço e quantidade, além de ser retornado o índice
            # do produto
        if pesquisa == produto[0].lower():
            print(f"Produto: {produto[0]}")
            print(f"Preço: R${float(produto[1]):.2f}")
            print(f"Quantidade: {produto[2]}")
            print("")
            encontrado = True
            indice_encontrado = indice
            return indice_encontrado
    
    # Se não for encontrado, é exibida uma mensagem dizendo isso e é retornado o valor None
    if encontrado == False:
        print("Produto não encontrado")
        print("")
        return None

def exibir_produtos():
    # Primeiro são idas as linhas do produto
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = arquivo_produtos.readlines()
        produtos = [i.split(",") for i in produtos]
    
    # É imprimido um cabeçalho
    print("Produto / Preço / Quantidade")
    # O for imprime o nome, preço e quantidade de cada produto
    for produto in produtos:
        print(f"{produto[0]} - R${float(produto[1]):.2f} - {produto[2]}")
    print("")


# Função para editar arquivo
def editar_item(arquivo, linha_a_ser_editada, novos_dados):
    # Primeiro o arquivo é lido em csv e suas linhas são armazenadas em uma lista
    with open(arquivo, mode="r") as file:
        leitor = csv.reader(file)
        linhas = list(leitor)
    
    # O valor da linha com o índice que se deseja editar é substituída pelo valor em novos_dados
    linhas[linha_a_ser_editada] = novos_dados
    
    # O arquivo é aberto para escrita, e cada linha que está na lista (incluindo a alterada) sobrescrevem
        # o arquivo original
    with open(arquivo, mode = "w", newline = "") as file:
        escritor = csv.writer(file)
        escritor.writerows(linhas)

# Função para apagar linhas do arquivo
def apagar_item(arquivo, linha_a_ser_removida):
    # Cada linha do arquivo csv é colocada em uma lista
    with open(arquivo, "r") as file:
        leitor = csv.reader(file)
        linhas = list(leitor)

    # A linha com o índice que se deseja remover é apagada
    del linhas[linha_a_ser_removida]

    # O arquivo é sobrescrito com a lista em que a linha desejada foi apagada
    with open(arquivo, "w", newline = "") as file:
        escritor = csv.writer(file)
        escritor.writerows(linhas)

# Saudações
print("São Vicente Panificadora")
print("Prótipo de Sistema Interno para Gerenciamento Estoque e Pessoal")
print("Agradecemos pela preferência pela Lelles Developments")
print("")

# Menu inicial
while True:
    print("Escolha uma operação")
    print("1 - Login")
    print("0 - Sair")
    answer = input("Opção: ")

    # Caso a operaçã Login (1) seja exigida, o loop acaba e é executada os 
        #comandos subsequentes, caso seja Sair (0), é executada a função
        # de confirmação. Se a resposta não corresponder a nenhuma operação,
        # o loop se repete.
    if answer == "1":
        print("")
        break
    elif answer == "0":
        fechar_programa()
    else:
        print("Resposta operação inválida! Tente novamente")
        print("")


# Leitura do arquivo de usuários a fim de identificar usuários
with open("usuarios.csv", "r") as users_file:
    usuarios = users_file.readlines()

# Divisão das linhas em listas contendo as informações dos usuários
usuarios = [i.split(",") for i in usuarios]

# Loop de acesso que reinicia enquanto o acesso não for permitido
acesso = False
while acesso == False:
    # Solicitação de login e senha
    print("Digite seu login:")
    login = input("")
    print("Digite a sua senha:")
    senha = input("")

    # Este trecho verifica um por um dos usuários existentes, testando
        # se o login e senha digitados correspondem a algum deles
    for usuario in usuarios:
        # Caso o login e senhas digitados seja correspondente a algum usuário
            # o acesso é permitido e o cargo do usuário é registrado
        if (login == usuario[0] or login == usuario[2]) and senha == usuario[1]:
            print("")
            print("Acesso permitido!")
            print(f"Seja bem-vindo {usuario[2]}")
            print("")
            acesso = True
            permissao_tipo = usuario[3].rstrip()
    
    # Caso o acesso não tenha sido permitido do for, é exibida uma mensagem de erro
    if acesso == False:
        print("Acesso Negado!")
        print("Senha ou login incorretos!")
        print("")

# Opções de menu do gerente
if permissao_tipo == "gerente":
    # O loop serve para repetir o menu sempre uma opção inexistente for digitada, além de permitir
        # que o usuário possa voltar para ele caso termine de fazer o que precesa em "Contas" ou "Prdutos"
        # e deseje trocar de opção
    while True:
        # Ipresão do menu + solicitação de opção
        print("Opções:")
        print("1 - Contas")
        print("2 - Produtos")
        print("0 - Sair")
        answer = input("Opção: ")
        print("")
        # Caaso a entrada for 1 é aberto o menu de contas
        if answer == "1":
            # O while serve para repetir o menu sempre que o usuário terminar de realizar alguma ação em
                # alguma subseção
            while True:
                print("Operações:")
                print("1 - Criar nova conta")
                print("2 - Pesquisar usuário")
                print("3 - Exibir contas")
                print("4 - Voltar para o menu anterior")
                print("0 - Sair")
                answer = input("Opção: ")
                print("")
                if answer == "0":
                    # Ao digitar 0 é executada a função de verificação para fechar o programa
                    fechar_programa()
                elif answer == "1":
                    # Ao digitar 1 é executada a função de criar conta
                    criar_conta()
                elif answer == "2":
                    # Ao digitar 2 é exeecutada a função de pesquisar conta, e seu retorno é armazenado em
                        # uma variável
                    indice = pesquisar_conta()
                    # Caso seja éncontrada uma conta (ou seja, valor retornado seja diferente de None) é 
                        # perguntado ao usuário se ele gostaria de apagar ou editar a conta
                    if indice != None:
                        answer = input("Gostaria de editar ou apagar essa conta? (S/N): ").lower()
                        print("")
                        # Caso sim, é exigida uma opção 
                        if answer == "s":
                            print("Operações:")
                            print("1 - Apagar conta")
                            print("2 - Editar conta")
                            answer = input("Opção: ")
                            print("")
                            if answer == "1":
                                # Caso a resposta seja 1, é executada a função de apagar item, dando como parâmetro
                                    # arquivo dos usuáros e o índice da conta
                                apagar_item("usuarios.csv", indice)
                            
                            elif answer == "2":
                                # Caso a resposta seja 2, são solicitados o novo cpf, a nova senha,
                                    # o novo nome e o novo cargo
                                new_cpf = input("Digite o novo cpf: ")
                                new_password = input("Digite a nova senha: ")
                                new_name = input("Digite o novo nome: ")
                                new_position = input("Digite o novo cargo: ")
                                # É executada a função de edição, sendo passados como parâmetro o arquivo, o índice da
                                    # conta e as novas infomações
                                editar_item("usuarios.csv", indice, [new_cpf, new_password, new_name, new_position])
                elif answer == "3":
                    # São exibidas as contas
                    exibir_contas()
                elif answer == "4":
                    # É dado um break no loop, assim, este menu é encerrado e o loop do menu anterior começa
                        # a ser executado
                    break
                else:
                    # Caso nenhuma das opções anteriosrs sejam atendidas, significa que a opção não existe
                    print("Resposta operação inválida! Tente novamente")
                    print("")

        elif answer == "2":
            while True:
                print("Operações:")
                print("1 - Adicionar produto")
                print("2 - Pesquisar produto")
                print("3 - Exibir produtos")
                print("4 - Voltar para o menu anterior")
                print("0 - Sair")
                answer = input("Opção: ")
                print("")
                if answer == "0":
                    # Ao digitar 0 é executada a função de verificação para fechar o programa
                    fechar_programa()
                elif answer == "1":
                    # Ao digitar 1 é executada a função de criar produto
                    adicionar_produto()
                elif answer == "2":
                    # Ao digitar 2 é exeecutada a função de pesquisar produto, e seu retorno é armazenado em
                        # uma variável
                    indice = pesquisar_produto()
                    # Caso seja éncontradao um produto (ou seja, valor retornado seja diferente de None) é 
                        # perguntado ao usuário se ele gostaria de apagar ou editar o produto
                    if indice != None:
                        answer = input("Gostaria de editar ou apagar esse produto? (S/N): ").lower()
                        print("")
                        if answer == "s":
                            # Caso sim, é exigida uma opção 
                            print("Opções:")
                            print("1 - Apagar produto")
                            print("2 - Editar produto")
                            answer = input("Opção: ")
                            print("")
                            if answer == "1":
                                # Caso a resposta seja 1, é executada a função de apagar item, dando como parâmetro
                                    # arquivo dos produtos e o índice da produto
                                apagar_item("produtos.csv", indice)
                        
                            elif answer == "2":
                                # Caso a resposta seja 2, são solicitados o novo nome, a preço,
                                    # e a quantidade
                                new_name = input("Digite o novo nome: ")
                                new_price = float(input("Digite o novo preço: "))
                                new_quantity = input("Digite a nova quantidade: ")
                                # É executada a função de edição, sendo passados como parâmetro o arquivo, o índice do
                                    # produto e as novas infomações
                                editar_item("produtos.csv", indice, [new_name, str(new_price), new_quantity])

                            else:
                                print("Resposta operação inválida! Tente novamente")
                                print("")
                elif answer == "3":
                    # São exibidas as contas
                    exibir_produtos()
                elif answer == "4":
                    # É dado um break no loop, assim, este menu é encerrado e o loop do menu anterior começa
                        # a ser executado
                    break
                else:
                    # Caso nenhuma das opções anteriosrs sejam atendidas, significa que a opção não existe
                    print("Resposta operação inválida! Tente novamente")
                    print("")

else: 
    while True:
        print("Opções:")
        print("1 - Minha conta")
        print("2 - Produtos")
        print("0 - Sair")
        answer = input("Opção: ")
        print("")

        if answer == "0":
            fechar_programa()
        elif answer == "1":
            with open("usuarios.csv", "r") as file:
                contas = file.readlines()
                contas = [i.split(",") for i in contas]
                # Este trecho verifica um por um dos usuários existentes, testando
                        # se o login digitado corresponde a algum deles
            for indice, conta in enumerate(contas):
                # Quando a conta é encontrada, imprime as informações da conta
                if login == conta[0] or login == conta[2].lower():
                    print(f"CPF: {conta[0]}")
                    print(f"Nome: {conta[2]}")
                    print(f"Senha: {conta[1]}")
                    print(f"Cargo: {conta[3]}")
                    print("")
                    indice_encontrado = indice
            
            # É perguntado ao usuário se ele gostaria de alterar a senha
            answer = input("Gostaria de trocar a sua senha? (S/N): ").lower()
            if answer == "s":
                # Caso sim, a nova senha é solicitada
                print("Digite a nova senha: ")
                new_password = input("")

                # As informações originais da conta (cpf, nome e cargo) são armazendas em uma lista junto com
                    # a nova senha
                editado = [contas[indice_encontrado][0],new_password ,contas[indice_encontrado][2], 
                            contas[indice_encontrado][3]]
                
                # A função de edição de arquivo é executada, recebendo como parâmetros o arquivo dos usuários,
                    # o índice da conta do funcionário e a lista com a senha nova
                editar_item("usuarios.csv", indice_encontrado, editado)
                print("")
        
        elif answer == "2":
            while True:
                print("Operações:")
                print("1 - Adicionar produto")
                print("2 - Pesquisar produto")
                print("3 - Exibir produtos")
                print("4 - Voltar para o menu anterior")
                print("0 - Sair")
                answer = input("Opção: ")
                print("")
                if answer == "0":
                    # Ao digitar 0 é executada a função de verificação para fechar o programa
                    fechar_programa()
                elif answer == "1":
                    # Ao digitar 1 é executada a função de criar produto
                    adicionar_produto()
                elif answer == "2":
                    # Ao digitar 2 é exeecutada a função de pesquisar produto, e seu retorno é armazenado em
                        # uma variável
                    indice = pesquisar_produto()
                    # Caso seja éncontradao um produto (ou seja, valor retornado seja diferente de None) é 
                        # perguntado ao usuário se ele gostaria de apagar ou editar o produto
                    if indice != None:
                        answer = input("Gostaria de editar ou apagar esse produto? (S/N): ").lower()
                        print("")
                        if answer == "s":
                            # Caso sim, é exigida uma opção 
                            print("Opções:")
                            print("1 - Apagar produto")
                            print("2 - Editar produto")
                            answer = input("Opção: ")
                            print("")
                            if answer == "1":
                                # Caso a resposta seja 1, é executada a função de apagar item, dando como parâmetro
                                    # arquivo dos produtos e o índice da produto
                                apagar_item("produtos.csv", indice)
                        
                            elif answer == "2":
                                # Caso a resposta seja 2, são solicitados o novo nome, a preço,
                                    # e a quantidade
                                new_name = input("Digite o novo nome: ")
                                new_price = float(input("Digite o novo preço: "))
                                new_quantity = input("Digite a nova quantidade: ")
                                # É executada a função de edição, sendo passados como parâmetro o arquivo, o índice do
                                    # produto e as novas infomações
                                editar_item("produtos.csv", indice, [new_name, str(new_price), new_quantity])

                            else:
                                print("Resposta operação inválida! Tente novamente")
                                print("")
                elif answer == "3":
                    # São exibidas as contas
                    exibir_produtos()
                elif answer == "4":
                    # É dado um break no loop, assim, este menu é encerrado e o loop do menu anterior começa
                        # a ser executado
                    break
                else:
                    # Caso nenhuma das opções anteriosrs sejam atendidas, significa que a opção não existe
                    print("Resposta operação inválida! Tente novamente")
                    print("")
        else:
            print("Opção inválida! Tente novamente")
            print("")