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

if (__name__ == '__main__'):
    main()