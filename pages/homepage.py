import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.Div([
        html.H2('DATA ', style={'font-family': 'sans-serif', 'line-height': '60%'}),
        html.H2('HELP YOU WIN', style={'font-family': 'sans-serif', 'line-height': '60%', 'padding-bottom': '20px'}),
        html.P('If you are a new player,', style={'font-weight': 'bold', 'font-size': 'large'}),
        html.P('No Worries, We got you back.'),
        html.P('Using our amazing tools to help you find appropriate Operators and Weapon combos.'),
        html.P('If you are already a master,', style={'font-weight': 'bold', 'font-size': 'large', 'padding-top':'15px'}),
        html.P('Let explore more details about the game by using our tools,'),
        html.P('and find more interesting ideas to punish your opponent in each game.'),

    ], style={'padding': '25px'}),
    html.A('User Guide', href='/pages/page1', className='button', style={'margin': '18px', 'color': 'white'})
], className='four columns',
    style={'background': 'rgba(43, 43, 43, 0.5)', 'color': 'white', 'margin-top': '200px', 'margin-left': '300px'})
