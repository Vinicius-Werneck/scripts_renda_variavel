import datetime
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpf
import os

from PIL import Image
from matplotlib.lines import Line2D


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Especifique as datas de início e fim para os dados históricos
start_date = '2022-11-01'
end_date = '2023-06-30'

#symbol = ['USDBRL=X']

symbol = ['ABEV3.SA', 'AZUL4.SA', 'B3SA3.SA', 'BBAS3.SA', 'BBDC3.SA',
               'BBDC4.SA', 'BBSE3.SA', 'BEEF3.SA', 'GOLL4.SA', 'BRAP4.SA',
               'ROMI3.SA', 'BRFS3.SA', 'BRKM5.SA', 'GRND3.SA', 'SAPR11.SA',
               'CCRO3.SA', 'CIEL3.SA', 'CMIG4.SA', 'COGN3.SA', 'CPFE3.SA',
               'CPLE6.SA', 'CRFB3.SA', 'CSAN3.SA', 'CSNA3.SA', 'CVCB3.SA',
               'CYRE3.SA', 'ECOR3.SA', 'EGIE3.SA', 'ELET3.SA', 'ELET6.SA',
               'EMBR3.SA', 'ENBR3.SA', 'ENGI11.SA', 'EQTL3.SA', 'EZTC3.SA',
               'FLRY3.SA', 'GGBR4.SA', 'CAML3.SA', 'GOAU4.SA', 'GOLL4.SA',
               'HAPV3.SA', 'LEVE3.SA', 'HYPE3.SA', 'ARZZ3.SA', 'IRBR3.SA',
               'ITSA4.SA', 'ITUB4.SA', 'JBSS3.SA', 'JHSF3.SA', 'KLBN11.SA',
               'AMER3.SA', 'PSSA3.SA', 'LREN3.SA', 'MGLU3.SA', 'MRFG3.SA',
               'MRVE3.SA', 'MULT3.SA', 'USIM3.SA', 'OIBR3.SA', 'PETR4.SA',
               'PETR4.SA', 'PRIO3.SA', 'QUAL3.SA', 'RADL3.SA', 'RAIL3.SA',
               'RENT3.SA', 'SANB11.SA', 'SBSP3.SA', 'OIBR3.SA', 'SUZB3.SA',
               'TAEE11.SA', 'TIMS3.SA', 'TRPL4.SA', 'UGPA3.SA', 'USIM5.SA',
               'VALE3.SA', 'VIVT3.SA', 'SHOW3.SA', 'WEGE3.SA', 'YDUQ3.SA']


# Cria uma pasta para armazenar as imagens
folder = './Graficos_Acoes'
if not os.path.exists(folder):
    os.makedirs(folder)

# Gerar as imagens e salvá-las na pasta temporária
for symbols in symbol:

    # Use a função download do yfinance para obter os dados históricos da ação
    df = yf.download(symbols, start=start_date, end=end_date)
    df.index = pd.to_datetime(df.index)

    # Verifica se os dados foram baixados com sucesso
    if len(df) > 0:
        mc = mpf.make_marketcolors(
            up='tab:green', down='tab:red', edge='black', volume='in')
        s = mpf.make_mpf_style(marketcolors=mc)

        # personalizações, incluindo o formato de velas.
        fig, axlist = mpf.plot(df, type='candle', mav=(9, 21), style=s, ylabel='Preço', volume=True, title=symbols, returnfig=True)
        #fig, axlist = mpf.plot(df, type='candle', style=s, ylabel='Preço', title=symbols, returnfig=True)
        # Cria uma legenda customizada com os elementos desejados.
        legend_elements = [Line2D([0], [0], color='blue', label='MMA9'),
                           Line2D([0], [0], color='orange', label='MMA21')]
        # Adiciona a legenda ao gráfico.
        axlist[0].legend(handles=legend_elements, loc='upper left',
                         fontsize=10, facecolor='white', edgecolor='red')
        # Adiciona grid
        axlist[0].grid(color='gray', linestyle='--', linewidth=0.5, axis='x')
        axlist[0].grid(color='gray', linestyle='--', linewidth=0.5, axis='y')

        # Define o nome do arquivo de saída
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # filename = f"{symbols}_{now}.jpg"
        filename = f"{symbols}.jpg"
        fig.savefig(os.path.join(folder, filename))
        #plt.close(fig)

        # Salva a imagem em formato JPEG
        #plt.savefig(filename, dpi=300, bbox_inches='tight', format='jpg')
        print(f"Imagem salva como {filename}")
        print("Processo concluído com sucesso!")

        # Exiba o gráfico
        # plt.show()

    else:
        print(
            f"Erro: não foi possível baixar os dados para o símbolo {symbols}.")

print(f"Programa finalizado com sucesso!.")
