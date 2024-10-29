# -*- coding: utf-8 -*-
import pandas as pd

# Criando um dicionário com dados sobre comidas
Menu = {
    'Comida': ['Pizza', 'Hambúrguer', 'Salada', 'Sushi', 'Taco', 'Sorvete'],
    'Tipo': ['Fast Food', 'Fast Food', 'Saudável', 'Japonês', 'Mexicano', 'Sobremesa'],
    'Calorias': [266, 295, 152, 200, 226, 207],
    'Proteína': [11, 17, 3, 8, 12, 3],
    'Gordura': [10, 12, 5, 7, 9, 11]
};

df_Menu = pd.DataFrame(Menu);

# df_Menu = pd.DataFrame(data);

# Pergunta 1 - Imprimir base de dados:
print("1) Base de dados completa:")
print(Menu);

# Pergunta 2 - tamanho
print("2) Tamanho do dataframe:")
print(df_Menu.shape)

# Pergunta 3
x = 0 # Substitua pelo valor da linha desejada
print(f"3) Características da linha {1}:")
print(df_Menu.loc[1])

# Pergunta 4
print("4) Verificação se o dataframe está vazio:")
if df_Menu.empty:
    print("O dataframe está vazio.")
else:
    print("O dataframe não está vazio.")

# Pergunta 5 - Apresente em tela os 5 primeiros registros da base de dados.
print("5) Primeiros 5 registros:")
print(df_Menu.head(5))

# Pergunta 6 - Realize a exclusão de uma linha
df_Menu = df_Menu.drop(3)

print(Menu)
display(Menu)

# Pergunta 7 - Realize a adição de uma linha
Preco_medio = {'Comida': "pao de queijo", 'Tipo': "mineira", 'Calorias': 157, 'Proteína': 2, 'Gordura': 5,}
df_Menu.loc[len(df_Menu)] = Preco_medio
print(df_Menu)

# Pergunta 8 - Transponha a coluna para a linha em sua base de dados.
dataframe_transposed = df_Menu.T
print("8) Transposição da coluna para a linha:")
print(dataframe_transposed)
df_Menu = df_Menu.transpose()

# Pergunta 9 - Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados.
print("9) 1ª e 2ª coluna:")
print(df_Menu.iloc[:, :2])
print(df_Menu.iloc[:, 0:2])
