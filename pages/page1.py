
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

    html.Div([html.Img(id='wp_plot', src='', style={
        'height': '40%',
        'width': '60%',
        'padding-top': '20px',
        'padding-left': '10px',
        'padding-bottom': '16px',
    }, className='eight columns'),
              html.Div([
                  html.H6('Win Delta:', style={'fontWeight': 'bold', 'color': 'white'}),
                  html.P('The win rate of an operator minus the average win rate of the operator\'s role (Attacker or Defender). ', style={'fontWeight': 'bold', 'color': 'white'}),
                  html.H6('Presence:', style={'fontWeight': 'bold', 'color': 'white'}),
                  html.P('The presence rate of an operator in a round. The average presence rate of an operator is around 30%. ', style={'fontWeight': 'bold', 'color': 'white'}),
                  html.H6('Four Quadrants:', style={'fontWeight': 'bold', 'color': 'white'}),
                  html.P('Based on the the win delta rate and the presence rate, most operators are close to the origin. '
                         'Game designers should pay attention to the outliers. Tachanka may need a rework based on his performance', style={'fontWeight': 'bold', 'color': 'white'})
              ], className='five columns', style={'padding-left':'5px', 'padding-top': '15px'})
              ], className='row', style={'background': '#2b2b2b'}),


    html.Div(id='tier_list', className='row', style={'padding-top': '30px'}),

],  className='ten columns offset-by-one', style={'opacity': '0.955'})


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





    # windelta df
    factor = ["operator"]
    adf = dff.groupby("role").sum()[["haswon", "count"]].apply(lambda x:x).reset_index()
    adf["avrwinrate"] = adf["haswon"] / adf["count"]
    adf = adf[["role", "avrwinrate"]]

    wdf = dff.groupby(["role", "operator"]).sum()[["haswon", "count"]].apply(lambda x:x).reset_index()
    wdf = pd.merge(wdf, adf, on="role", how='outer')
    wdf["windelta"] = (wdf["haswon"] / wdf["count"] - wdf["avrwinrate"]) * 100


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
    ax.set_xlabel('Presence (in %)', size=20)
    ax.set_ylabel('WinDelta (in %)', size=20)
    fig.set_size_inches(10, 10, forward=True)
    plt.axhline(0, color='red')
    plt.axvline(30, color='red')
    for x0, y0, path in zip(x, y,paths):
        ab = AnnotationBbox(OffsetImage(Image.open('assets/' + path + '.png').resize((32,32))), (x0, y0), frameon=False)
        ax.add_artist(ab)
    ax.text(10, -2, "Underpicked\nToo Weak", ha="center", va="center", size=20, color="green", alpha=0.5)
    ax.text(10, 2, "Underpicked\nToo Strong", ha="center", va="center", size=20, color="orange", alpha=0.5)
    ax.text(50, -2, "Overpicked\nToo Weak", ha="center", va="center", size=20, color="blue", alpha=0.5)
    ax.text(50, 2, "Overpicked\nToo Strong", ha="center", va="center", size=20, color="red", alpha=0.5)
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
@app.callback(
    Output(component_id='tier_list', component_property='children'),
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='skillrank_select', component_property='value'),
     Input(component_id='gamemode_select', component_property='value'),
     Input(component_id='role_select', component_property='value')]
)
def generate_tierList(platform, skillrank, gamemode, role):
    temp_df = df.copy()
    if platform != "All":
        temp_df = temp_df[temp_df["platform"] == platform]

    if skillrank == "Copper & Bronze":
        temp_df = temp_df[(temp_df["skillrank"] == "Copper") | (temp_df["skillrank"] == "Bronze")]
    if skillrank == "Silver & Gold":
        temp_df = temp_df[(temp_df["skillrank"] == "Silver") | (temp_df["skillrank"] == "Gold")]
    if skillrank == "Platinum+":
        temp_df = temp_df[(temp_df["skillrank"] == "Platinum") | (temp_df["skillrank"] == "Diamond")]

    if gamemode != "All":
        temp_df = temp_df[temp_df["gamemode"] == gamemode]

    if role != "All":
        temp_df = temp_df[temp_df["role"] == role]

    factor2 = [('operator'), ('role')]
    temp_df = temp_df.groupby(factor2).sum()[["haswon", "count", "nbkills", "isdead"]].apply(lambda x: x).reset_index()
    temp_df['Kill'] = temp_df['nbkills'] / temp_df['count']
    temp_df['Dead'] = temp_df['isdead'] / temp_df['count']
    temp_df['Win Rate'] = temp_df['haswon'] / temp_df['count']
    totalnum = 0
    for each in temp_df['count']:
        totalnum += each
    temp_df['Presence'] = (temp_df['count'] / totalnum) * 500
    temp_df = temp_df[temp_df.operator != 'SWAT-RESERVE']
    temp_df = temp_df[temp_df.operator != 'GIGN-RESERVE']
    temp_df = temp_df[temp_df.operator != 'GSG9-RESERVE']
    temp_df = temp_df[temp_df.operator != 'SAS-RESERVE']
    temp_df = temp_df[temp_df.operator != 'SPETSNAZ-RESERVE']

    # Win Rate Rank
    winRank_df = temp_df.groupby('operator').sum()[['Win Rate']].apply(lambda x: x).reset_index()
    winRank_df = winRank_df.sort_values('Win Rate')
    # Kill Rank    high to low
    killRank_df = temp_df.groupby('operator').sum()[['Kill']].apply(lambda x: x).reset_index()
    killRank_df = killRank_df.sort_values('Kill')
    # dead Rank
    deadRank_df = temp_df.groupby('operator').sum()[['Dead']].apply(lambda x: x).reset_index()
    deadRank_df = deadRank_df.sort_values('Dead', ascending=False)
    # Popularity Rank   high to low
    popularity_df = temp_df.groupby('operator').sum()[['Presence']].apply(lambda x: x).reset_index()
    popularity_df = popularity_df.sort_values('Presence')

    #generate the score list, the index of the list will be represented operator
    size_tem = temp_df['operator'].size
    score_win = []
    score_kill = []
    score_dead = []
    score_popularity = []
    score_total = []
    for a in range(0, size_tem):
        score_win.append(0)
        score_kill.append(0)
        score_dead.append(0)
        score_popularity.append(0)
        score_total.append(0)
    temp_score = 0
    for index, row in winRank_df.iterrows():
        temp_score += 1
        score_win[index] = temp_score

    temp_score = 0
    for index, row in killRank_df.iterrows():
        temp_score += 1
        score_kill[index] = temp_score

    temp_score = 0
    for index, row in deadRank_df.iterrows():
        temp_score += 1
        score_dead[index] = temp_score

    temp_score = 0
    for index, row in popularity_df.iterrows():
        temp_score += 1
        score_popularity[index] = temp_score

    num_div = 6
    if size_tem == 15:
        num_div = 3

    for a, item in enumerate(score_total):
        score_total[a] = (score_win[a] + score_kill[a] + score_dead[a] + score_popularity[a]) / num_div

    temp_df['score'] = score_total
    temp_df['rank'] = np.ceil(temp_df['score'] / 4)

    rank_df = temp_df.reset_index()[["operator", "rank"]]

    rankS_df = rank_df[rank_df["rank"] == 5]
    rankA_df = rank_df[rank_df["rank"] == 4]
    rankB_df = rank_df[rank_df["rank"] == 3]
    rankC_df = rank_df[rank_df["rank"] == 2]
    rankD_df = rank_df[rank_df["rank"] == 1]

    rankS = []
    rankA = []
    rankB = []
    rankC = []
    rankD = []

    def getImage(op):
        path = 'assets/' + op + '.png'
        encoded_image = base64.b64encode(open(path, 'rb').read())
        link = "https://www.ubisoft.com/en-us/game/rainbow-six/siege/game-info/operators/" + op.split('-')[1].lower()

        str = html.A([html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), className='opImage')],
                     href=link, target="_blank")
        return str

    for op in rankS_df["operator"]:
        rankS.append(getImage(op))

    for op in rankA_df["operator"]:
        rankA.append(getImage(op))

    for op in rankB_df["operator"]:
        rankB.append(getImage(op))

    for op in rankC_df["operator"]:
        rankC.append(getImage(op))

    for op in rankD_df["operator"]:
        rankD.append(getImage(op))

    #generate html component
    return html.Div([
        html.Div([
            html.H2('Tier Rank for Operators'),
            html.P('We rank Operators based on their scores.'),
            html.P("The scores is based on each operator's performance on Win Rate, Kill, Survive, Popularity."),
            html.P("Click on each operator's icon to see the official operator instruction page")
        ], className='row', style={'color': 'white', 'text-align': 'center'}),
        html.Div([
            html.Div([
                html.H6('S', className='half column',
                        style={'background': '#ff6a6a','padding-top': '20px', 'padding-bottom':'20px',
                               'text-align': 'center'}),
                html.Div(rankS, className='ranks')
            ], className='row', style={'background': '#323232'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom':'5px', 'padding-left':'5px'}),
        html.Div([
            html.Div([
                html.H6('A', className='half column',
                        style={'background': '#ffb977', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.Div(rankA, className='ranks')
            ], className='row', style={'background': '#323232'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'}),
        html.Div([
            html.Div([
                html.H6('B', className='half column',
                        style={'background': '#ffdd79', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.Div(rankB, className='ranks')
            ], className='row', style={'background': '#323232'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'}),
        html.Div([
            html.Div([
                html.H6('C', className='half column',
                        style={'background': '#feff7c', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.Div(rankC, className='ranks')
            ], className='row', style={'background': '#323232'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'}),
        html.Div([
            html.Div([
                html.H6('D', className='half column',
                        style={'background': '#b5ff7b', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.Div(rankD, className='ranks')
            ], className='row', style={'background': '#323232'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'})
    ],  className='row', style={'background': '#2b2b2b'})
