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
    
    # Cria o gráfico de barras com os valores acima das barras
    min_val = stream_time.min()
    max_val = stream_time.max()
    bin_size = (max_val - min_val) / 8
    
    fig = go.Figure(data=[go.Histogram(
        x=stream_time,
        xbins=dict(
            start=min_val,
            end=max_val,
            size=bin_size
        ),
        texttemplate="%{y}",
        textposition='outside'
    )])
    
    fig.update_layout(
        xaxis_title='Tempo de Streaming (Minutos)',
        yaxis_title='Frequência'
    )
    fig.show()

if (__name__ == '__main__'):
    main()