# Análise de Ações com Python

Este repositório contém scripts em Python para análise de dados financeiros, incluindo coleta de dados de ações, visualização de gráficos, correlação de séries temporais e decomposição de tendências.

## Funcionalidades
- **Coleta de Dados**: Usa a API do Yahoo Finance (`yfinance`) para baixar históricos de preços de ações.
- **Geração de Gráficos**: Utiliza `matplotlib` e `mplfinance` para gerar gráficos de velas e médias móveis.
- **Análise de Correlação**: Cria um heatmap de correlação entre ativos financeiros usando `seaborn`.
- **Decomposição de Séries Temporais**: Separa componentes sazonais, de tendência e ruído dos preços de fechamento do Ibovespa (`^BVSP`).
- **Estudo de Rentabilidade**: Analisa a rentabilidade média mensal das ações.

## Instalação
Antes de executar os scripts, instale as dependências necessárias:
```sh
pip install pandas matplotlib yfinance seaborn statsmodels mplfinance
```

## Uso
### 1. Geração de Gráficos de Ações
O script **graficos_acoes.py** baixa dados históricos de diversas ações da B3 e gera gráficos de velas.
```sh
python graficos_acoes.py
```
Os gráficos serão salvos na pasta `./Graficos_Acoes`.

### 2. Análise de Correlação
O script **correlacao.py** gera uma matriz de correlação entre diferentes ativos e exibe um heatmap.
```sh
python correlacao.py
```

### 3. Decomposição de Tendências
O script **decomposicao.py** realiza a decomposição da série temporal do Ibovespa e plota os componentes.
```sh
python decomposicao.py
```

### 4. Estudo de Rentabilidade Mensal
O script **rentabilidade.py** analisa a rentabilidade mensal de `PETR4.SA` e gera um gráfico de barras.
```sh
python rentabilidade.py
```

## Estrutura do Repositório
```
/
├── Graficos_Acoes/      # Pasta onde os gráficos são salvos
├── graficos_acoes.py    # Gera gráficos de velas
├── correlacao.py        # Analisa a correlação entre ativos
├── decomposicao.py      # Realiza decomposição de tendências
├── rentabilidade.py     # Analisa a rentabilidade mensal
├── README.md            # Este arquivo
```

## Contribuição
Sinta-se à vontade para abrir *issues* ou enviar *pull requests* para melhorias.


