import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


def relationAvgViewersXLanguage(twitchdata, restricao):
    # Pega os 5 idiomas mais frequentes
    top_langs = twitchdata['Language'].value_counts().nlargest(6).index
    subset = twitchdata[twitchdata['Language'].isin(top_langs)]

    # Organiza os dados para o boxplot
    data_to_plot = [subset[subset['Language'] == lang]['Average viewers'] for lang in top_langs]

    plt.figure(figsize=(10, 6))
    plt.boxplot(data_to_plot, labels=top_langs, patch_artist=True)
    plt.title('Espectadores Médios por Idioma (Top 5 Idiomas)')
    plt.ylabel('Espectadores Médios')
    plt.xlabel('Idioma')
    plt.grid(True)
    
    if restricao:
        plt.ylim(0, 20000)

    plt.show()


def main():

    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    print(twitchdata.keys())
    restricao = False
    relationAvgViewersXLanguage(twitchdata, restricao)

if (__name__ == '__main__'):
    main()