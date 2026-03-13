import pandas as pd

df = pd.read_csv('/data/ecommerce_ex4.csv')
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

# Remover linhas duplicadas

# Remover linhas duplicadas

# Remover linhas com menos de 8 valores não nulos

# O parâmetro 'thresh' define o número mínimo de valores não nulos necessários para manter a linha

letras_minusculas = ['Marca', 'Material', 'Temporada']
df[letras_minusculas] = df[letras_minusculas].apply(lambda x: x.str.lower())

print('Colunas convertidas para letras minúsculas:\n', letras_minusculas)

# Exercício 3:

# Calcular o intervalo interquartil (IQR)
q1 = df['N_Avaliacoes'].quantile(0.25)
q3 = df['N_Avaliacoes'].quantile(0.75)
iqr = q3 - q1

# Definir o limite superior para identificar outliers
limite_alto = q3 + 1.5 * iqr

# Filtrar os produtos que possuem um número de avaliações maior que o limite superior
df_avaliados = df[df['N_Avaliacoes'] > limite_alto]

# Exercício 4:

# Escreva seu código abaixo

# Extrair e limpar os dados da coluna 'Condicao'
# A função lambda é usada aqui para pegar a primeira palavra da string na coluna 'Condicao'
# x.split(' ')[0] pega a primeira palavra da string.
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split(' ')[0])

# A função lambda é usada aqui para pegar a quinta palavra da string na coluna 'Condicao' se existir,
# caso contrário, retorna 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split(' ')[4] if len(x.split(' ')) > 5 else 'Nenhum')

# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

# A função lambda é usada aqui para remover o símbolo '%' da string na coluna 'Desconto'
df['Desconto'] = df['Desconto'].apply(lambda x: str(x).split('%')[0])












