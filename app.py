import numpy as np
import pandas as pd

# Importando arquivo .CSV para ser utilizado no exercicio numero 1
df = pd.read_csv("datasets/world_alcohol.csv")

#A
print("A-")
#Agrupe os dados por tipo de bebidas ----------------------

df_bebidas = df.groupby('Beverage Types')

#Print para visualizacao no console da referencia do objeto dataframe agrupado.
print(df_bebidas)

#Utilizando o 'describe' para mostrar a agrupacao por bebidas, mas essa funcao gera várias informações adicionais.
print(df_bebidas.describe().head(10))


#B
print("B-")
#Agrupe os dados por Região e por Ano ---------------------

df_regiao_ano = df.groupby(['WHO region', 'Year'])

#Print para visualizacao no console da referencia do objeto dataframe agrupado.
print(df_regiao_ano)

#Utilizando o 'describe' para mostrar a agrupacao por regiao e ano, mas essa funcao gera várias informações adicionais.
print(df_regiao_ano.describe().head(10))

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


print("Média")
#media dos valores por tipo de bebida
df_bebidas3 = df.groupby('Beverage Types')
media = df_bebidas3.mean()['Display Value']
print(media)

print("Mediana")
#mediana dos valores por tipo de bebida
df_bebidas4 = df.groupby('Beverage Types')
mediana = df_bebidas4.median()['Display Value']
print(mediana)

print("Moda")
# moda dos valores por tipo de bebida
df_bebidas5 = df.groupby('Beverage Types').size()
moda = [df_bebidas5.idxmax(), df_bebidas5.max()]
print(moda)

print("Estatística Descritiva")
#Estatística Descritiva dos valores por tipo de bebida
df_bebidas6 = df.groupby('Beverage Types')
esta_desc = df_bebidas6.describe()['Display Value']
print(esta_desc)

print("Gráfico de comparação dos valores")
#Gráfico de comparação dos valores por tipo de bebida

# grafico = df.loc[df['Display Value'] >= 0]
# print(grafico.plot.bar(x='Beverage Types'))



#O "describe" fornece muitas informacoes, media, mediana, desvio padrao, etc.


#E
print("E-")
#Mostre resultados de acordo com alguns critérios:

print("Coluna de bebidas do ano de 1985")
# I. Mostrar a coluna de bebidas do ano de 1985.
df_ano = df.groupby('Year')
print(df_ano.get_group(1985)['Beverage Types'])


print("Coluna de de Regioes com valores acima de 4")
# II. Mostrar a coluna de Regioes com valores acima de 4.


df_regiao2 = df.groupby('WHO region').size()

dict = df_regiao2.to_dict()
for i in dict:
    if dict[i] > 4:
        print (i)
    

























