
import pandas as pd
import dash_table as dt
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import combodf
# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

ddff = pd.DataFrame(columns=['Team', 'Win Rate %', 'Sample Size', 'Kill', 'Death'], index=[])

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

    html.Div([
        html.Div([
            dt.DataTable(
                id='combo_table',
                columns=[{"name": i, "id": i} for i in ddff.columns],
                sort_action='native',
                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
            ),
        ]),
    ], className='row'),

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
    dff = combodf.copy()
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

    dff = dff[dff["count"] > 1000]

    dff = dff.groupby("grouped").sum()[["haswon", "count", "nbkills", "isdead"]].apply(lambda x: x).reset_index()
    dff['Team'] = dff['grouped']
    dff['Kill'] = round(dff['nbkills'] / dff['count'], 3)
    dff['Death'] = round(dff['isdead'] / dff['count'], 3)
    dff['Win Rate %'] = round((dff['haswon'] / dff['count'])*100, 3)
    dff['Sample Size'] = dff['count']


    result = dff.head(50)

    rows = result.to_dict('records')

    return rows




# ------------------------------------------------------------------------------
# other functions

