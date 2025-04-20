import plotly.graph_objects as go
import pandas as pd
import os
import sys

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    languages = twitchdata['Language']
    
    language_counts = languages.value_counts()
    labels = language_counts.index.tolist()
    values = language_counts.tolist()
    
    # Cria gráfico de donout
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.show()

if (__name__ == '__main__'):
    main()