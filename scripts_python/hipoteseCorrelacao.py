import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


def test_correlation_followers_viewers(twitchdata):
    
    twitchdata = twitchdata.dropna(subset=["Followers", "Average viewers"])

    # Calcula a correlação de Pearson
    corr, p_val = pearsonr(twitchdata["Followers"], twitchdata["Average viewers"])

    print("===== Estatísticas de Correlação =====")
    print(f"Coeficiente de correlação de Pearson: {corr:.3f}")
    print(f"P-valor (bilateral): {p_val}")

    print("\n===== Teste de Hipótese =====")
    if p_val < 0.05:
        print("\n Resultado: Rejeitamos H₀. Existe correlação significativa entre seguidores e espectadores.")
    else:
        print("\n Resultado: Não há evidência suficiente para rejeitar H₀.")


def plot_scatter_followers_viewers(twitchdata):
    twitchdata = twitchdata.dropna(subset=["Followers", "Average viewers"])

    plt.figure(figsize=(10, 6))
    sns.regplot(
        x="Followers",
        y="Average viewers",
        data=twitchdata,
        scatter_kws={'alpha': 0.3},
        line_kws={'color': 'red'},
        ci=None  
)

    plt.title("Relação entre Seguidores e Espectadores Médios")
    plt.xlabel("Número de Seguidores")
    plt.ylabel("Média de Espectadores")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    twitchdata = pd.read_csv("twitchdata-update.csv")
    print(twitchdata.columns)
    test_correlation_followers_viewers(twitchdata)
    plot_scatter_followers_viewers(twitchdata)


if __name__ == "__main__":
    main()
