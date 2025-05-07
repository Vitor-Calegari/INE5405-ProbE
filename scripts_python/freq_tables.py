import pandas as pd
import tkinter as tk
from tkinter import ttk

# Carregar dados
df = pd.read_csv("twitchdata-update.csv")

discretas = ["Followers", "Watch time(Minutes)", "Stream time(minutes)", "Peak viewers", "Average viewers", "Followers gained", "Views gained"]
nominais = ["Partnered", "Mature", "Language"]

# Criar janela principal
root = tk.Tk()
root.title("Tabelas de Frequência")

# Notebook com abas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Função para criar uma aba com rótulo e tabela
def criar_aba(titulo, tabela_df):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=titulo)

    # Rótulo acima da tabela
    label = ttk.Label(frame, text=f"Tabela de Frequência: {titulo}", font=("Helvetica", 14, "bold"))
    label.pack(pady=10)

    # Criar Treeview
    tree = ttk.Treeview(frame, columns=list(tabela_df.columns), show="headings", style="Custom.Treeview")

    # Configurar colunas
    for col in tabela_df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)

    # Inserir linhas com zebra striping
    for index, row in tabela_df.iterrows():
        tag = 'evenrow' if index % 2 == 0 else 'oddrow'
        tree.insert("", "end", values=list(row), tags=(tag,))

    # Adicionar linha de total
    total_freq = tabela_df["Frequência"].sum()
    total_percent = 100.0
    valores_total = ["Total", total_freq, f"{total_percent:.2f}"]
    tree.insert("", "end", values=valores_total, tags=('total',))

    # Estilo das linhas
    tree.tag_configure('evenrow', background='#FFFFFF')     # branco
    tree.tag_configure('oddrow', background='#F0F0F0')       # cinza claro
    tree.tag_configure('total', font=('Helvetica', 10, 'bold'), background='#D0D0D0')  # linha total

    # Adicionar barra de rolagem
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Empacotar Treeview
    tree.pack(expand=True, fill="both", padx=10, pady=10)

# Estilo com linhas separadoras
style = ttk.Style()
style.configure("Custom.Treeview", rowheight=25)
style.configure("Custom.Treeview.Heading", font=("Helvetica", 11, "bold"))
style.map("Custom.Treeview", background=[('selected', '#ececec')])

# Processar variáveis discretas
for coluna in discretas:
    df["faixa"] = pd.cut(df[coluna], bins=8)
    frequencia = df["faixa"].value_counts().sort_index()
    porcentagem = df["faixa"].value_counts(normalize=True).sort_index() * 100

    tabela = pd.DataFrame({
        "Faixa": frequencia.index.astype(str),
        "Frequência": frequencia.values,
        "Porcentagem (%)": porcentagem.round(2).values
    })

    criar_aba(coluna, tabela)

# Processar variáveis nominais
for coluna in nominais:
    frequencia = df[coluna].value_counts()
    porcentagem = df[coluna].value_counts(normalize=True) * 100

    tabela = pd.DataFrame({
        coluna: frequencia.index.astype(str),
        "Frequência": frequencia.values,
        "Porcentagem (%)": porcentagem.round(2).values
    })

    criar_aba(coluna, tabela)

root.mainloop()
