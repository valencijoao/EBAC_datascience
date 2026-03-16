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
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

encoder = LabelEncoder()
df['Marca_Cod'] = encoder.fit_transform(df[['Marca']])
df['Material_Cod'] = encoder.fit_transform(df[['Material']])
df['Temporada_Cod'] = encoder.fit_transform(df[['Temporada']])

mapa_vendas = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}

df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(mapa_vendas)

marca_freq = df['Marca'].value_counts() / len(df) 
df['Marca_Freq'] = df['Marca'].map(marca_freq)

material_freq = df['Material'].value_counts() / len(df)
df['Material_Freq'] = df['Material'].map(material_freq)