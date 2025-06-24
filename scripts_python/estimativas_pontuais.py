import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
import os
from scipy import stats

# Muda o diretório atual para o do script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Carregar dados
df = pd.read_csv("twitchdata-update.csv")

discretas = ["Followers", "Watch time(Minutes)", "Stream time(minutes)", "Peak viewers", "Average viewers", "Followers gained", "Views gained"]
nominais = ["Partnered", "Mature", "Language"]

# Criar janela principal
root = tk.Tk()
root.title("Estatísticas Amostrais")

# Notebook com abas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Função para criar uma aba com resultados
def criar_aba(titulo, tabela_df):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=titulo)

    label = ttk.Label(frame, text=f"Estatísticas: {titulo}", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    tree = ttk.Treeview(frame, columns=list(tabela_df.columns), show="headings", style="Custom.Treeview")

    for col in tabela_df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)

    for index, row in tabela_df.iterrows():
        tag = 'evenrow' if index % 2 == 0 else 'oddrow'
        tree.insert("", "end", values=list(row), tags=(tag,))

    tree.tag_configure('evenrow', background='#FFFFFF')
    tree.tag_configure('oddrow', background='#F0F0F0')

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tree.pack(expand=True, fill="both", padx=10, pady=10)

style = ttk.Style()
style.configure("Custom.Treeview", rowheight=25)
style.configure("Custom.Treeview.Heading", font=("Helvetica", 11, "bold"))
style.map("Custom.Treeview", background=[('selected', '#ececec')])

# Processar variáveis discretas (amostragem aleatória)
for coluna in discretas:
    amostra = df[coluna].dropna().sample(n=30, random_state=42)

    media_amostral = amostra.mean()
    desvio_amostral = amostra.std(ddof=1)
    n = len(amostra)

    # Intervalo de confiança de 95% (t-Student)
    t_critico = stats.t.ppf(1 - 0.025, df=n - 1)
    margem_erro = t_critico * (desvio_amostral / np.sqrt(n))
    ic_inferior = media_amostral - margem_erro
    ic_superior = media_amostral + margem_erro

    tabela = pd.DataFrame({
        "Estatística": ["Média Amostral", "Desvio Padrão", "IC 95% Inferior", "IC 95% Superior"],
        "Valor": [f"{media_amostral:.2f}", f"{desvio_amostral:.2f}", f"{ic_inferior:.2f}", f"{ic_superior:.2f}"]
    })

    criar_aba(coluna, tabela)

# Processar variáveis nominais (amostragem aleatória para proporção)
for coluna in nominais:
    amostra = df[coluna].dropna().sample(n=30, random_state=42)

    proporcao = amostra.value_counts(normalize=True)
    total_amostra = len(amostra)

    resultados = []
    for categoria, prop in proporcao.items():
        p_hat = prop
        z = 1.96  # 95% de confiança
        margem_erro = z * np.sqrt((p_hat * (1 - p_hat)) / total_amostra)
        ic_inferior = p_hat - margem_erro
        ic_superior = p_hat + margem_erro

        resultados.append({
            coluna: categoria,
            "Proporção (%)": f"{p_hat * 100:.2f}",
            "IC 95% Inferior (%)": f"{max(ic_inferior, 0) * 100:.2f}",
            "IC 95% Superior (%)": f"{min(ic_superior, 1) * 100:.2f}"
        })

    tabela = pd.DataFrame(resultados)
    criar_aba(coluna, tabela)

root.mainloop()
