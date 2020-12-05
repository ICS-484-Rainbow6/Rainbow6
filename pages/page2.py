
import pandas as pd
import numpy as np

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

df = pd.read_csv("combo.csv")

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
    ], className='row', style={'padding-bottom': '20px'}),

    html.P("hey!", id="combo_table")

],  className='ten columns offset-by-one', style={'opacity': '0.955'})


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output('combo_table', 'data'),
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



    return dff



# ------------------------------------------------------------------------------
# other functions

