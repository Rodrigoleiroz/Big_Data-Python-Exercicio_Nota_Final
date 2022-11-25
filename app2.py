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




# c. Agrupe os dados pelos cursos de Matemática, Medicina e Pedagogia.----------------------------------------------------




# d. Agrupe os dados por Estado.-------------------------------------------------------------------------------------------




# e. Agrupe os dados pelos cursos Tecnológicos.----------------------------------------------------------------------------




# f. Elimine a coluna “cidade_filtro” do dataframe.------------------------------------------------------------------------




# g. Apresente a média das mensalidades dos cursos de Medicina.------------------------------------------------------------




# h. Média das notas de corte dos cursos de tempo integral.---------------------------------------------------------------




# i. Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado.---------------------------------------------





# j. Gráfico comparativo entre o grau dos cursos (Bacharelado, Licenciatura, Tecnologia, etc) pelas Notas Integral de Cotas.--