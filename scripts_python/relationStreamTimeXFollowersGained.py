import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

def relationStreamTimeXFollowersGained(twitchdata):

    # Converte o tempo de transmissão de minutos para horas
    twitchdata['Stream time(hours)'] = twitchdata['Stream time(minutes)'] / 60

    # Filtra colunas relevantes
    stream_hours = twitchdata['Stream time(hours)']
    followers_gained = twitchdata['Followers gained']

    plt.figure(figsize=(10, 6))
    plt.scatter(stream_hours, followers_gained, alpha=0.5, color='mediumseagreen', edgecolors='black', linewidths=0.3)

    plt.title('Stream Time (horas) × Followers Gained', fontsize=14)
    plt.xlabel('Tempo de Transmissão (horas)', fontsize=12)
    plt.ylabel('Seguidores Ganhos', fontsize=12)

    # Formata o eixo Y em intervalos de 100.000
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(200_000))
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x/1000)}k'))

    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()

    # Limita os eixos para ignorar outliers extremos
    plt.xlim(0, stream_hours.quantile(0.99))
    plt.ylim(0, followers_gained.quantile(0.99))


    plt.savefig("/Users/antonio/INE5405-ProbE/scripts_python/graficos", dpi=300)  # dpi=300 deixa em alta resolução

    

    plt.show()



def main():

    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    print(twitchdata.keys())
    relationStreamTimeXFollowersGained(twitchdata)

if (__name__ == '__main__'):
    main()