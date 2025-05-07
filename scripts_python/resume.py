import pandas as pd
import tkinter as tk
from tkinter import ttk

# Colunas a analisar
descritivas = [
    "Followers", "Watch time(Minutes)", "Stream time(minutes)",
    "Average viewers"
]

qualitativas = ["Partnered", "Mature", "Language"]

# Carregar dados
df = pd.read_csv("twitchdata-update.csv")

# Definir variáveis numéricas e qualitativas
numericas = [col for col in descritivas if pd.api.types.is_numeric_dtype(df[col])]
categóricas = qualitativas

# Criar janela principal
root = tk.Tk()
root.title("Estatísticas Descritivas")

# Estilo
style = ttk.Style()
style.configure("Custom.Treeview", rowheight=25)
style.configure("Custom.Treeview.Heading", font=("Helvetica", 12, "bold"))
style.configure("Custom.Treeview", font=("Helvetica", 12))

# Notebook (abas)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

def criar_aba_estatisticas(titulo, df_desc):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=titulo)

    # Label
    label = ttk.Label(frame, text=f"Estatísticas {titulo}", font=("Helvetica", 16, "bold"))
    label.pack(pady=10)

    # Treeview
    tree = ttk.Treeview(frame, columns=list(df_desc.columns), show="headings", style="Custom.Treeview")

    # Configurar colunas
    for col in df_desc.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)

    # Inserir dados com zebra striping
    for i, row in df_desc.iterrows():
        tag = 'evenrow' if i % 2 == 0 else 'oddrow'
        tree.insert("", "end", values=list(row), tags=(tag,))

    tree.tag_configure('evenrow', background='#FFFFFF')
    tree.tag_configure('oddrow', background='#F0F0F0')

    # Scrollbar
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tree.pack(expand=True, fill="both", padx=10, pady=10)

# Estatísticas numéricas
df_numericas = pd.DataFrame()
for col in numericas:
    descr = df[col].describe()
    
    # Calcular a moda e adicionar à tabela
    moda = df[col].mode()[0] if not df[col].mode().empty else None
    descr["moda"] = moda

    # Remover apenas 'count', manter 'std'
    descr = descr.drop(["count"])

    descr.name = col
    df_numericas[col] = descr

df_numericas = df_numericas.transpose().reset_index().rename(columns={"index": "Coluna"})

# Estatísticas categóricas
df_categoricas = pd.DataFrame()
for col in categóricas:
    descr = df[col].describe(include='object')
    descr.name = col
    df_categoricas[col] = descr
df_categoricas = df_categoricas.transpose().reset_index().rename(columns={"index": "Coluna"})

# Criar abas
criar_aba_estatisticas("Quantitativas", df_numericas)
criar_aba_estatisticas("Qualitativas", df_categoricas)

# Iniciar GUI
root.mainloop()
