import plotly.graph_objects as go
import pandas as pd
import os

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    # Seleciona a coluna de Stream time (minutes)
    stream_time = twitchdata['Stream time(minutes)']
    
    # Cria um histograma do stream time em horas
    fig = go.Figure(data=[go.Histogram(x=stream_time, nbinsx=20)])
    fig.update_layout(
        xaxis_title='Tempo de Streaming (Horas)',
        yaxis_title='Frequência'
    )
    fig.show()

if (__name__ == '__main__'):
    main()