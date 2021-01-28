import plotly_to_gif as ptg
import numpy as np
import pandas as pd
import plotly.graph_objects as go

layout = go.Layout(title=go.layout.Title(text='test', x=0.5, y=0.9, xanchor='center', yanchor='top'),
                    xaxis=go.layout.XAxis(title='y', range=[-10, 10], showgrid=True, scaleanchor='y'),
                    yaxis=go.layout.YAxis(title='x', range=[-10,10], showgrid=True))
gif_conv = ptg.Converter(layout)
a = np.linspace(0, 9, 100)
a = a.reshape(100//2,2)
a_pd = pd.DataFrame(a)
gif_conv.to_gif(a_pd, changing_index=True)