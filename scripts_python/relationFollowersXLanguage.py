import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.ticker as ticker
import seaborn as sns


def relationFollowersXLanguage(twitchdata):
    # Pega os 5 idiomas mais frequentes
    top_langs = twitchdata['Language'].value_counts().nlargest(6).index
    subset = twitchdata[twitchdata['Language'].isin(top_langs)]

    # Organiza os dados para o boxplot
    data_to_plot = [subset[subset['Language'] == lang]['Followers'] for lang in top_langs]

    # Subplots: 2 linhas, 1 coluna, com tamanho reduzido
    fig, axes = plt.subplots(2, 1, figsize=(8, 6))

    # Gráfico 1: sem restrição
    axes[0].boxplot(data_to_plot, labels=top_langs, patch_artist=True)
    axes[0].set_title('Seguidores por Idioma (Sem Restrição)', fontsize=12)
    axes[0].set_ylabel('Seguidores', fontsize=10)
    axes[0].set_xlabel('Idioma', fontsize=10)
    axes[0].grid(True)
    axes[0].yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{x / 1_000_000:.1f}M'))

    # Gráfico 2: com restrição
    axes[1].boxplot(data_to_plot, labels=top_langs, patch_artist=True)
    axes[1].set_title('Seguidores por Idioma (Com Restrição até 2M)', fontsize=12)
    axes[1].set_ylabel('Seguidores', fontsize=10)
    axes[1].set_xlabel('Idioma', fontsize=10)
    axes[1].grid(True)
    axes[1].set_ylim(0, 2_000_000)
    axes[1].yaxis.set_major_locator(ticker.MultipleLocator(500_000))
    axes[1].yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{x / 1_000_000:.1f}M'))

    plt.tight_layout()

    plt.savefig("/Users/antonio/INE5405-ProbE/scripts_python/graficos", dpi=300)  # dpi=300 deixa em alta resolução

    
    plt.show()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    twitchdata = pd.read_csv('twitchdata-update.csv')
    print(twitchdata.keys())
    relationFollowersXLanguage(twitchdata)

if __name__ == '__main__':
    main()
