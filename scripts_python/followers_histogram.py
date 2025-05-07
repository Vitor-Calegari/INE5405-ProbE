import plotly.graph_objects as go
import pandas as pd
import os

import plotly.express as px

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    # Recupera dados de Followers
    followers = twitchdata['Followers']
    
    fig = px.histogram(followers, nbins=8, text_auto=True)
    fig.update_layout(
        title='Histograma de Seguidores',
        xaxis_title='Seguidores',
        yaxis_title='Frequência',
    )
    fig.show()

if (__name__ == '__main__'):
    main()