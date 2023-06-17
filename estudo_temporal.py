import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import yfinance as yf
import seaborn as sns


#Aquisição dos dados de ações
start_date = '2020-01-01'
end_date = '2023-06-01'

symbol = '^BVSP'
ticker = yf.Ticker(symbol)

#df = ticket.history(period='1y',interval='1d')
df = ticker.history(interval='1d',start=start_date,end=end_date)

#Decomposição de uma série temporal
decomposicao = seasonal_decompose(df[['Close']], model='additive', period=30, extrapolate_trend=30)
sinal_total = decomposicao.seasonal + decomposicao.resid + decomposicao.trend
sinal_tend = decomposicao.trend

#Calcular a média
media_9 = df['Close'].rolling(9).mean()
media_21 = df['Close'].rolling(21).mean()
media_200 = df['Close'].rolling(200).mean()

# Extraçao de features
df.reset_index(inplace=True) #coloca novamente o indice na tabela

# calculo da Rentabilidade
# Rentabilidade = [(preço atual/preço anterior) * 100] - 100
# Faz a função de extração de features
def features_extraction(df_):
    #criar features para cada período
    df_['year'] = df_['Date'].dt.year
    df_['month'] = df_['Date'].dt.month
    df_['day'] = df_['Date'].dt.day
    df_['rentabilidade'] = df_['Close'] / df_['Close'].shift() * 100 -100

features_extraction(df)

#Gera figuras

fig, axs = plt.subplots(2, 1, figsize=(10,5))
axs[0].plot(decomposicao.seasonal,'black')
axs[0].set_title('Sazonalidade do ativo')
axs[0].set_xlabel('Escala de tempo em anos.')

axs[1].plot(decomposicao.trend,'red')
axs[1].set_title('Linha de Tendência')
axs[1].set_xlabel('Escala de tempo em anos.')
axs[1].set_ylabel('Valor')

#plt.plot(media_9,'red')
#plt.plot(media_21,'yellow')
#plt.plot(media_200,'green')
plt.tight_layout()
plt.show()