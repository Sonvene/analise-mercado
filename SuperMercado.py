import pandas as pd
import plotly.express as px

# Carregar o conjunto de dados
df = pd.read_csv('supermarket_sales.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M')

##########################
# Análises por Filial e Cidade
##########################

# Total de vendas por filial e cidade
branch_city = df.groupby(['Branch', 'City']).agg({'Total': 'sum'}).reset_index()
print("Total de vendas por filial e cidade:\n", branch_city)

##########################
# Análise por Linha de Produto
##########################

# Avaliação média por linha de produto
product_line_rating = df.groupby('Product line')['Rating'].mean().reset_index()
print("\nAvaliação média por linha de produto:\n", product_line_rating)

# Gráfico de barra da avaliação por linha de produto
fig = px.bar(product_line_rating, x='Product line', y='Rating', title='Avaliação Média por Linha de Produto')
fig.show()

# Preço médio unitário por linha de produto
product_line_unit_price = df.groupby('Product line')['Unit price'].mean().reset_index()
produtos = px.bar(product_line_unit_price, x='Product line', y='Unit price', title='Preço Médio Unitário por Linha de Produto')
produtos.show()

# Quantidade total vendida por linha de produto
product_line_quantity = df.groupby('Product line')['Quantity'].sum().reset_index()
quantidade_produto = px.pie(product_line_quantity, values='Quantity', names='Product line', title='Quantidade Total Vendida por Linha de Produto', color_discrete_sequence=px.colors.sequential.RdBu)
quantidade_produto.show()

##########################
# Análise por Gênero
##########################

# Quantidade total vendida por gênero
gender_quantity = df.groupby('Gender')['Quantity'].sum().reset_index()
gender = px.bar(gender_quantity, x='Gender', y='Quantity', title='Quantidade Total Vendida por Gênero')
gender.show()

# Número de vendas por gênero e linha de produtos
gender_product_line = df.groupby(['Gender', 'Product line']).size().reset_index(name='Count')
gender = px.pie(gender_product_line, values='Count', names='Product line', hover_data=['Gender'], title='Número de Vendas por Gênero e Linha de Produtos', color_discrete_sequence=px.colors.sequential.RdBu)
gender.show()

# Vendas totais por gênero
gender_total = df.groupby('Gender')['Total'].sum().reset_index()
gen = px.pie(gender_total, names='Gender', values='Total', color_discrete_sequence=px.colors.sequential.RdBu, title='Vendas Totais por Gênero')
gen.show()

##########################
# Análise por Tipo de Cliente e Forma de Pagamento
##########################

# Total de vendas por tipo de cliente e forma de pagamento
customer_payment = df.groupby(['Customer type', 'Payment'])['Total'].sum().reset_index()
pagamento = px.bar(customer_payment, x='Customer type', y='Payment', color='Total', title='Total de Vendas por Tipo de Cliente e Forma de Pagamento')
pagamento.show()

# Tabela de contingência para tipo de pagamento por filial
payment_branch = pd.crosstab(df['Payment'], df['Branch'])
print("\nTabela de contingência para tipo de pagamento por filial:\n", payment_branch)

##########################
# Análise Temporal
##########################

# Vendas totais ao longo do tempo
date_sales = df.groupby('Date')['Total'].sum().reset_index()
tempo_vendas = px.line(date_sales, x='Date', y='Total', title='Vendas Totais ao Longo do Tempo')
tempo_vendas.show()

##########################
# Análise por Filial
##########################

# Total de vendas por filial
branch_total_sales = df.groupby('Branch')['Total'].sum().reset_index()
total_sales = px.pie(branch_total_sales, names='Branch', values='Total', title='Vendas Totais por Filial', color_discrete_sequence=px.colors.sequential.RdBu)
total_sales.show()
