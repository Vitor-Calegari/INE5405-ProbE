import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

def relationFollowersXPeakViewers(twitchdata):
    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=twitchdata,
        x='Followers',
        y='Peak viewers',
        alpha=0.5,
        color='mediumseagreen',
        edgecolor='black',
        linewidth=0.3
    )

    plt.title('Followers × Peak Viewers', fontsize=14)
    plt.xlabel('Seguidores', fontsize=12)
    plt.ylabel('Pico de Visualizações', fontsize=12)

    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(50000))
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

    plt.xlim(0, twitchdata['Followers'].quantile(0.99))
    plt.ylim(0, twitchdata['Peak viewers'].quantile(0.99))

    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

    plt.grid(True, linestyle='--', alpha=0.6)
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