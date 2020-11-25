  
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
from plotly.tools import mpl_to_plotly
from io import BytesIO
import base64

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

# test purpose, 1M rows only
# name all the 1G file like "s1.csv", "s2.csv", etc

for toprow in pd.read_csv("s1.csv", chunksize = 1000000):
    df = pd.DataFrame(columns = toprow.columns)
    break

print(toprow.iloc[0])


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Win Delta Per Operator VS Presence", style={'text-align': 'center'}),
    
    html.H3("Platform:"),   
    dcc.Dropdown(id="platform_select",
                 options=[
                     {"label": "All", "value": "None"},
                     {"label": "PC", "value": "PC"},
                     {"label": "PS4", "value": "PS4"},
                     {"label": "XONE", "value": "XONE"}],
                 multi=False,
                 value="None",
                 style={'width': "40%"}
                 ),
    
    html.H3("Role:"),
    dcc.Dropdown(id="role_select",
                 options=[
                     {"label": "Both", "value": "None"},
                     {"label": "Attacker", "value": "Attacker"},
                     {"label": "Defender", "value": "Defender"}],
                 multi=False,
                 value="None",
                 style={'width': "40%"}
                 ),
    
    dcc.Graph(id='windelta_figure', figure={}),
    html.Div([html.Img(id = 'wp_plot', src = '')],
             id='plot_div')
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='windelta_figure', component_property='figure'),
     Output(component_id='wp_plot', component_property='src')],
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='role_select', component_property='value')]
)

def update_graph(platform, role):
   
    dff = toprow.copy()
    if platform != "None":
        dff = dff[dff["platform"] == platform]
    if role != "None":
        dff = dff[dff["role"] == role]
    
    rdf = dff.groupby(["operator"]).mean()["haswon"].apply(lambda x:x).reset_index()
    rdf.rename(columns={"haswon": "WinDelta"}, inplace=True)
    rdf["WinDelta"] = (rdf["WinDelta"] - 0.5) * 100
    fig1 = px.bar(rdf, x="operator", y="WinDelta")
    
    
    rdf2 = dff.groupby(["operator"]).count()["platform"].apply(lambda x:x).reset_index()
    rdf2.rename(columns={"platform": "Presence"}, inplace=True)
    rdf2["Presence"] = (rdf2["Presence"] / dff.shape[0]) * 100
    
    rdf3 = pd.concat([rdf, rdf2["Presence"]], axis = 1)
      
    paths = rdf3["operator"]
    
    fig= plt.figure()
    fig, ax = plt.subplots()
    x = rdf3["Presence"]
    y = rdf3["WinDelta"]
    ax.scatter(x, y)
    ax.grid(True)
    for x0, y0, path in zip(x, y,paths):
        ab = AnnotationBbox(OffsetImage(Image.open('png\\' + path + '.png').resize((30,30))), (x0, y0), frameon=False)
        ax.add_artist(ab)
    out_url = fig_to_uri(fig)

    
    
    return fig1, out_url



# ------------------------------------------------------------------------------
# other functions

def fig_to_uri(in_fig, close_all=True, **save_args):
    # type: (plt.Figure) -> str
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)





# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)