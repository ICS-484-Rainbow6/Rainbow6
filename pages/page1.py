
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
from app import df
# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)


# ------------------------------------------------------------------------------
# App layout
layout = html.Div([

    html.Div([
        html.H1("Win Delta Per Operator VS Presence", style={'font-family': 'Helvetica',
                                                             "margin-top": "25",
                                                             "margin-bottom": "0"}, className='eight columns'),
    ], className='row'),

    html.Div([
        html.Div([
            html.P("Platform:"),
            dcc.Dropdown(
                id="platform_select",
                options=[
                    {"label": "All", "value": "All"},
                    {"label": "PC", "value": "PC"},
                    {"label": "PS4", "value": "PS4"},
                    {"label": "XONE", "value": "XONE"}],
                multi=False,
                value="All",
            )], className='two columns', style={'margin-top': '10'}),

        html.Div([
            html.P("Rank:"),
            dcc.Dropdown(
                id="skillrank_select",
                options=[
                    {"label": "All", "value": "All"},
                    {"label": "Copper & Bronze", "value": "Copper & Bronze"},
                    {"label": "Silver & Gold", "value": "Silver & Gold"},
                    {"label": "Platinum+", "value": "Platinum+"}],
                multi=False,
                value="All",
            )], className='two columns', style={'margin-top': '10'}),

        html.Div([
            html.P("Game Mode:"),
            dcc.Dropdown(
                id="gamemode_select",
                options=[
                    {"label": "All", "value": "All"},
                    {"label": "Bomb", "value": "BOMB"},
                    {"label": "Secure", "value": "SECURE"},
                    {"label": "Hostage", "value": "HOSTAGE"}],
                multi=False,
                value="All",
            )], className='two columns', style={'margin-top': '10'}),


        html.Div([
            html.P("Role:"),
            dcc.Dropdown(
                id="role_select",
                options=[
                    {"label": "Both", "value": "All"},
                    {"label": "Attacker", "value": "Attacker"},
                    {"label": "Defender", "value": "Defender"}],
                multi=False,
                value="All",
            )], className='two columns', style={'margin-top': '10'})
    ]),
    html.Div([html.Img(id='wp_plot', src='', style={
        'height': '60%',
        'width': '60%'
    })],
             id='plot_div', style={'textAlign': 'center'}),
],  className='ten columns offset-by-one')


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(

    Output(component_id='wp_plot', component_property='src'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='skillrank_select', component_property='value'),
     Input(component_id='gamemode_select', component_property='value'),
     Input(component_id='role_select', component_property='value')]
)

def update_graph(platform, skillrank, gamemode, role):

    # Apply filters
    dff = df.copy()
    if platform != "All":
        dff = dff[dff["platform"] == platform]

    if skillrank == "Copper & Bronze":
        dff = dff[(dff["skillrank"] == "Copper") | (dff["skillrank"] == "Bronze")]
    if skillrank == "Silver & Gold":
        dff = dff[(dff["skillrank"] == "Silver") | (dff["skillrank"] == "Gold")]
    if skillrank == "Platinum+":
        dff = dff[(dff["skillrank"] == "Platinum") | (dff["skillrank"] == "Diamond")]

    if gamemode != "All":
        dff = dff[dff["gamemode"] == gamemode]

    if role != "All":
        dff = dff[dff["role"] == role]





    # windelta df
    factor = ["operator"]
    wdf = dff.groupby(factor).sum()[["haswon", "count"]].apply(lambda x:x).reset_index()
    wdf["windelta"] = (wdf["haswon"] / wdf["count"] - 0.5) * 100


    # presence df

    pdf = dff.groupby(["operator", "role"]).sum()["count"].apply(lambda x:x).reset_index()

    ## operator df
    rdf = dff.groupby("role").sum()["count"].apply(lambda x:x).reset_index()
    rdf.rename(columns={"count": "role_count"}, inplace=True)
    pdf = pd.merge(rdf, pdf, on="role", how='outer')
    pdf["presence"] = pdf["count"] / pdf["role_count"] * 500

    # result df
    result = pd.merge(wdf[["operator", "windelta"]], pdf[["operator", "presence"]], on=factor, how='outer')
    paths = result["operator"]

    fig, ax = plt.subplots()
    x = result["presence"]
    y = result["windelta"]
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
