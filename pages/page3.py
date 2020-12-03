import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app, df
import dash_table as dt

ddff_data={'primaryweapon': 'ITA12L', 'secondaryweapon': 'ITA12S', 'Win Rate %': 0.463, 'Presence Rate %': 0.009, 'kill': 0.526, 'dead': 0.747}
ddff = pd.DataFrame(ddff_data, columns=['primaryweapon', 'secondaryweapon', 'Win Rate %', 'Presence Rate %', 'kill', 'dead'], index=[])
layout = html.Div([

    #title
    html.Div([
        html.H1("Win Delta Per Operator VS Presence", style={'font-family': 'Helvetica',
                       "margin-top": "25",
                       "margin-bottom": "0"}, className='eight columns'),
    ], className='row'),
    #Dropdown Menu
    html.Div([
        html.Div([
            html.P("Platform:"),
            dcc.Dropdown(
                id="platform_select",
                options=[
                    {"label": "All", "value": "None"},
                    {"label": "PC", "value": "PC"},
                    {"label": "PS4", "value": "PS4"},
                    {"label": "XONE", "value": "XONE"}
                ],
                multi=False,
                value='None'
            )
            ], className='two columns', style={'margin-top': '10'}),
        html.Div([
            html.P('Rank:'),
            dcc.Dropdown(
                id="rank_select",
                options=[
                    {"label": "All", "value": "None"},
                    {"label": "Unranked", "value": "Unranked"},
                    {"label": "Copper", "value": "Copper"},
                    {"label": "Bronze", "value": "Bronze"},
                    {"label": "Silver", "value": "Silver"},
                    {"label": "Gold", "value": "Gold"},
                    {"label": "Platinum", "value": "Platinum"},
                    {"label": "Diamond", "value": "Diamond"}
                ],
                multi=False,
                value='None'
            )
        ], className='two columns', style={'margin-top': '10'}),
        html.Div([
            html.P('Map:'),
            dcc.Dropdown(
                id="map_select",
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
                    {"label": "YACHT", "value": "YACHT"}
                ],
                multi=False,
                value='None'
            )
        ], className='two columns', style={'margin-top': '10'}),
        html.Div([
            html.P('Operator:'),
            dcc.Dropdown(
                id="operator_select",
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
                    {"label": "SWAT-THERMITE", "value": "SWAT-THERMITE"}
                ],
                multi=False,
                value='None'
            )
        ], className='two columns', style={'margin-top': '10'})
    ], className='row'),
    html.Div([
        html.Div([
            html.H4('Primary & Secondary Weapon data Per Game', style={'padding-bottom': '26px', 'padding-top': '16px'}),
            dt.DataTable(
                id='datatable',
                columns=[{"name": i, "id": i} for i in ddff.columns],
                sort_action='native',

            )

        ], className="six columns"),
        html.Div([
            dcc.Graph(id='delta_figure', figure={})
        ], className="six columns")
    ], className='row')


], className='ten columns offset-by-one')


# callback and function for the dataTable
@app.callback(
    Output('datatable', 'data'),
    [dash.dependencies.Input('platform_select', 'value'),
     dash.dependencies.Input('rank_select', 'value'),
     dash.dependencies.Input('map_select', 'value'),
     dash.dependencies.Input('operator_select', 'value')]
)
def generate_table(platform_selected, rank_selected, map_selected, operator_selected):
    if operator_selected != "None":
        table_data = df.loc[(df['operator'] == operator_selected)]
        if rank_selected != "None":
            table_data = table_data.loc[(df['skillrank'] == rank_selected)]
        if map_selected != "None":
            table_data = table_data.loc[(df['mapname'] == map_selected)]
        if platform_selected != "None":
            table_data = table_data.loc[(df['platform'] == platform_selected)]

        factor = [("primaryweapon"), ("secondaryweapon")]
        table_data = table_data.groupby(factor).sum()[["haswon", "count", "nbkills", "isdead"]].apply(lambda x: x).reset_index()
        table_data['kill'] = round(table_data['nbkills'] / table_data['count'], 3)
        table_data['dead'] = round(table_data['isdead'] / table_data['count'], 3)
        table_data['Win Rate %'] = round((table_data['haswon'] / table_data['count'])*100, 3)


        tempNum = 0
        for each in table_data['count']:
            tempNum += each
        print(tempNum)
        table_data['Presence Rate %'] = round((table_data['count'] / tempNum)*100, 3)

        res = table_data.groupby(factor).sum()[["Win Rate %", "Presence Rate %", "kill", "dead"]].apply(lambda x: x).reset_index()

        rows = res.to_dict('records')
        print(rows)
        return rows

    else:
        return


# callback and function for the win Delta Chart
@app.callback(
    Output(component_id='delta_figure', component_property='figure'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='rank_select', component_property='value'),
     Input(component_id='map_select', component_property='value'),
     Input(component_id='operator_select', component_property='value')]
)
def generate_graph(platform_selected, rank_selected, map_selected, operator_selected):
    if operator_selected != "None":
        dff = df.loc[(df['operator'] == operator_selected)]
        if rank_selected != "None":
            dff = dff.loc[(df['skillrank'] == rank_selected)]
        if map_selected != "None":
            dff = dff.loc[(df['mapname'] == map_selected)]
        if platform_selected != "None":
            dff = dff.loc[(df['platform'] == platform_selected)]

        #dealing with data
        factor = [("primaryweapon"), ("secondaryweapon")]
        wdf = dff.groupby(factor).sum()[["haswon", "count"]].apply(lambda x: x).reset_index()
        wdf['winrate'] = wdf['haswon'] / wdf['count']
        factor2 = ['operator']
        avf = dff.groupby(factor2).sum()[["haswon", "count"]].apply(lambda x: x).reset_index()
        avf['winrate'] = avf['haswon'] / avf['count']
        tempNum = avf['winrate'][0]
        wdf['winDelta'] = (wdf['winrate'] - tempNum)*100
        tempNum = avf['count'][0]
        wdf['presence'] = (wdf['count'] / tempNum)*100


        #generate graph
        fig = go.Figure()
        for index, row in wdf.iterrows():
            tempName = row['primaryweapon'] + ' & ' + row['secondaryweapon']
            fig.add_trace(go.Scatter(x=[row['presence']], y=[row['winDelta']], mode='markers', marker=dict(size=[40]),name=tempName))

        fig.update_layout(title='Weapon Influence about Win Rate',
                          xaxis_title='Presence (in %)',
                          yaxis_title='Win Delta(in %)')

        return fig
    else:

        fig = go.Figure()
        fig.update_layout(title='Weapon combo Influence about Win Rate',
                          xaxis_title='Presence (in %)',
                          yaxis_title='Win Delta(in %)')

        return fig

