import plotly.graph_objects as go
import pandas as pd
import os
from plotly.subplots import make_subplots

def main():
    # Muda o diretório atual para o do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Importa o CSV
    twitchdata = pd.read_csv('twitchdata-update.csv')
    
    # Seleciona a coluna "Average viewers"
    average_viewers = twitchdata['Average viewers']
    
    # Cria subplots para os dois boxplots
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=[
                            'Boxplot de Average viewers',
                            'Boxplot de Average viewers (sem outliers)'
                        ])
    
    # Boxplot com outliers
    fig.add_trace(go.Box(
        y=average_viewers,
        name='Average viewers',
        boxpoints='outliers',
        hovertext=twitchdata['Channel'],
        hovertemplate='Channel: %{hovertext}<br>Average viewers: %{y}<extra></extra>'
    ), row=1, col=1)
    
    # Boxplot sem os outliers extremos
    fig.add_trace(go.Box(
        y=average_viewers,
        name='Average viewers (sem outliers)',
        boxpoints=False,
        hovertext=twitchdata['Channel'],
        hovertemplate='Channel: %{hovertext}<br>Average viewers: %{y}<extra></extra>'
    ), row=1, col=2,)
    
    # Atualiza o layout e mostra a figura
    fig.update_layout(title='Average viewers', showlegend=False)
    fig.update_yaxes(title_text='Average viewers', row=1, col=1)
    fig.update_yaxes(title_text='Average viewers', row=1, col=2)
    fig.update_yaxes(range=[0, 30000], row=1, col=2)
    fig.show()
    
if (__name__ == '__main__'):
    main()