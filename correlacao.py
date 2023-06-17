import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns


#Aquisição dos dados de ações
start_date = '2015-01-01'
end_date = '2023-06-01'

#correlações de séries temporais
tickers = ['SAPR11.SA','ITUB4.SA','PETR4.SA','SUZB3.SA','^BVSP','USDBRL=X']

dfs = []

for t in tickers:
    print('Carregando ticker {}...'.format(t))
    ticker = yf.Ticker(t)
    aux = ticker.history(interval='1d', start=start_date, end=end_date)
    aux.reset_index(inplace=True)
    aux['ticker'] = t
    dfs.append(aux)

correlacao = pd.DataFrame()
for d in dfs:
    correlacao[d['ticker'].iloc[0]] = d['Close']

#Gera figura
fig, ax = plt.subplots(figsize=(10,5))
ax = sns.heatmap(correlacao.corr(),annot=True)
plt.tight_layout()
plt.show()