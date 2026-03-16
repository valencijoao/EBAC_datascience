import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados.csv')

# Escreva seu código abaixo

# Verifica a quantidade de dados únicos em cada coluna
unicos = df.nunique()
print('Analise de dados únicos:\n', unicos)

# Calcula estatísticas descritivas dos campos numéricos
estatisticas = df.describe()
print('Estatísticas dos dados:\n', estatisticas)

# Cria o campo "Preço" com o cálculo em relação aos campos "Reais" e "Centavos"

df['preço'] = df['reais'] + (df['centavos']/100)

# Remova os campos citados nas intruções e armazene novamente na variável `df`
df = df.drop(['reais','centavos','condicao','condicao_atual'], axis= 1)

scaler = MinMaxScaler()
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
df['N_Avaliações_MinMax'] = scaler.fit_transform(df[['N_Avaliações']])
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

encoder = LabelEncoder()
df['Marca_Cod'] = encoder.fit_transform(df[['Marca']])
df['Material_Cod'] = encoder.fit_transform(df[['Material']])
df['Temporada_Cod'] = encoder.fit_transform(df[['Temporada']])
