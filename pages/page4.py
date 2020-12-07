
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
        html.H1("Some statistical facts that may interest you", style={'font-family': 'Helvetica',
                                                                       "margin-top": "25",
                                                                       "margin-bottom": "0"}, className='eight columns'),
    ], className='row'),


    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.P("Platform:", style={'fontWeight': 'bold', 'color': 'white'}),
                    dcc.Dropdown(
                        id="platform_select",
                        options=[
                            {"label": "All", "value": "All"},
                            {"label": "PC", "value": "PC"},
                            {"label": "PS4", "value": "PS4"},
                            {"label": "XONE", "value": "XONE"}],
                        multi=False,
                        value="All",
                    )], className='four columns', style={'margin-top': '10'}),

                html.Div([
                    html.P("Game Mode:", style={'fontWeight': 'bold', 'color': 'white'}),
                    dcc.Dropdown(
                        id="gamemode_select",
                        options=[
                            {"label": "All", "value": "All"},
                            {"label": "Bomb", "value": "BOMB"},
                            {"label": "Secure", "value": "SECURE"},
                            {"label": "Hostage", "value": "HOSTAGE"}],
                        multi=False,
                        value="All",
                    )], className='four columns', style={'margin-top': '10'}),

                html.Div([
                    html.P("Role:", style={'fontWeight': 'bold', 'color': 'white'}),
                    dcc.Dropdown(
                        id="role_select",
                        options=[
                            {"label": "Both", "value": "All"},
                            {"label": "Attacker", "value": "Attacker"},
                            {"label": "Defender", "value": "Defender"}],
                        multi=False,
                        value="All",
                    )], className='four columns', style={'margin-top': '10'})
            ], className='row', style={'padding': '10px'}),
            dcc.Graph(id='pbr_figure')
        ], className='six columns'),
        html.Div([
            html.H2('Operator preference in different ranks', style={'fontWeight': 'bold', 'color': 'white', 'padding-bottom': '20px'}),
            html.H6('Interesting fact:', style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('The result shows that players in higher ranks prefer Ash and Jager than other operators.', style={'fontWeight': 'bold', 'color': 'white'}),

            html.H6('Possible reason:', style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('Ash and Jager both have one of the best primary weapons of their roles. Their high movement speed and powerful special skills make them the best picks in their position.', style={'fontWeight': 'bold', 'color': 'white'}),

            html.H6('How to use the graph:', style={'fontWeight': 'bold', 'color': 'white', 'padding-top': '20px'}),
            html.P('Double click on a row of the legend to see the presence curve of that operator.', style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('* Diamond rank games may contain Platinum players, causing the calculated presence rate slightly different than the actual value.', style={'fontWeight': 'bold', 'color': 'white', 'padding-top': '20px'}),
        ], className='six columns', style={'padding-left':'5px', 'padding-top': '15px'})
    ], className='row', style={'background': '#2b2b2b'}),


],  className='ten columns offset-by-one', style={'opacity': '0.955'})


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
