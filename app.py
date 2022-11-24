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
#Seção de Contagens: Contar a ocorrência de Regiões, de Países e a soma da coluna de valores por Bebida ------------
















