import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

def relationFollowersXPeakViewers(twitchdata):
    # Cria a figura
    plt.figure(figsize=(10, 6))

    # Plota o scatter + linha de regressão linear
    sns.regplot(
        data=twitchdata,
        x='Followers',
        y='Peak viewers',
        scatter_kws={'alpha': 0.5, 'color': 'mediumseagreen', 'edgecolors': 'black', 'linewidths': 0.3},
        line_kws={'color': 'darkblue', 'label': 'Tendência Linear',
        },
        ci = None
        )

    # Título e eixos
    plt.title('Followers × Peak Viewers', fontsize=14)
    plt.xlabel('Seguidores', fontsize=12)
    plt.ylabel('Pico de Visualizações', fontsize=12)

    # Formata o eixo Y
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(50000))
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

    # Limita os eixos (remove outliers)
    plt.xlim(0, twitchdata['Followers'].quantile(0.99))  # Limita até 99% dos seguidores
    plt.ylim(0, twitchdata['Peak viewers'].quantile(0.99))  # Limita até 99% do pico de visualizações

    # Formata o eixo X
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))


    # Formata o eixo Y

    # Exibe o gráfico
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():

    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    print(twitchdata.keys())
    relationFollowersXPeakViewers(twitchdata)

if (__name__ == '__main__'):
    main()