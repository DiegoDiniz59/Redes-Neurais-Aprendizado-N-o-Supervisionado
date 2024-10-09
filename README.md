# Atividade 4 – Redes Neurais e Aprendizado Não Supervisionado

### Professor: Otaviano Silvério de Souza.
### Aluno: Diego Diniz Amaral de Sá (RA: 12119820).

--------------------------------------------------------------------

## 1) Interpretação dos clusters: Fazer uma análise dos clusters identificados. Discutir o que cada grupo representa e possíveis insights, como perfis de cliente.

Resposta: O código da atividade utiliza o algoritmo K-Means para identificar três clusters com base nas variáveis "Annual Income (k$)" e "Spending Score (1-100)". A análise deles pode ser feita observando a distribuição dos pontos no gráfico gerado e as características específicas dos clientes que cada cluster representa.

Cluster 0: Representa clientes com baixo rendimento e baixo gasto. Este grupo inclui consumidores mais econômicos, que preferem não gastar muito em compras. Podem estar mais focados em necessidades básicas e utilidades.

Cluster 1: Representa clientes com alto rendimento e alto gasto. Eles podem ser classificados como consumidores de luxo, dispostos a gastar mais, e valorizam mais produtos premium e experiências de compra. Estratégias de marketing voltadas para itens de luxo e alta qualidade seriam mais adequadas para este grupo.

Cluster 2: Representa clientes com alto rendimento e baixo gasto. Estes são consumidores mais moderados, que possuem capacidade financeira, mas preferem gastar moderadamente. Podem valorizar descontos, ofertas e ter um comportamento de compra mais calculado.

Possíveis insights que poderíamos tirar dessa análise seriam, por exemplo: 

Em relação ao Cluster 1, ele é o grupo mais valioso em termos de lucro potencial, pois combina alta capacidade de renda com uma disposição elevada para o gasto. Campanhas de fidelização e programas exclusivos seriam ótimas ideias para se usar com eles.

Já o Cluster 2 pode ser o alvo de campanhas para aumentar a taxa de conversão e incentivar mais gastos, explorando estratégias como ofertas personalizadas para eles.
Cluster 0 não é o foco principal de estratégias de vendas que visam altos lucros, mas pode ser interessante para produtos de baixo custo e ofertas econômicas.

## 2) Alterar o número de clusters e observar os impactos.

Resposta: Segue a imagem do reajuste do código abaixo. 

![image](https://github.com/user-attachments/assets/9367dc7a-9106-45e8-af62-cd8d531167ee)

Analisando os impactos das alterações, podemos ver que ao mudar para 4 Clusters, nós temos: 

Subdivisão dos Grupos Originais: Um dos clusters originais pode ser dividido em dois novos subgrupos. Por exemplo, um grupo com alto rendimento e gasto moderado pode se dividir em consumidores com gasto muito alto e consumidores mais moderados.

Clusters mais semelhantes: Com um número maior de clusters, cada grupo será mais específico, o que facilita a criação de estratégias de marketing mais direcionadas, mas pode perder generalização e aplicabilidade prática.
Essas mudanças revelam novos perfis, como clientes com baixo rendimento e gastos elevados (talvez consumidores impulsivos), ou ajudar a distinguir melhor entre consumidores que possuem padrões de compra diferentes, mas rendas semelhantes.

### 3) Tentar outro dataset do Kaggle para exercitar a técnica com dados diferentes.

`Primeiras linhas do dataset:
  InvoiceNo StockCode                          Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6 2010-12-01 08:26:00       2.55     17850.0  United Kingdom
1    536365     71053                  WHITE METAL LANTERN         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8 2010-12-01 08:26:00       2.75     17850.0  United Kingdom
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom`

Informações gerais do dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 541909 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype
---  ------       --------------   -----
 0   InvoiceNo    541909 non-null  object        
 1   StockCode    541909 non-null  object
 2   Description  540455 non-null  object
 3   Quantity     541909 non-null  int64
 4   InvoiceDate  541909 non-null  datetime64[ns]
 5   UnitPrice    541909 non-null  float64
 6   CustomerID   406829 non-null  float64
 7   Country      541909 non-null  object
dtypes: datetime64[ns](1), float64(2), int64(1), object(4)
memory usage: 33.1+ MB

![Cluster de Clientes](https://github.com/user-attachments/assets/80417f90-6248-4817-be00-6819ccf20922)

Análise dos clusters:
          CustomerID    Frequency     TotalSpent  TotalQuantity
Cluster
0        15301.41028    83.146562    1601.825493     937.420468
1        16661.00000   711.750000  225721.652500  103007.250000
2        14649.00000  2395.133333   72682.466000   47137.600000

Analisando os Clusters, nós temos:

Cluster 1 (Roxo) - Denso e Compacto:

Este cluster contém a maioria dos pontos e é o mais concentrado, com baixa variação em termos de PCA 1 e PCA 2. 

Representa um grupo de clientes com compras frequentes de valor médio-baixo. Alta recorrência e fidelidade, além de um comportamento estável e previsível.

Cluster 2 (Amarelo) - Distribuição Média:

Este grupo apresenta maior dispersão, indicando que os clientes aqui são mais diferentes em termos de características. 

Eles têm comportamento variado, fazem compras esporádicas com valores variados. São moderados em termos de frequência e valor de compra. São clientes ocasionais e que gastam mais em períodos específicos.

Cluster 3 (Verde) - Disperso e Isolado:

Este é o grupo com menor número de clientes, localizado mais distante dos demais clusters.

Clientes únicos, com padrões de comportamento bastante diferentes do restante. Fazem compras de alto valor, mas com baixa frequência. São grandes investidores e clientes corporativos num geral.

### 4) Realizar testes sobre outros métodos de clustering (DBSCAN, Agglomerative) e os benefícios de diferentes abordagens, dependendo dos dados.

Primeiras linhas do dataset:
  InvoiceNo StockCode                          Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6 2010-12-01 08:26:00       2.55     17850.0  United Kingdom
1    536365     71053                  WHITE METAL LANTERN         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8 2010-12-01 08:26:00       2.75     17850.0  United Kingdom
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom

Informações gerais do dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 541909 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype
---  ------       --------------   -----
 0   InvoiceNo    541909 non-null  object
 1   StockCode    541909 non-null  object
 2   Description  540455 non-null  object
 3   Quantity     541909 non-null  int64
 4   InvoiceDate  541909 non-null  datetime64[ns]
 5   UnitPrice    541909 non-null  float64
 6   CustomerID   406829 non-null  float64
 7   Country      541909 non-null  object
dtypes: datetime64[ns](1), float64(2), int64(1), object(4)
memory usage: 33.1+ MB

![Cluster de Clientes](https://github.com/user-attachments/assets/fe745fb6-4de1-4612-96f5-b0d4cd3011d3)

Análise dos clusters:
                 CustomerID    Frequency     TotalSpent  TotalQuantity  DBSCAN_Cluster  Agglomerative_Cluster
KMeans_Cluster
0               15301.41028    83.146562    1601.825493     937.420468       -0.002778                    0.0
1               16661.00000   711.750000  225721.652500  103007.250000       -1.000000                    1.0
2               14649.00000  2395.133333   72682.466000   47137.600000       -1.000000                    1.2

![Cluster de Clientes DBSCAN](https://github.com/user-attachments/assets/d6639abf-4932-4103-8435-695ca45983a7)

                  CustomerID    Frequency    TotalSpent  TotalQuantity  KMeans_Cluster  Agglomerative_Cluster
DBSCAN_Cluster
-1              15123.129032  1447.290323  78832.552258   44539.161290        1.096774               0.709677
 0              15301.684003    81.963780   1501.648197     879.289064        0.000000               0.000000

 ![Cluster de Clientes Agglomerative](https://github.com/user-attachments/assets/13e6611b-4961-4990-a719-c231ce933964)

                          CustomerID    Frequency     TotalSpent  TotalQuantity  KMeans_Cluster  DBSCAN_Cluster
Agglomerative_Cluster
0                      15301.249306    83.752315    1604.268739     938.644213        0.000463       -0.003009
1                      15155.500000   917.571429  121233.271429   69102.428571        1.714286       -1.000000
2                      14899.000000  5807.000000   70925.287500   36358.750000        2.000000       -1.000000
