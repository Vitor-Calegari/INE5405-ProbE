import os
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

SIGNIFICANCE = 0.05

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    languages = twitchdata['Language']
    
    spanish_count = (languages == 'Spanish').sum()
    portuguese_count = (languages == 'Portuguese').sum()
    n_total = len(languages)
    
    # Valores para o teste
    count = [spanish_count, portuguese_count]
    nobs = [n_total, n_total]
    # Teste de proporções com hipótese unilateral (português > espanhol)
    stat, pval = proportions_ztest(count, nobs, alternative='larger')

    print("===== Teste de Proporção: Português vs Espanhol =====")
    print(f"Português: {portuguese_count} transmissões")
    print(f"Espanhol: {spanish_count} transmissões")
    print(f"Estatística Z: {stat:.4f}")
    print(f"P-valor: {pval:.4f}")

    # H0: Proporção Portugues <= Proporção Espanhol
    # H1: Proporção Portugues >  Proporção Espanhol
    if pval < SIGNIFICANCE:
        print("Resultado: Rejeitamos H₀. A proporção de transmissões em português é maior que em espanhol.")
    else:
        print("Resultado: Não há evidência suficiente para afirmar que a proporção de transmissões com língua principal português é maior do que com a língua principal espanhol.")

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm

    # Estatística Z do teste
    z_obs = 0.6372
    p_val = 0.262

    # Intervalo do eixo x
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)

    # Plot da curva normal padrão
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Distribuição Normal Padrão", color='black')

    # Área do p-valor (região à direita de z_obs)
    x_fill = np.linspace(z_obs, 4, 500)
    plt.fill_between(x_fill, norm.pdf(x_fill), color='red', alpha=0.4, label=f"p-valor ≈ {p_val:.3f}")

    # Linha vertical no z observado
    plt.axvline(z_obs, color='red', linestyle='--', label=f"Z observado = {z_obs:.3f}")

    # Linha vertical no valor crítico para α = 0.05 (z crítico unilateral)
    z_crit = norm.ppf(1 - 0.05)
    plt.axvline(z_crit, color='blue', linestyle='--', label=f"Z crítico (α=0.05) ≈ {z_crit:.2f}")

    # Estética do gráfico
    plt.title("Distribuição Normal Padrão")
    plt.xlabel("Z")
    plt.ylabel("Densidade de Probabilidade")
    plt.legend()
    
    plt.grid(True)
    plt.show()

if (__name__ == '__main__'):
    main()