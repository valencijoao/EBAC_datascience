import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2_tratado.csv')

print(df.head())

df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1 ) # transforma os valores em números

print('\nDataFrame após codificação one-hot para variável estado_civil:\n', df.head())

educacao_ordem = {'Ensino Fundamental': 1,
                  'Ensino Médio': 2,
                  'Ensino Superior': 3,
                  'Pós-Graduação': 4
}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print(df.head())


