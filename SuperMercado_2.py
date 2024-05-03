import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_csv('supermarket_sales.csv')

# Converter as colunas de data e hora para o tipo datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')


##########################
# Análises por Filial e Cidade
##########################

# Agrupar por filial e cidade, somando as vendas totais
filiais = df.groupby(['Branch', 'City']).agg({'Total': 'sum'}).reset_index()
print("Vendas totais por filial e cidade:\n", filiais)

# Calcular a avaliação média por linha de produto
avaliacao_media_produto = df.groupby('Product line')['Rating'].mean().reset_index()
print("\nAvaliação média por linha de produto:\n", avaliacao_media_produto)

# Distribuição por linha de produto
produtos = df['Product line'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(produtos, labels=produtos.index, autopct='%1.1f%%')
plt.title('Distribuição por Linha de Produto')
plt.show()

# Preço médio unitário por linha de produto
preco_medio_unitario = df.groupby('Product line')['Unit price'].mean().reset_index()
plt.figure(figsize=(8, 6))
plt.pie(preco_medio_unitario['Unit price'], labels=preco_medio_unitario['Product line'], autopct='%1.1f%%')
plt.title('Preço Médio Unitário por Linha de Produto')
plt.show()

# Quantidade total vendida por linha de produto
quantidade_produtos = df.groupby('Product line')['Quantity'].mean().reset_index()
plt.figure(figsize=(8, 6))
plt.pie(quantidade_produtos['Quantity'], labels=quantidade_produtos['Product line'], autopct='%1.1f%%')
plt.title('Quantidade Total Vendida por Linha de Produto')
plt.show()


##########################
# Análise por Gênero
##########################

# Quantidade total vendida por gênero
quantidade_generos = df.groupby('Gender')['Quantity'].sum().reset_index()
plt.figure(figsize=(8, 6))
plt.bar(quantidade_generos['Gender'], quantidade_generos['Quantity'])
plt.title('Quantidade Total Vendida por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade Vendida')
plt.show()

# Número de vendas por gênero e linha de produtos
gender_product_line = df.groupby(['Gender', 'Product line']).size().reset_index(name='Count')
plt.figure(figsize=(8, 6))
plt.pie(gender_product_line['Count'], labels=gender_product_line['Product line'], autopct='%1.1f%%', startangle=140)
plt.title('Número de Vendas por Gênero e Linha de Produtos')
plt.show()

# Vendas totais por gênero
gender_total = df.groupby('Gender')['Total'].sum().reset_index()
plt.figure(figsize=(8, 6))
plt.pie(gender_total['Total'], labels=gender_total['Gender'], autopct='%1.1f%%', startangle=140)
plt.title('Vendas Totais por Gênero')
plt.show()


##########################
# Análise por Tipo de Cliente e Forma de Pagamento
##########################

# Vendas totais por tipo de cliente e forma de pagamento
customer_payment = df.groupby(['Customer type', 'Payment'])['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(x=customer_payment['Payment'], height=customer_payment['Total'], color='skyblue')
plt.title('Vendas Totais por Tipo de Cliente e Forma de Pagamento')
plt.xlabel('Forma de Pagamento')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.show()

# Tabela de contingência para tipo de pagamento por filial
payment_branch = pd.crosstab(df['Payment'], df['Branch'])
print("\nTabela de contingência para tipo de pagamento por filial:\n", payment_branch)


##########################
# Análise Temporal
##########################

# Vendas totais ao longo do tempo
date_sales = df.groupby('Date')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(date_sales['Date'], date_sales['Total'])
plt.xlabel('Data')
plt.ylabel('Total de Vendas')
plt.title('Vendas Totais ao Longo do Tempo')
plt.show()


##########################
# Análise por Filial
##########################

# Total de vendas por filial
branch_total_sales = df.groupby('Branch')['Total'].sum().reset_index()
plt.figure(figsize=(8, 8))
plt.pie(branch_total_sales['Total'], labels=branch_total_sales['Branch'], autopct='%1.1f%%')
plt.title('Total de Vendas por Filial')
plt.show()
