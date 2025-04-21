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
    
    # Seleciona a coluna de Stream time (minutes)
    stream_time = twitchdata['Stream time(minutes)']
    
    # Calcula o histograma com 20 bins
    counts, bin_edges = np.histogram(stream_time, bins=20)
    
    # Calcula o valor central de cada bin (para posicionar as barras)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    
    # Cria um gráfico de barras com o número em cima de cada barra
    fig = go.Figure(data=[go.Bar(
        x=bin_centers,
        y=counts,
        text=counts,
        textposition='auto'
    )])
    
    fig.update_layout(
        xaxis_title='Tempo de Streaming (Minutos)',
        yaxis_title='Frequência'
    )
    fig.show()

if (__name__ == '__main__'):
    main()