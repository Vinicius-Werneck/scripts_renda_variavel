import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


#Aquisição dos dados de ações
start_date = '2015-01-01'
end_date = '2023-06-01'

symbol = 'PETR4.SA'
ticket = yf.Ticker(symbol)

df = ticket.history(interval='1d',start=start_date,end=end_date)

# Extraçao de features
# calculo da Rentabilidade
# Rentabilidade = [(preço atual/preço anterior) * 100] - 100

# Extraçao de features
df.reset_index(inplace=True) #coloca novamente o indice na tabela

# Faz a função de extração de features (características ou atributos que descrevem um objeto ou conjunto de dados)
def features_extraction(df_):
    #criar features para cada período
    df_['year'] = df_['Date'].dt.year
    df_['month'] = df_['Date'].dt.month
    df_['day'] = df_['Date'].dt.day
    df_['rentabilidade'] = df_['Close'] / df_['Close'].shift() * 100 -100

features_extraction(df)

# Estudo de caso: Qual o melhor mês para investir?
r = df.groupby('month').agg({'rentabilidade':'sum'})

# Criar o gráfico de barras
x = r.index  # Índice representa os meses
y = r['rentabilidade']  # Valores da rentabilidade
plt.bar(x, y)

# Adicionar a linha da rentabilidade
plt.plot(x, y, color='red', linewidth=2, marker='o')

# Adicionar rótulos e título
plt.xlabel(f'Meses entre {start_date} à {end_date}')
plt.ylabel('Valor (R$)')
plt.title(f'Rentabilidade Média Mensal {symbol}')

# Mostrar o gráfico
plt.show()

