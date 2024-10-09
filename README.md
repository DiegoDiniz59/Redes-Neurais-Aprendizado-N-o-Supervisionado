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




