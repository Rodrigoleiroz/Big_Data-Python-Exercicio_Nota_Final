import numpy as np
import pandas as pd
#A
#Agrupe os dados por tipo de bebidas ----------------------

df = pd.read_csv("datasets/world_alcohol.csv")

df_bebidas = df.groupby('Beverage Types')

print(df_bebidas)


#B
#Agrupe os dados por Região e por Ano ---------------------

df_regiao_ano = df.groupby(['WHO region', 'Year'])

print(df_regiao_ano)

#C
#Seção de Contagens: (I) Contar a ocorrência de Regiões, (II) de Países e a (III) soma da coluna de valores por Bebida ------------
#(I)
df_regiao = df.groupby('WHO region')
print(df_regiao.count())

#(II)
df_pais = df.groupby('Country')
print(df_pais.count())

#(III)
print(df_bebidas.sum())















