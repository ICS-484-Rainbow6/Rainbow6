
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

from io import BytesIO
import base64

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

# test purpose, 1M rows only
# name all the 1G file like "s1.csv", "s2.csv", etc

# for toprow in pd.read_csv("s1.csv", chunksize = 1000000):
#     fakedf = pd.DataFrame(columns = toprow.columns)
#     break

# print(toprow.iloc[0])

for df in pd.read_csv("s1.csv", chunksize=4000000):
    break
    print(df.shape)


# ------------------------------------------------------------------------------
# App layout
layout = html.Div([

    html.H1("Win Delta Per Operator VS Presence", style={'text-align': 'center'}),

    html.Div([
        html.Div([
            html.H3("Platform:", style={'width': '49%', 'display': 'inline-block'}),
            dcc.Dropdown(id="platform_select",
                         options=[
                             {"label": "All", "value": "None"},
                             {"label": "PC", "value": "PC"},
                             {"label": "PS4", "value": "PS4"},
                             {"label": "XONE", "value": "XONE"}],
                         multi=False,
                         value="None",
                         style={'width': '49%', 'display': 'inline-block'}
                         )], style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            html.H3("Role:", style={'width': '49%', 'display': 'inline-block'}),
            dcc.Dropdown(id="role_select",
                         options=[
                             {"label": "Both", "value": "None"},
                             {"label": "Attacker", "value": "Attacker"},
                             {"label": "Defender", "value": "Defender"}],
                         multi=False,
                         value="None",
                         style={'width': '49%', 'display': 'inline-block'}
                         )], style={'width': '49%', 'display': 'inline-block'})
    ]),





    html.Div([html.Img(id = 'wp_plot', src = '', style={
        'height': '50%',
        'width': '50%'
    })],
             id='plot_div', style={'textAlign': 'center'})
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(

    Output(component_id='wp_plot', component_property='src'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='role_select', component_property='value')]
)

def update_graph(platform, role):

    i1 = 1.0
    dff = df.copy()
    if platform != "None":
        dff = dff[dff["platform"] == platform]
    if role != "None":
        temp1 = dff.shape[0]
        dff = dff[dff["role"] == role]
        temp2 = dff.shape[0]
        i1 = temp2 / temp1

    average_winrate = dff["haswon"].sum() / dff.shape[0]
    rdf = dff.groupby(["operator"]).mean()["haswon"].apply(lambda x:x).reset_index()
    rdf.rename(columns={"haswon": "WinDelta"}, inplace=True)
    rdf["WinDelta"] = (rdf["WinDelta"] - average_winrate) * 100


    rdf2 = dff.groupby(["operator"]).count()["platform"].apply(lambda x:x).reset_index()
    rdf2.rename(columns={"platform": "Presence"}, inplace=True)
    rdf2["Presence"] = (rdf2["Presence"] / dff.shape[0]) * 1000 * i1

    rdf3 = pd.concat([rdf, rdf2["Presence"]], axis = 1)

    paths = rdf3["operator"]

    fig, ax = plt.subplots()
    x = rdf3["Presence"]
    y = rdf3["WinDelta"]
    ax.scatter(x, y)
    ax.grid(True)
    ax.set_xlabel('Presence (in %)')
    ax.set_ylabel('WinDelta (in %)')
    fig.set_size_inches(10, 10, forward=True)
    plt.axhline(0, color='red')
    plt.axvline(30, color='red')
    for x0, y0, path in zip(x, y,paths):
        ab = AnnotationBbox(OffsetImage(Image.open('png/' + path + '.png').resize((32,32))), (x0, y0), frameon=False)
        ax.add_artist(ab)
    out_url = fig_to_url(fig)



    return out_url



# ------------------------------------------------------------------------------
# other functions

def fig_to_url(in_fig, close_all=True):
    # type: (plt.Figure) -> str
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png')
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)





# ------------------------------------------------------------------------------
