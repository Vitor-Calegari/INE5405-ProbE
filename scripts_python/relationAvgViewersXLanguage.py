import matplotlib.pyplot as plt
import pandas as pd
import os

def relationAvgViewersXLanguage(twitchdata):
    # Pega os 5 idiomas mais frequentes
    top_langs = twitchdata['Language'].value_counts().nlargest(6).index
    subset = twitchdata[twitchdata['Language'].isin(top_langs)]

    # Organiza os dados para o boxplot
    data_to_plot = [subset[subset['Language'] == lang]['Average viewers'] for lang in top_langs]

    fig, axes = plt.subplots(2, 1, figsize=(8, 6))  # <--- Aqui está a mudança

    # Gráfico sem restrição
    axes[0].boxplot(data_to_plot, labels=top_langs, patch_artist=True)
    axes[0].set_title('Espectadores Médios por Idioma (Sem Restrição)')
    axes[0].set_ylabel('Espectadores Médios')
    axes[0].set_xlabel('Idioma')
    axes[0].grid(True)

    # Gráfico com restrição de y
    axes[1].boxplot(data_to_plot, labels=top_langs, patch_artist=True)
    axes[1].set_title('Espectadores Médios por Idioma (Com Restrição até 20000)')
    axes[1].set_ylabel('Espectadores Médios')
    axes[1].set_xlabel('Idioma')
    axes[1].grid(True)
    axes[1].set_ylim(0, 20000)

    plt.tight_layout()
    plt.show()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    twitchdata = pd.read_csv('twitchdata-update.csv')
    print(twitchdata.keys())
    relationAvgViewersXLanguage(twitchdata)

if __name__ == '__main__':
    main()
