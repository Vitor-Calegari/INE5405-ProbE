import plotly.graph_objects as go
import pandas as pd
import os
from plotly.subplots import make_subplots
import numpy as np

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
        
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    # Recupera dados de Followers
    followers = twitchdata['Followers']
    
    # Calcula contagens e bins para criar o histograma
    counts, bins = np.histogram(followers, bins=20)
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    
    # Calcula a porcentagem cumulativa
    cumulative = np.cumsum(counts)
    cumulative_percentage = cumulative / cumulative[-1] * 100
    
    # Cria a figura com eixo y secundário para a linha cumulativa
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Barra para as frequências
    fig.add_trace(
        go.Bar(x=bin_centers, y=counts, name='Frequência'),
        secondary_y=False,
    )
    
    # Linha para o acumulado percentual
    fig.add_trace(
        go.Scatter(x=bin_centers, y=cumulative_percentage, name='Porcentagem acumulada',
                   mode='lines+markers'),
        secondary_y=True,
    )
    
    # Atualiza o layout do gráfico
    fig.update_layout(
        title='Gráfico de Pareto de Seguidores',
        xaxis_title='Seguidores'
    )
    fig.update_yaxes(title_text="Frequência", secondary_y=False)
    fig.update_yaxes(title_text="Porcentagem acumulada", secondary_y=True, range=[0, 110])
    
    fig.show()

if (__name__ == '__main__'):
    main()