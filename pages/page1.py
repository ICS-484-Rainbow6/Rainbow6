
import pandas as pd

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
    ], className='row'),
    html.Div([html.Img(id='wp_plot', src='', style={
        'height': '50%',
        'width': '50%'
    })],
             id='plot_div', style={'textAlign': 'center'}),
    html.Div(id='tier_list', className='row')
],  className='ten columns offset-by-one')


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
    wdf = dff.groupby(factor).sum()[["haswon", "count"]].apply(lambda x:x).reset_index()
    wdf["windelta"] = (wdf["haswon"] / wdf["count"] - 0.5) * 100


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
    ax.set_xlabel('Presence (in %)')
    ax.set_ylabel('WinDelta (in %)')
    fig.set_size_inches(10, 10, forward=True)
    plt.axhline(0, color='red')
    plt.axvline(30, color='red')
    for x0, y0, path in zip(x, y,paths):
        ab = AnnotationBbox(OffsetImage(Image.open('png/' + path + '.png').resize((32,32))), (x0, y0), frameon=False)
        ax.add_artist(ab)
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

    #generate html component
    return html.Div([
        html.Div([
            html.Div([
                html.H6('S', className='half column', style={'background': '#ff6a6a','padding-top': '20px', 'padding-bottom':'20px', 'text-align': 'center'}),
            ], className='row', style={'background': '#11212b'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom':'5px', 'padding-left':'5px'}),
        html.Div([
            html.Div([
                html.H6('A', className='half column',
                        style={'background': '#ffb977', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.P("lalal")
            ], className='row', style={'background': '#11212b'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'}),
        html.Div([
            html.Div([
                html.H6('B', className='half column',
                        style={'background': '#ffdd79', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.P("lalal")
            ], className='row', style={'background': '#11212b'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'}),
        html.Div([
            html.Div([
                html.H6('C', className='half column',
                        style={'background': '#feff7c', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.P("lalal")
            ], className='row', style={'background': '#11212b'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'}),
        html.Div([
            html.Div([
                html.H6('D', className='half column',
                        style={'background': '#b5ff7b', 'padding-top': '20px', 'padding-bottom': '20px',
                               'text-align': 'center'}),
                html.P("lalal")
            ], className='row', style={'background': '#11212b'}),
        ], className='row', style={'padding-top': '5px', 'padding-bottom': '5px', 'padding-left': '5px'})
    ],  className='row', style={'background': '#0f1d26'})
