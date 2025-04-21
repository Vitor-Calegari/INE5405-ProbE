import plotly.graph_objects as go
import pandas as pd
import os
import numpy as np

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    # Seleciona a coluna de Watch time (minutes)
    watch_time = twitchdata['Watch time(Minutes)']
    
    # Calcula o histograma manualmente para obter os valores
    hist, bin_edges = np.histogram(watch_time, bins=20)
    # Calcula o centro de cada bin para posicionar as barras
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Cria o gráfico de barras com os valores acima das barras
    fig = go.Figure(data=[go.Bar(
        x=bin_centers,
        y=hist,
        text=hist,
        textposition='outside'
    )])
    fig.update_layout(
        xaxis_title='Tempo assistido (Minutos)',
        yaxis_title='Frequência'
    )
    fig.show()

if (__name__ == '__main__'):
    main()