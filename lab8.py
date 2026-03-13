import pandas as pd

df = pd.read_csv('/data/ecommerce2g.csv')
df = df.drop_duplicates()
df = df.dropna(thresh=8)

# Exercício 1:
# Verifique a quantidade de linhas e colunas
linhas_colunas = df.shape
print('Verificar a qtd de Linhas e colunas: ', linhas_colunas)

# Verifique os tipos de dados
tipos = df.dtypes
print('Verificar Tipagem:\n', tipos)

# Verifique a quantidade de valores nulos
nulos = df.isnull().sum()
print('Verificar valores nulos:\n', nulos)

#  Substitua os valores nulos das colunas ‘Temporada’ e ‘Marca’ por ‘Não Definido’
ajuste_colunas = ['Temporada', 'Marca']
df[ajuste_colunas] = df[ajuste_colunas].fillna('Não Definido')

# Exercício 2:
# Escreva seu código abaixo

# Converter a coluna 'Marca' para letras minúsculas

# Converter a coluna 'Material' para letras minúsculas

# Converter a coluna 'Temporada' para letras minúsculas

letras_minusculas = ['Marca', 'Material', 'Temporada']
df[letras_minusculas] = df[letras_minusculas].apply(lambda x: x.str.lower())

print('Colunas convertidas para letras minúsculas:\n', letras_minusculas)


# Remover linhas duplicadas


# Remover linhas com menos de 8 valores não nulos
# O parâmetro 'thresh' define o número mínimo de valores não nulos necessários para manter a linha




