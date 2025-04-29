import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


def relationFollowersXLanguage(twitchdata, restricao):

    # Pega os 5 idiomas mais frequentes
    top_langs = twitchdata['Language'].value_counts().nlargest(6).index
    subset = twitchdata[twitchdata['Language'].isin(top_langs)]

    # Organiza os dados para o boxplot
    data_to_plot = [subset[subset['Language'] == lang]['Followers'] for lang in top_langs]

    # Cria o gráfico
    plt.figure(figsize=(10, 6))
    plt.boxplot(data_to_plot, labels=top_langs, patch_artist=True)
    plt.title('Seguidores por Idioma (Top 5 Idiomas)', fontsize=14)
    plt.ylabel('Seguidores', fontsize=12)
    plt.xlabel('Idioma', fontsize=12)
    plt.grid(True)

    # Restringe o eixo Y para visualização mais clara (opcional)
    if restricao:
        plt.ylim(0, 2_000_000)
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(500_000))

    # Formata o eixo Y com casa decimal (ex: 0.5M)
    plt.gca().yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{x / 1_000_000:.1f}M' if x >= 1_000_000 else f'{x / 1_000_000:.1f}M')
    )

    plt.tight_layout()
    plt.show()


def main():

    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    print(twitchdata.keys())
    restricao = False
    relationFollowersXLanguage(twitchdata, restricao)

if (__name__ == '__main__'):
    main()