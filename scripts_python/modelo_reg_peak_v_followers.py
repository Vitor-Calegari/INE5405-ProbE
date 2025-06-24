import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


SIGNIFICANCE = 0.05

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    # Define as variáveis
    X = twitchdata["Followers"]
    y = twitchdata["Peak viewers"]

    # Adiciona o intercepto (constante β₀)
    X = sm.add_constant(X)

    # Cria e ajusta o modelo de regressão linear
    modelo = sm.OLS(y, X).fit()

    # Exibe o resumo estatístico
    print(modelo.summary())
    
    beta_1 = modelo.params["Followers"]
    p_value = modelo.pvalues["Followers"]
    
    print("\n===== Teste de Hipótese para β₁ (Followers) =====")
    print("H₀: β₁ = 0 (seguidores não influenciam a audiência mais alta já alcançada)")
    print("H₁: β₁ ≠ 0 (seguidores influenciam a audiência mais alta já alcançada)")
    print(f"Coeficiente β₁: {beta_1:.4f}")
    print(f"Valor-p: {p_value}")

    if p_value < SIGNIFICANCE:
        print(f"Resultado: Rejeitamos H₀ ao nível de significância de {SIGNIFICANCE:.0%}.")
        print("Conclusão: Existe evidência estatística de que o número de seguidores influencia o pico máximo de espectadores.")
    else:
        print(f"Resultado: Não rejeitamos H₀ ao nível de significância de {SIGNIFICANCE:.0%}.")
        print("Conclusão: Não há evidência estatística suficiente de que seguidores influencia o pico máximo de espectadores.")
    
    # Plota a dispersão com a linha de regressão
    plt.figure(figsize=(10, 6))
    sns.regplot(x="Followers", y="Peak viewers", data=twitchdata,
                line_kws={"color": "red"}, scatter_kws={"alpha": 0.3})
    plt.title("Modelo de regressão linear: Pico de espectadores em relação ao Número de Seguidores")
    plt.ylabel("Peak viewers")
    plt.xlabel("Followers")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Plota segundo gráfico com limite no eixo x
    plt.figure(figsize=(10, 6))
    sns.regplot(x="Followers", y="Peak viewers", data=twitchdata,
                line_kws={"color": "red"}, scatter_kws={"alpha": 0.3})
    plt.title("Modelo de regressão linear: Pico de espectadores em relação ao Número de Seguidores (até 4e6 seguidores)")
    plt.ylabel("Peak viewers")
    plt.xlabel("Followers")
    plt.xlim(0, 4e6)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if (__name__ == '__main__'):
    main()