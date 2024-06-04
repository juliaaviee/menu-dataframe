# menu-dataframe
## Descrição

Este é um projeto para análise de dados sobre alimentos, utilizando Python e Pandas para processar e visualizar os dados. *Foi utilizado o Google Collab.*

COMO FOI DESENVOLVIDO O PROJETO?

1) Criando a base de dado

Primeiramente a estrutura de dados utilizada foi um Dicionário (Menu), com dados sobre comidas (os dados fornecidos experimentalmente por inteligencia artificial). Cada chave recebeu um valor de lista. chaves: (Comida, Tipo, Calorias, Proteína e Gordura). 

2) Convertendo o Dicionário para Dataframe

Utilizando a biblioteca Pandas (pd) criei um dataframe a partir do dicionário Menu: df_Menu, esse dataframe sendo uma estrutura de dados tabular com colunas sendo as chaves e as linhas sendo os itens das linhas.

Finalizando imprimindo a base de dados Menu.

3) Medindo o tamanho da base de dados

Utilizando o metodo '.shape' que retornará uma tupla com o numero de linhas e colunas no dataframe.

4) Acessando a uma Linha Específica do DataFrame

-- print(df_Menu.loc[1]) --
Utilizei o método '.loc' para acessar uma linha ou coluna do DataFrame pelo rótulo. está acessando a linha com índice 1.
Resultado: Esta operação retorna a linha inteira do DataFrame df_Menu que tem o índice 1. A linha é retornada como uma Série pandas, onde os índices são os nomes das colunas e os valores são os dados da linha correspondente. O código é bastante simples e serve para exibir as características de uma linha específica de um DataFrame pandas, identificada pelo seu índice.

5) Apresentando em tela os 5 primeiros registros da base de dados

A função head() é um método do DataFrame que retorna as primeiras linhas do DataFrame. Ela recebe um argumento opcional que indica o número de linhas a serem retornadas. No caso, recebeu o argumento 5 especifica que apenas as 5 primeiras linhas devem ser retornadas. As linhas retornadas são exibidas no console.

6) Excluindo uma linha

A função utilizada é o '.drop()', que é um método do DataFrame usado para excluir linhas ou colunas, método drop() é usado no DataFrame df_Menu e recebe o argumento 3, indicando o índice da linha a ser removida.
Pandas retorna um novo objeto DataFrame contendo as alterações.
Depois imprimi o código no console e usei o método display para vizualizar os dados de forma mais interativa como tabelas.

7) Adicionando uma nova linha

--df_Menu.loc[len(df_Menu)]--
O método '.loc' é usado para acessar linhas e colunas do dataframe df_Menu. A variável preco_medio recebe as informações que vão ser adicionadas as chaves do dataframe.
df_Menu.loc[len(df_Menu)]: Seleciona a última linha do dataframe.
df_Menu. len(df_Menu) retorna o número total de linhas no dataframe.

8) Mudando colunas para linhas

dataframe_transposed = df_Menu.T vai criar um novo dataframe. A transposição troca as linhas e colunas.
A última linha df_Menu = df_Menu.transpose() modifica o dataframe original df_Menu para que ele seja agora a transposição original.

9) Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados


O método '.iloc' é usado para indexar e selecionar partes de um dataframe usando posições numéricas.
As linhas print("9) 1ª e 2ª coluna:") e print(df_Menu.iloc[:, :2]) e print(df_Menu.iloc[:, 0:2]) exibem as duas primeiras colunas do DataFrame df_Menu.
O código seleciona e exibe as duas primeiras colunas do DataFrame df_Menu. As duas formas de selecionar as colunas ([:, :2] e [:, 0:2]) são equivalentes e usam o método iloc para acessar as posições desejadas.



