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

ddff_data={'PrimaryWeapon': 'ITA12L', 'SecondaryWeapon': 'ITA12S', 'Win Rate %': 0.463, 'Presence Rate %': 0.009, 'Kill': 0.526, 'Dead': 0.747}
ddff = pd.DataFrame(ddff_data, columns=['PrimaryWeapon', 'SecondaryWeapon', 'Win Rate %', 'Presence Rate %', 'Kill', 'Dead'], index=[])

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
                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
            ),


        ], className="six columns"),
        html.Div([
            dcc.Graph(id='delta_figure', figure={}),
        ], className="six columns")
    ], className='row'),
    html.Div([
        html.Div([
            html.H4('Operator Capability', style={'margin-top': '-10px'}),
            html.P('5 is the maximum value for each dimension,'),
            html.P('which means the operator is the best at this ability for overall.'),
            dcc.Graph(id='ability_figure', figure={})
        ], className="six columns"),
        html.Div([
            html.P('Win Delta:', style={'fontWeight': 'bold'}),
            html.P('Win Delta = (The Win rate of WeaponCombo) - (The Win rate of the Operator)'),
            html.P('If the numbers of Win Delta is greater than 0, You have higher probability than average to win this game by using this Weapon combos.'),
            html.P('Presence:', style={'fontWeight': 'bold'}),
            html.P('Presence = (The presence number of WeaponCombo) / (The Overall presence number of the Operator)'),
            html.P('Presence means the popularity of this WeaponCombos.'),
            html.P('Kill: (in Table)', style={'fontWeight': 'bold'}),
            html.P('Kill = (The total kill of the WeaponCombo) / (The number of picked times of the WeaponCombo)'),
            html.P('Kill means the average kills can get in each round when you pick the WeaponCombo.'),
            html.P('Dead: (in Table)', style={'fontWeight': 'bold'}),
            html.P('Dead = (The total Dead when pick WeaponCombo) / (The number of picked times of the WeaponCombo)'),
            html.P('Dead means the average dead times in each round when you pick the WeaponCombo.'),
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
    table_data = df.copy()
    if operator_selected != "None":
        table_data = table_data.loc[(table_data['operator'] == operator_selected)]
        if rank_selected != "None":
            table_data = table_data.loc[(table_data['skillrank'] == rank_selected)]
        if map_selected != "None":
            table_data = table_data.loc[(table_data['mapname'] == map_selected)]
        if platform_selected != "None":
            table_data = table_data.loc[(table_data['platform'] == platform_selected)]

        factor = [("primaryweapon"), ("secondaryweapon")]
        table_data = table_data.groupby(factor).sum()[["haswon", "count", "nbkills", "isdead"]].apply(lambda x: x).reset_index()
        table_data['Kill'] = round(table_data['nbkills'] / table_data['count'], 3)
        table_data['Dead'] = round(table_data['isdead'] / table_data['count'], 3)
        table_data['Win Rate %'] = round((table_data['haswon'] / table_data['count'])*100, 3)
        table_data['PrimaryWeapon'] = table_data['primaryweapon']
        table_data['SecondaryWeapon'] = table_data['secondaryweapon']

        tempNum = 0
        for each in table_data['count']:
            tempNum += each
        print(tempNum)
        table_data['Presence Rate %'] = round((table_data['count'] / tempNum)*100, 3)
        factor7 = [("PrimaryWeapon"), ("SecondaryWeapon")]

        res = table_data.groupby(factor7).sum()[["Win Rate %", "Presence Rate %", "Kill", "Dead"]].apply(lambda x: x).reset_index()

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
    dff = df.copy()
    if operator_selected != "None":
        dff = dff.loc[(dff['operator'] == operator_selected)]
        if rank_selected != "None":
            dff = dff.loc[(dff['skillrank'] == rank_selected)]
        if map_selected != "None":
            dff = dff.loc[(dff['mapname'] == map_selected)]
        if platform_selected != "None":
            dff = dff.loc[(dff['platform'] == platform_selected)]

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
            fig.add_trace(go.Scatter(x=[row['presence']], y=[row['winDelta']], mode='markers', marker=dict(size=[20]),name=tempName))

        fig.update_layout(title='Weapon Influence about Win Rate',
                          xaxis_title='Presence (in %)',
                          yaxis_title='Win Delta(in %)',
                          yaxis_zeroline=True,
                          yaxis_zerolinecolor='red',
                          )


        return fig
    else:

        fig = go.Figure()
        fig.update_layout(title='Weapon combo Influence about Win Rate',
                          xaxis_title='Presence (in %)',
                          yaxis_title='Win Delta(in %)')

        return fig

@app.callback(
    Output(component_id='ability_figure', component_property='figure'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='rank_select', component_property='value'),
     Input(component_id='map_select', component_property='value'),
     Input(component_id='operator_select', component_property='value')]
)
def generate_abgraph(platform_selected, rank_selected, map_selected, operator_selected):
    if operator_selected != "None":
        temp_df = df.copy()

        temp_df = temp_df[temp_df.operator != 'SWAT-RESERVE']
        temp_df = temp_df[temp_df.operator != 'GIGN-RESERVE']
        temp_df = temp_df[temp_df.operator != 'GSG9-RESERVE']
        temp_df = temp_df[temp_df.operator != 'SAS-RESERVE']
        temp_df = temp_df[temp_df.operator != 'SPETSNAZ-RESERVE']
        if rank_selected != "None":
            temp_df = temp_df.loc[(temp_df['skillrank'] == rank_selected)]
        if map_selected != "None":
            temp_df = temp_df.loc[(temp_df['mapname'] == map_selected)]
        if platform_selected != "None":
            temp_df = temp_df.loc[(temp_df['platform'] == platform_selected)]

        factor2 = [('operator'),('role')]
        temp_df = temp_df.groupby(factor2).sum()[["haswon", "count", "nbkills", "isdead"]].apply(lambda x: x).reset_index()
        temp_df['Kill'] = temp_df['nbkills'] / temp_df['count']
        temp_df['Dead'] = temp_df['isdead'] / temp_df['count']
        temp_df['Win Rate'] = temp_df['haswon'] / temp_df['count']
        totalnum = 0
        for each in temp_df['count']:
            totalnum += each
        temp_df['Presence'] = (temp_df['count'] / totalnum)*500

        Att_df = temp_df.loc[(temp_df['role'] == 'Attacker')]
        Def_df = temp_df.loc[(temp_df['role'] == 'Defender')]
        cur_role = ''
        cur_df = Att_df

        for index, row in temp_df.iterrows():
            if row['operator'] == operator_selected:
                cur_role = row['role']

        if cur_role == 'Defender':
            cur_df = Def_df


        #Win Rate Rank
        winRank_df = cur_df.groupby('operator').sum()[['Win Rate']].apply(lambda x: x).reset_index()
        winRank_df = winRank_df.sort_values('Win Rate')
        #Kill Rank    high to low
        killRank_df = cur_df.groupby('operator').sum()[['Kill']].apply(lambda x: x).reset_index()
        killRank_df = killRank_df.sort_values('Kill')
        #dead Rank
        deadRank_df = cur_df.groupby('operator').sum()[['Dead']].apply(lambda x: x).reset_index()
        deadRank_df = deadRank_df.sort_values('Dead', ascending=False)
        #Popularity Rank   high to low
        popularity_df = cur_df.groupby('operator').sum()[['Presence']].apply(lambda x: x).reset_index()
        popularity_df = popularity_df.sort_values('Presence')

        #Calculate score for each element

        kill_rank = 0
        for index, row in killRank_df.iterrows():
            kill_rank += 1
            if row['operator'] == operator_selected:
                break


        dead_rank = 0
        for index, row in deadRank_df.iterrows():
            dead_rank += 1
            if row['operator'] == operator_selected:
                break


        win_rank = 0
        for index, row in winRank_df.iterrows():
            win_rank += 1
            if row['operator'] == operator_selected:
                break


        popularity_rank = 0
        for index, row in popularity_df.iterrows():
            popularity_rank += 1
            if row['operator'] == operator_selected:
                break

        #score
        kill_score = kill_rank/3
        dead_score = dead_rank/3
        win_score = win_rank/3
        popularity_score = popularity_rank/3
        print("there is test for score: \n")
        print(kill_score, dead_score,win_score,popularity_score)


        #generate graph


        test_df = pd.DataFrame(dict(
            r=[win_score, kill_score, popularity_score, dead_score],
            theta=['Win Rate', 'Kill', 'Popularity',
                   'Survive']))
        fig77 = px.line_polar(test_df, r='r', theta='theta', line_close=True)
        fig77.update_traces(fill='toself')
        fig77.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=False
        )
        return fig77
    else:
        test_df = pd.DataFrame(dict(
            r=[0, 0, 0, 0],
            theta=['Win Rate', 'Kill', 'Popularity',
                   'Survive']))
        fig77 = px.line_polar(test_df, r='r', theta='theta', line_close=True)
        fig77.update_traces(fill='toself')
        fig77.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=False
        )
        return fig77