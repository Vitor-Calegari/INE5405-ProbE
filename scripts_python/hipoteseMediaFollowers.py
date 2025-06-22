import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t, ttest_ind
import seaborn as sns

def test_followers_partnered(twitchdata):
    
    twitchdata = twitchdata.dropna(subset=["Followers", "Partnered"])

    # Divide os dados em dois grupos, os que são parceiros e os que não são
    followers_partnered = twitchdata[twitchdata["Partnered"] == True]["Followers"]
    followers_not_partnered = twitchdata[twitchdata["Partnered"] == False]["Followers"]

    # Estatísticas descritivas
    media_parceiros = followers_partnered.mean()
    media_nao_parceiros = followers_not_partnered.mean()
    std_parceiros = followers_partnered.std()
    std_nao_parceiros = followers_not_partnered.std()
    n_parceiros = len(followers_partnered)
    n_nao_parceiros = len(followers_not_partnered)

    # Teste t para amostras independentes (unilateral)
    t_stat, p_bilateral = ttest_ind(followers_partnered, followers_not_partnered, equal_var=False)
    p_unilateral = p_bilateral / 2  

    print("===== Estatísticas Descritivas =====")
    print(f"Média de seguidores (parceiros): {media_parceiros:,.0f}")
    print(f"Desvio padrão (parceiros): {std_parceiros:,.0f}")
    print(f"Tamanho da amostra (parceiros): {n_parceiros}")

    print(f"Média de seguidores (não-parceiros): {media_nao_parceiros:,.0f}")
    print(f"Desvio padrão (não-parceiros): {std_nao_parceiros:,.0f}")
    print(f"Tamanho da amostra (não-parceiros): {n_nao_parceiros}")

    print("\n===== Teste t de Student =====")
    print(f"Estatística t: {t_stat:.3f}")
    print(f"P-valor unilateral: {p_unilateral:.5f}")

    if p_unilateral < 0.05:
        print("\n Resultado: Rejeitamos H₀. Streamers parceiros têm, em média, mais seguidores.")
    else:
        print("\n Resultado: Não há evidência suficiente para rejeitar H₀.")

    # Visualização do teste t
    diff_observada = media_parceiros - media_nao_parceiros

    # Erro padrão da diferença (variâncias diferentes)
    se_dif = np.sqrt((std_parceiros**2 / n_parceiros) + (std_nao_parceiros**2 / n_nao_parceiros))

    # Recalcula a estatística t para o gráfico
    t_stat = diff_observada / se_dif

    # Graus de liberdade
    df = ((std_parceiros**2 / n_parceiros + std_nao_parceiros**2 / n_nao_parceiros) ** 2) / (
        ((std_parceiros**2 / n_parceiros) ** 2) / (n_parceiros - 1) +
        ((std_nao_parceiros**2 / n_nao_parceiros) ** 2) / (n_nao_parceiros - 1)
    )

    # Valor crítico t (unilateral à direita, 5%)
    t_critico = t.ppf(0.95, df)

    # plotagem da distribuição t
    x = np.linspace(-4, 6, 500)
    y = t.pdf(x, df)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Distribuição t (H₀ verdadeira)', color='skyblue')
    plt.axvline(t_critico, color='black', linestyle=':', label=f'T crítico (5%) = {t_critico:.2f}')
    plt.fill_between(x, y, where=(x > t_critico), color='orange', alpha=0.3, label='Região crítica (α = 0.05)')

    # Ponto no eixo x para o valor t observado
    plt.scatter(t_stat, 0, color='red', label=f'Estatística t = {t_stat:.2f}', zorder=5, s=60)

    plt.title("Visualização do Teste t Unilateral (Parceria e Seguidores)")
    plt.xlabel("Valores da estatística t (diferença padronizada entre médias)")
    plt.ylabel("Densidade de probabilidade")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_boxplot_horizontal_followers(twitchdata):

    twitchdata = twitchdata.dropna(subset=["Followers", "Partnered"])

    
    twitchdata["Partnered_Label"] = twitchdata["Partnered"].map({True: "Parceiro", False: "Não-Parceiro"})

    plt.figure(figsize=(10, 4))
    sns.boxplot(y="Partnered_Label", x="Followers", data=twitchdata, palette="Set2")
    plt.title("Distribuição de Seguidores por Status de Parceria")
    plt.xlabel("Número de Seguidores")
    plt.ylabel("Status de Parceria")
    plt.xlim(0, 3_000_000)
    plt.grid(True, axis='x')
    plt.tight_layout()
    plt.show()

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    twitchdata = pd.read_csv("twitchdata-update.csv")
    print(twitchdata.columns)
    test_followers_partnered(twitchdata)
    plot_boxplot_horizontal_followers(twitchdata)
    


if __name__ == "__main__":
    main()
