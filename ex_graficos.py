import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def converter_vendas(valor):
    valor = str(valor).lower()

    if "mil" in valor:
        numero = re.findall(r'[\d,.]+', valor)[0]
        numero = float(numero.replace(",", "."))
        return int(numero * 1000)

    numero = re.findall(r'\d+', valor)

    if numero:
        return int(numero[0])

    return None


df = pd.read_csv('ecommerce_preparados.csv')

# roteiro para tratar os dados -> remover nulos, remover as colunas 'Título' , 'Review' , padronizar números, reduzir casas decimais, fazer levantamento de dados únicos
df = df.drop(columns=["Unnamed: 0"])

print(df.isnull().sum())

df["Desconto"] = df["Desconto"].fillna(0)

print(df[['Marca', 'Material', 'Gênero']].isnull().sum())

df["Material"] = df["Material"].fillna("Não_informado")
df["Gênero"] = df["Gênero"].fillna("Não_informado")

df["Qtd_Vendidos_Num"] = df['Qtd_Vendidos'].apply(converter_vendas)
 
print(df["Qtd_Vendidos_Num"].unique)


plt.figure(figsize=(10,6))
plt.hist2d(
    df["Preço"],
    df["Qtd_Vendidos_Num"],
    bins=30
)
plt.colorbar()
plt.xlabel("Preço")
plt.ylabel("Qtd Vendidos")
plt.savefig("heatmap.png")
