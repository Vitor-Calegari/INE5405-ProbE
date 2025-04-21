import plotly.graph_objects as go
import pandas as pd
import os

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
    
    # Cria gráfico de barras com o número em cima de cada barra
    fig = go.Figure(data=[go.Bar(x=labels, y=values, text=values, textposition='outside')])
    fig.update_layout(title='Contagem de Idiomas', xaxis_title='Idioma', yaxis_title='Contagem')
    fig.show()

if (__name__ == '__main__'):
    main()