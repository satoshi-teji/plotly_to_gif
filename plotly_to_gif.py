from PIL import Image
import plotly.graph_objects as go
import io
import numpy as np
import pandas as pd


class Converter:
    def __init__(self, layout=go.Layout()):
        self.layout = layout
        self.images = []

    def to_gif(self, ts_data, changing_index=False, indexes=np.array([])):
        data_type = type(ts_data)
        if data_type == pd.core.frame.DataFrame:
            if changing_index:
                indexes = ts_data.index.values.tolist()
            ts_data = ts_data.values

        for i in range(ts_data.shape[0]):
            fig = go.Figure()
            fig.layout = self.layout
            x, y = ts_data[i]
            fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers'))
            if changing_index:
                fig.add_annotation(text=str(indexes[i])+' sec', bgcolor='white', x=0.97, xanchor='right', xref='paper', yanchor='bottom', yref='paper', y=0.03, showarrow=False)
            image_data = fig.to_image(format='png')
            image_byte = io.BytesIO(image_data)
            img = Image.open(image_byte)
            self.images.append(img)
        self.images[0].save('output.gif',
                            save_all=True, append_images=self.images[1:],
                            optimize=False, duration=100, loop=0)
