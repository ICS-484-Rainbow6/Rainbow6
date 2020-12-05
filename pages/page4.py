
import pandas as pd
import plotly.express as px

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import df

# ------------------------------------------------------------------------------
# Import


# ------------------------------------------------------------------------------
# App layout
layout = html.Div([

    html.Div([
        html.H1("Operator Presence by Rank", style={'font-family': 'Helvetica',
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
    ], className='row'),
    html.Div([dcc.Graph(id='pbr_figure', figure={})])
],  className='ten columns offset-by-one')


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(

    Output(component_id='pbr_figure', component_property='figure'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='gamemode_select', component_property='value'),
     Input(component_id='role_select', component_property='value')]
)

def update_graph(platform, gamemode, role):

    # Apply filters
    dff = df.copy()
    if platform != "All":
        dff = dff[dff["platform"] == platform]

    if gamemode != "All":
        dff = dff[dff["gamemode"] == gamemode]

    if role != "All":
        dff = dff[dff["role"] == role]

    # remove unranked and reserve operators
    dff = dff[dff["skillrank"] != "Unranked"]
    dff = dff[~dff["operator"].str.contains('RESERVE')]
    dff = dff.groupby(["skillrank", "role", "operator"]).sum()["count"].apply(lambda x: x).reset_index()

    # count the total rounds in each skillrank & role group

    rank = dff.groupby(["skillrank"]).sum()["count"].apply(lambda x: x).reset_index()
    rank = rank.reindex([1,0,5,3,4,2]).reset_index()
    rank = rank["skillrank"]

    total = dff.groupby(["skillrank", "role"]).sum()["count"].apply(lambda x: x).reset_index()
    total = pd.merge(rank, total, on=["skillrank"], how='outer')
    total.rename(columns={"count": "total"}, inplace=True)

    # this merge order matters
    dff = pd.merge(total, dff, on=["skillrank", "role"], how='outer')
    dff["presence"] = dff["count"] / dff["total"] * 500
    fig = px.line(dff, x="skillrank", y="presence", color="operator")

    return fig

# ------------------------------------------------------------------------------
# other functions


# ------------------------------------------------------------------------------
