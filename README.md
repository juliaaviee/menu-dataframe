# menu-dataframe
## Descrição

Exemplo:
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





