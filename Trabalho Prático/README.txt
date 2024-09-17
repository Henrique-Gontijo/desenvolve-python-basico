INTRODUÇÃO

    A empresa modelada na verdade foi a desenvolvedora do programa, que estaria
desenvolvendo um protótipo de gerenciamento de estoque e pessoal para uma empre-
sa local, no caso a São Vicente Panificadora. A ideia foi inspirada pelo fato de
de na disciplina de projetos meu grupo trabalhou com a empresa. Então a Lelles
Developments seria como uma evolução dessa parceria, chegando a ponto da São
Vicente contrá-la para o desenvolvimento do próprio software.


IMPLEMENTAÇÃO


(1)
    A estrutura para o armazenamento de dados escolhida foi o formato de tabela 
(CSV). As informações estão aramazenadas dessa forma (separadas por vírgula) a 
fim de facilitar a interpretação das informações pelo programa. Esse utiliza as 
vírgulas como parâmetro para separar cada uma das informações contidas nos ar-
quivos.

(2)    
    O protótipo armazena as informações de usuários e de produtos em dois arquivos 
CSV. Em usuarios.csv, na primeira coluna temos o CPF da conta, na segunda coluna 
temos a senha, na terceira o nome completo do usuário e na quarta temos o cargo exer-
cido por ele. Já em produtos.csv, na primeira coluna temos o nome do produto, segui-
do pelo seu preço e pela quantidade em estoque.

(3)
    Para a criação de novos arquivos, o programa solicita as informações necessárias
para a criação de um novo item (cpf, senha, nome e cargo no caso de usuários, nome, 
preço e quantidade no caso de produtos), após isso ele as armazena em uma lista, que
é transformada em uma string, onde os dados são separados por vírgulas e adicionado 
ao arquivo (para que cada produto ou usuário fique em uma linha, após os dados é co-
locado um "\n" no final da string).
    Para a leitura das informações, o protótipo lê cada uma das linhas do arquivo,
armazenando cada linha em uma lista, separando os dados em strings dentro da lista.
Utilizando como parâmetro para a divisão as vírgulas.
    Para a edição de dados, o programa identifica a linha que o usuário deseja edi-
tar, solicita as informações que substituirão as antigas, e sobrescreve o arquivo 
original por uma cópia contendo as alterações.
    Para deletar os dados, o programa identifica linha que o usuário deseja excluir,
cria uma cópia do arquivo em uma variável sem a linha que o usuário deseja remover,
e sobrescreve o arquivo original.


CONCLUSÃO

    A maior dificuldade com certeza foi o gerenciamento de dados, a mainpulação de 
arquivos e a organização das funções, pois o código começou a ficar muito grande com
o tempo. Meus maiores acertos com certeza foram a divisão de subtarefas em funções,
o que deixou o código mais organizado e da utilização de while's para a criação
de menus que se repetem, permitindo que eu pudesse navegar para menus anteriores. A-
lém da criação da função para fechar o programa, que evitou a repetição do trecho de
código em diversas partes do código principal, ela também facilitou um pouco a reali-
zação de testes. Isso porque eu não precisava utilizar o "Ctrl + C", que gera uma es-
pécie de erro enorme no terminal, causando uma grande poluição visual, atrapalhando
para identificar as informações do próprio código.


    ATENÇÃO

    Junto com o código principal haverá um script chamado "gerador_cpf.py", cuja úni-
ca função é facilitar o processo de criação de novos usuários para o programa. Vale
destacar que os CPF's utilizados para os usuários no programa são aleatórios e que os 
nomes utilizados são meramente inlustrativos, não representando necessariamente pessoas
reais. Agradeço pela compreensão.