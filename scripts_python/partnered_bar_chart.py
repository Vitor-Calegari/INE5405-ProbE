import plotly.graph_objects as go
import pandas as pd
import os

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    languages = twitchdata['Partnered']
    
    language_counts = languages.value_counts()
    labels = language_counts.index.tolist()
    values = language_counts.tolist()
    
    labels = ['Parceiro' if l else 'Não parceiro' for l in labels]
    
    # Cria gráfico de barras
    fig = go.Figure(data=[go.Bar(x=labels, y=values)])
    
    fig.show()

if (__name__ == '__main__'):
    main()