from data_preprocessing import data_preprocess
import pandas as pd
import plotly.express as px
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import io
from PIL import Image
a =[]
data = data_preprocess()
def data_visualization():
    data.drop(['LOCATION','Type of clients','Criticality from previous study','Electric power not supplied EENS [kWh] ','Type of installation','Air network','SELF-PROTECTION','Air network','km of network LT:'], axis=1,inplace=True)
    col=list(data.columns)
    col.remove("Burned transformers")
    print(col)
    for i in col:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}.jpg")
        # a.append(fig)
    # for i in col:
    #     fig = ff.create_distplot([data[i].values],group_labels=[i])
    #     fig.update_layout(template='plotly_dark')
    #     #fig.update_layout(plot_bgcolor = "plotly_dark")
    #     fig.update_xaxes(showgrid=False,zeroline=False)
    #     fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        # a.append(fig)
    df=data.drop("Burned transformers",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    pio.write_image(fig, 'image.jpg', scale=6, width=1080, height=1080)
    #fig.write_image("img.jpg")
    # a.append(fig)
    
    return data

data_visualization()
