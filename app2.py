import numpy as np
import pandas as pd

# Importando arquivo .CSV para ser utilizado no exercicio numero 2
df = pd.read_csv("datasets/cursos-prouni.csv")


# a. Efetuar a limpeza das colunas de notas: onde tiver NaN (Not a Number), substituir por 0,0.----------------------------
df['nota_integral_ampla'].fillna('0,0', inplace = True)
df['nota_integral_cotas'].fillna('0,0', inplace = True)
df['nota_parcial_ampla'].fillna('0,0', inplace = True)
df['nota_parcial_cotas'].fillna('0,0', inplace = True)
print(df.head())



# b. Agrupe os dados pelo grau (Bacharelado, Licenciatura, etc).-----------------------------------------------------------
df_grau = df.groupby('grau')

#Utilizando o 'describe' para mostrar a agrupacao por grau, mas a funcao 'describe' gera várias informações adicionais.
print(df_grau.describe().head(10))

#Utilizando a funcao 'get_group' para selecionar o grupo a ser exibido dentro da coluna 'grau'.
df_grau_bachar = df_grau.get_group('Bacharelado').head(10)
print(df_grau_bachar)

df_grau_licen = df_grau.get_group('Licenciatura').head(10)
print(df_grau_licen)

df_grau_tecno = df_grau.get_group('Tecnológico').head(10)
print(df_grau_tecno)




# c. Agrupe os dados pelos cursos de Matemática, Medicina e Pedagogia.----------------------------------------------------
df_cursos_mat_med_ped = df.groupby('nome')

df_curso_med = df_cursos_mat_med_ped.get_group('Medicina').head(10)
print(df_curso_med)

df_curso_mat = df_cursos_mat_med_ped.get_group('Matemática').head(10)
print(df_curso_mat)

df_curso_ped = df_cursos_mat_med_ped.get_group('Pedagogia').head(10)
print(df_curso_ped)





# d. Agrupe os dados por Estado.-------------------------------------------------------------------------------------------
df_estados = df.groupby('uf_busca')
print(df_estados.describe().head(10))



# e. Agrupe os dados pelos cursos Tecnológicos.----------------------------------------------------------------------------
df_grau2 = df.groupby('grau')

df_grau_tecno = df_grau2.get_group('Tecnológico').head(10)
print(df_grau_tecno)


# f. Elimine a coluna “cidade_filtro” do dataframe.------------------------------------------------------------------------
df.drop('cidade_filtro', axis = 1, inplace=True)
print(df.head(10))


# g. Apresente a média das mensalidades dos cursos de Medicina.------------------------------------------------------------
df_cursos = df.groupby('nome')

df_curso_med2 = df_cursos.get_group('Medicina').head(10)

media = df_curso_med2.mean()['mensalidade']

print(media)



# h. Média das notas de corte dos cursos de tempo integral.---------------------------------------------------------------




# i. Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado.---------------------------------------------





# j. Gráfico comparativo entre o grau dos cursos (Bacharelado, Licenciatura, Tecnologia, etc) pelas Notas Integral de Cotas.--