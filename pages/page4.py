
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
        html.H1("Some Statistical Facts That May Interest You",
                style={'font-family': 'Helvetica',
                       "margin-top": "25",
                       "margin-bottom": "20"}, className='eight columns'),
    ], className='row'),

    # story 1
    # one story, left graph right text
    html.Div([
        # dropdown and figure
        html.Div([
            # dropdowns
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
                    )], className='four columns', style={'margin-top': '10'}),

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
                    )], className='four columns', style={'margin-top': '10'}),

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
                    )], className='four columns', style={'margin-top': '10'})
            ], className='row', style={'padding': '10px'}),
            # end of dropdown
            dcc.Graph(id='pbr_figure')
        ], className='six columns'),
        html.Div([
            html.H2('Operator preference in different ranks', style={'fontWeight': 'bold', 'color': 'white'}),
            html.Div(style={'padding-bottom': '20px'}),

            html.H6('Interesting fact:', style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('The result shows that players in higher ranks prefer Ash and Jager than other operators.',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.Div(style={'padding-bottom': '20px'}),

            html.H6('Possible reason:', style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('Ash and Jager both have one of the best primary weapons of their roles. '
                   'Their high movement speed and powerful special skills make them the best picks in their position.',
                   style={'fontWeight': 'bold', 'color': 'white'}),

            html.H6('How to use the graph:', style={'fontWeight': 'bold', 'color': 'white', 'padding-top': '20px'}),
            html.P('Double click on a row of the legend to see the presence curve of that operator.',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('* Diamond rank games may contain Platinum players, '
                   'causing the calculated presence rate slightly different than the actual value.',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.Div(style={'padding-bottom': '20px'}),
        ], className='six columns', style={'padding-left': '15px', 'padding-top': '15px', 'background': '#2b2b2b'})
    ], className='row'),

    # html.Div(style={'padding-bottom': '20px'}),

    # story 2
    # one story, left graph right text
    html.Div([
        html.Div([
            html.H2('Secondary Gadget Picks To Win Rate',
                    style={'fontWeight': 'bold', 'color': 'white'}),
            html.Div(style={'padding-bottom': '20px'}),
            html.H6('Win Delta:', style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('The win rate of operators who carry this secondary gadget minus the average win rate of the operators\' role.',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('* This value may be affected by the win rate of the operators',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.Div(style={'padding-bottom': '20px'}),
            html.H6('Interesting Facts:', style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('Barbed wire seems to be the best secondary gadget for defenders.',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('Impact grenade are more helpful in Bomb Mode because they can be used to connect two targets',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.Div(style={'padding-bottom': '20px'}),
            html.H6('How to use the graph:', style={'fontWeight': 'bold', 'color': 'white', 'padding-top': '20px'}),
            html.P('Use the dropdowns as the filter.',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.P('** Attackers and defenders have completely different secondary gadget options',
                   style={'fontWeight': 'bold', 'color': 'white'}),
            html.Div(style={'padding-bottom': '20px'}),
        ], className='six columns', style={'padding-left': '15px', 'padding-top': '15px', 'background': '#2b2b2b'}),

        # dropdowns and graph
        html.Div([
            # dropdowns
            html.Div([

                html.Div([
                    html.P("Platform:"),
                    dcc.Dropdown(
                        id="platform_select2",
                        options=[
                            {"label": "All", "value": "All"},
                            {"label": "PC", "value": "PC"},
                            {"label": "PS4", "value": "PS4"},
                            {"label": "XONE", "value": "XONE"}],
                        multi=False,
                        value="All",
                    )], className='three columns', style={'margin-top': '10'}),

                html.Div([
                    html.P("Game Mode:"),
                    dcc.Dropdown(
                        id="gamemode_select2",
                        options=[
                            {"label": "All", "value": "All"},
                            {"label": "Bomb", "value": "BOMB"},
                            {"label": "Secure", "value": "SECURE"},
                            {"label": "Hostage", "value": "HOSTAGE"}],
                        multi=False,
                        value="All",
                    )], className='three columns', style={'margin-top': '10'}),

                html.Div([
                    html.P("Rank:"),
                    dcc.Dropdown(
                        id="skillrank_select2",
                        options=[
                            {"label": "All", "value": "All"},
                            {"label": "Copper & Bronze", "value": "Copper & Bronze"},
                            {"label": "Silver & Gold", "value": "Silver & Gold"},
                            {"label": "Platinum+", "value": "Platinum+"}],
                        multi=False,
                        value="All",
                    )], className='three columns', style={'margin-top': '10'}),

                html.Div([
                    html.P("Role:"),
                    dcc.Dropdown(
                        id="role_select2",
                        options=[
                            {"label": "Both", "value": "All"},
                            {"label": "Attacker", "value": "Attacker"},
                            {"label": "Defender", "value": "Defender"}],
                        multi=False,
                        value="All",
                    )], className='three columns', style={'margin-top': '10'})

            ], className='row', style={'padding': '20px'}),
            # end of dropdown
            dcc.Graph(id='sg_figure')

        ], className='six columns')
    ], className='row'),





],  className='ten columns offset-by-one', style={'opacity': '0.955'})


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
# call back of figure #1
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
# Connect the Plotly graphs with Dash Components
# call back of figure #2
@app.callback(

    Output(component_id='sg_figure', component_property='figure'),
    [Input(component_id='platform_select2', component_property='value'),
     Input(component_id='gamemode_select2', component_property='value'),
     Input(component_id='skillrank_select2', component_property='value'),
     Input(component_id='role_select2', component_property='value')]
)

def update_graph(platform, gamemode, skillrank, role):

    # Apply filters
    dff = df.copy()
    if platform != "All":
        dff = dff[dff["platform"] == platform]
    else:
        dff = dff[~dff["operator"].str.contains("RESERVE")]

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

    # remove impossible role & secondary gadget combination
    dff = dff[~((dff["role"] == "Attacker") & (dff["secondarygadget"] == "IMPACT GRENADE"))]
    dff = dff[~((dff["role"] == "Attacker") & (dff["secondarygadget"] == "NITRO CELL"))]
    dff = dff[~((dff["role"] == "Defender") & (dff["secondarygadget"] == "FRAG GRENADE"))]
    dff = dff[~((dff["role"] == "Defender") & (dff["secondarygadget"] == "STUN GRENADE"))]

    adf = dff.groupby("role").sum()[["haswon", "count"]].apply(lambda x:x).reset_index()
    adf["avrwinrate"] = adf["haswon"] / adf["count"]
    adf = adf[["role", "avrwinrate"]]

    wdf = dff.groupby(["role", "secondarygadget"]).sum()[["haswon", "count"]].apply(lambda x: x).reset_index()
    wdf = pd.merge(wdf, adf, on="role", how='outer')
    print(wdf)
    wdf["windelta"] = (wdf["haswon"] / wdf["count"] - wdf["avrwinrate"]) * 100



    fig = px.bar(wdf, x="secondarygadget", y="windelta")

    return fig




# ------------------------------------------------------------------------------
# other functions


# ------------------------------------------------------------------------------
