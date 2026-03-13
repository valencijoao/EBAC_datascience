import pandas as pd

df = pd.read_csv('clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format ='%d/%m/%Y', errors ='coerce')

# Informações sobre o data frame, quantidade de não-nulos e tipo de objeto
print('Verificação incial:')
print(df.info())

# Análise dos dados nulos
print('Análise dos dados nulos:\n', df.isnull().sum()) # Se nulo = True, True é 1 e False é 0, Sum soma todos os True encontrados
print('% de dados nulos:\n', df.isnull().mean() *100) # Em uma lista de 0s e 1s, a média é exatamente a proporção de 1s (nulos)
df.dropna(inplace=True)
print('Confirmar remoção de nulos:\n', df.isnull().sum().sum()) # Soma o total, deve resultar em 0

print('Análise de dados duplicados:\n', df.duplicated().sum())

print('Análise de dados únicos:\n', df.nunique())

print('Estatística dos dados:\n', df.describe())

df = df[['idade','data','estado','salario','nivel_educacao','numero_filhos','estado_civil','area_atuacao']]
print(df.head().to_string)

df.to_csv('clientes-v2_tratado.csv', index=False)
