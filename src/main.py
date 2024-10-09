import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Passo 1: Carregar o dataset a partir do arquivo Excel
df = pd.read_excel("Online Retail.xlsx")

# Passo 2: Explorar os dados para identificar as variáveis importantes
print("Primeiras linhas do dataset:")
print(df.head())
print("\nInformações gerais do dataset:")
print(df.info())

# Passo 3: Limpeza de Dados
# Remover linhas com valores nulos e registros de transações negativas
df = df.dropna()
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Calcular o valor total de cada compra
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Passo 4: Criar uma nova tabela de segmentação por cliente
# Agregar por 'CustomerID' para obter as variáveis de segmentação
customer_data = df.groupby('CustomerID').agg({
    'InvoiceNo': 'count',         # Frequência de Compras
    'TotalPrice': 'sum',          # Valor Total Gasto
    'Quantity': 'sum'             # Quantidade Total Comprada
}).reset_index()

# Renomear colunas para facilitar a interpretação
customer_data.columns = ['CustomerID', 'Frequency', 'TotalSpent', 'TotalQuantity']

# Passo 5: Normalizar os dados para aplicar o clustering
scaler = StandardScaler()
scaled_data = scaler.fit_transform(customer_data[['Frequency', 'TotalSpent', 'TotalQuantity']])

# Passo 6: Aplicar o K-Means para encontrar clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_data)
customer_data['Cluster'] = kmeans.labels_

# Passo 7: Visualização com PCA
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

# Visualização dos clusters
plt.figure(figsize=(10, 6))
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=customer_data['Cluster'], cmap='viridis')
plt.title('Clusters de Clientes - PCA')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()

# Passo 8: Análise dos clusters
print("Análise dos clusters:")
print(customer_data.groupby('Cluster').mean())
