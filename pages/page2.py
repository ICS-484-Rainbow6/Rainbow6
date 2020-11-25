
import pandas as pd
import plotly.express as px

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import df

# ------------------------------------------------------------------------------
# App layout
layout = html.Div([

    html.H1("Operator Presence by rank", style={'text-align': 'center'}),

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





    dcc.Graph(id='pbr_figure', figure={})
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(

    Output(component_id='pbr_figure', component_property='figure'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='role_select', component_property='value')]
)

def update_graph(platform, role):

    dff = df.copy()
    if platform != "None":
        dff = dff[dff["platform"] == platform]
    if role != "None":
        dff = dff[dff["role"] == role]

    rdf = dff.groupby(["skillrank", "operator"]).count()["platform"].apply(lambda x:x).reset_index()
    rdf.rename(columns={"platform": "Count"}, inplace=True)
    rdf2 = dff.groupby(["skillrank"]).count()["platform"].apply(lambda x:x).reset_index()
    rdf2.rename(columns={"platform": "Count2"}, inplace=True)
    rdf2 = rdf2.reindex([6,1,0,5,3,4,2]).reset_index()
    rdf2 = rdf2[["skillrank", "Count2"]]
    rdf3 = pd.merge(rdf2, rdf, on='skillrank', how='outer')
    rdf3["Presence"] = rdf3["Count"]/ rdf3["Count2"] * 1000
    rdf3 = rdf3[rdf3["skillrank"] != "Unranked"]
    fig = px.line(rdf3, x="skillrank", y="Presence", color="operator")


    return fig



# ------------------------------------------------------------------------------
# other functions


# ------------------------------------------------------------------------------
