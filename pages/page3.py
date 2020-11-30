import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, df

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
            html.H3("Map:", style={'width': '49%', 'display': 'inline-block'}),
            dcc.Dropdown(id="map_select",
                         options=[
                             {"label": "All", "value": "None"},
                             {"label": "BANK", "value": "BANK"},
                             {"label": "BARTLETT U.", "value": "BARTLETT U."},
                             {"label": "BORDER", "value": "BORDER"},
                             {"label": "CHALET", "value": "CHALET"},
                             {"label": "CLUB HOUSE", "value": "CLUB HOUSE"},
                             {"label": "COASTLINE", "value": "COASTLINE"},
                             {"label": "CONSULATE", "value": "CONSULATE"},
                             {"label": "FAVELAS", "value": "FAVELAS"},
                             {"label": "HEREFORD BASE", "value": "HEREFORD BASE"},
                             {"label": "HOUSE", "value": "HOUSE"},
                             {"label": "KAFE DOSTOYEVSKY", "value": "KAFE DOSTOYEVSKY"},
                             {"label": "KANAL", "value": "KANAL"},
                             {"label": "OREGON", "value": "OREGON"},
                             {"label": "PLANE", "value": "PLANE"},
                             {"label": "SKYSCRAPER", "value": "SKYSCRAPER"},
                             {"label": "YACHT", "value": "YACHT"}],
                         multi=False,
                         value="None",
                         style={'width': '49%', 'display': 'inline-block'}
                         )], style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            html.H3("Operator:", style={'width': '49%', 'display': 'inline-block'}),

            dcc.Dropdown(id="operator_select",
                         options=[
                             {"label": "BOPE-CAPITAO", "value": "BOPE-CAPITAO"},
                             {"label": "BOPE-CAVEIRA", "value": "BOPE-CAVEIRA"},
                             {"label": "G.E.O.-JACKAL", "value": "G.E.O.-JACKAL"},
                             {"label": "G.E.O.-MIRA", "value": "G.E.O.-MIRA"},
                             {"label": "GIGN-DOC", "value": "GIGN-DOC"},
                             {"label": "GIGN-MONTAGNE", "value": "GIGN-MONTAGNE"},
                             {"label": "GIGN-ROOK", "value": "GIGN-ROOK"},
                             {"label": "GIGN-TWITCH", "value": "GIGN-TWITCH"},
                             {"label": "GSG9-BANDIT", "value": "GSG9-BANDIT"},
                             {"label": "GSG9-BLITZ", "value": "GSG9-BLITZ"},
                             {"label": "GSG9-IQ", "value": "GSG9-IQ"},
                             {"label": "GSG9-JAGER", "value": "GSG9-JAGER"},
                             {"label": "JTF2-BUCK", "value": "JTF2-BUCK"},
                             {"label": "JTF2-FROST", "value": "JTF2-FROST"},
                             {"label": "NAVYSEAL-BLACKBEARD", "value": "NAVYSEAL-BLACKBEARD"},
                             {"label": "NAVYSEAL-VALKYRIE", "value": "NAVYSEAL-VALKYRIE"},
                             {"label": "SAS-MUTE", "value": "SAS-MUTE"},
                             {"label": "SAS-SLEDGE", "value": "SAS-SLEDGE"},
                             {"label": "SAS-SMOKE", "value": "SAS-SMOKE"},
                             {"label": "SAS-THATCHER", "value": "SAS-THATCHER"},
                             {"label": "SAT-ECHO", "value": "SAT-ECHO"},
                             {"label": "SAT-HIBANA", "value": "SAT-HIBANA"},
                             {"label": "SPETSNAZ-FUZE", "value": "SPETSNAZ-FUZE"},
                             {"label": "SPETSNAZ-GLAZ", "value": "SPETSNAZ-GLAZ"},
                             {"label": "SPETSNAZ-KAPKAN", "value": "SPETSNAZ-KAPKAN"},
                             {"label": "SPETSNAZ-TACHANKA", "value": "SPETSNAZ-TACHANKA"},
                             {"label": "SWAT-ASH", "value": "SWAT-ASH"},
                             {"label": "SWAT-CASTLE", "value": "SWAT-CASTLE"},
                             {"label": "SWAT-PULSE", "value": "SWAT-PULSE"},
                             {"label": "SWAT-THERMITE", "value": "SWAT-THERMITE"}],
                         multi=False,
                         value="None",
                         style={'width': '49%', 'display': 'inline-block'}
                         )], style={'width': '49%', 'display': 'inline-block'})
    ]),
    dcc.Graph(id='delta_figure', figure={})
])

@app.callback(
    Output(component_id='delta_figure', component_property='figure'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='map_select', component_property='value'),
     Input(component_id='operator_select', component_property='value')]
)
def generate_graph(platform_selected, map_selected, operator_selected):
    dff = df.copy()

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months,
        y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
        name='Primary Product',
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=months,
        y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
        name='Secondary Product',
        marker_color='lightsalmon'
    ))
    return fig