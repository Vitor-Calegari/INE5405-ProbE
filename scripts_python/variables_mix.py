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

    plt.show()


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
    
    # Printa um boxplot que relaciona as variáveis de viewers médios com a linguagem transmitida
    # A variável booleana inserida como segundo argumento define uma restrição de eixo y, 
    # para melhorar a visualização, mesmo que exclua algum outliers 
    relationAvgViewersXLanguage(twitchdata, True)

    # A função plota um gráfico de dispersão entre tempo de transmissão (em horas) e seguidores ganhos,
    # usando uma linha de tendência linear para destacar a relação entre as variáveis.
    # Além disso, formata os eixos para facilitar a leitura e agrupa os seguidores em intervalos de 100 mil.
    relationStreamTimeXFollowersGained(twitchdata)

    # Printa a relação entre número de seguidores e pico de visualizações ao vivo
    # Utiliza um gráfico de dispersão com linha de regressão linear para identificar tendências,
    # formata ambos os eixos com notação em milhares (k) e limita os valores até o percentil 99% para evitar distorções por outliers.
    relationFollowersXPeakViewers(twitchdata)


    # Printa um boxplot que relaciona a quantidade de seguidores com a linguagem transmitida.
    # A variável booleana 'restricao' define uma limitação no eixo Y, para melhorar a visualização,
    # mesmo que isso exclua valores extremos (outliers).
    relationFollowersXLanguage(twitchdata, True)

if (__name__ == '__main__'):
    main()

