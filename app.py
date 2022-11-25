import numpy as np
import pandas as pd

#A
print("A-")
#Agrupe os dados por tipo de bebidas ----------------------

df = pd.read_csv("datasets/world_alcohol.csv")

df_bebidas = df.groupby('Beverage Types')

df_bebidas

#Print para visualizacao no console o objeto dataframe agrupado.
print(df_bebidas)


#B
print("B-")
#Agrupe os dados por Região e por Ano ---------------------

df_regiao_ano = df.groupby(['WHO region', 'Year'])

#Print para visualizacao no console o objeto dataframe agrupado.
print(df_regiao_ano)

#C
print("C-")
#Seção de Contagens: (I) Contar a ocorrência de Regiões, (II) de Países e a (III) soma da coluna de valores por Bebida ------------
#(I)
print("I-")

df_regiao = df.groupby('WHO region').size()
print(df_regiao)

#(II)
print("II-")

df_pais = df.groupby('Country').size()
print(df_pais)

#(III)
print("III-")

df_bebidas2 = df.groupby('Beverage Types')
print(df_bebidas2.sum()['Display Value'])

#D
print("D-")
#Realize análises estatísticas da coluna dos valores: Média, Moda, Mediana, Estatística Descritiva e Gráfico de comparação dos valores agrupados por tipo de bebida ------

#media dos valores por tipo de bebida
print(df_bebidas.mean()['Display Value'])

#mediana dos valores por tipo de bebida
print(df_bebidas.median()['Display Value'])

#moda dos valores por tipo de bebida
# df_valores = df.groupby('Display Value')
# print(df_bebidas.mode(df_valores))


#O "describe" fornece muitas informacoes, media, mediana, desvio padrao, etc.
print(df_bebidas.describe()['Display Value'])

#E
print("E-")
#Mostre resultados de acordo com alguns critérios:

# I. Mostrar a coluna de bebidas do ano de 1985.
df_ano = df.groupby('Year')
print(df_ano.get_group(1985)['Beverage Types'])

# II. Mostrar a coluna de Região com valores acima de 4.


df_regiao2 = df.groupby('WHO region').size()

dict = df_regiao2.to_dict()
for i in dict:
    if dict[i] > 4:
        print (i)
    
# 2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------


























