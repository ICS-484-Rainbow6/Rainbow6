import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
#'font': '60px R6S-Light, sans-serif',
layout = html.Div([
    html.Div([
        html.H2('OPERATION NEON', style={'font-family': 'sans-serif', 'line-height': '60%'}),
        html.H2('DAWN', style={'font-family': 'sans-serif', 'line-height': '60%', 'padding-bottom': '20px'}),
        html.P('If you see a laser, be warned. Nighthaven was'),
        html.P('hiding her well, but not anymore. Operation Neon'),
        html.P('Dawn is welcoming a newcomer: Aruni. Don’t'),
        html.P('underestimate her. Her prosthetic arm and leg'),
        html.P('make her a fierce opponent.'),
    ], style={'padding': '25px'}),
    html.A('User Guide', href='/pages/page1', className='button', style={'margin': '25px', 'color': 'white'})
], className='four columns',
    style={'background': 'rgba(43, 43, 43, 0.5)', 'color': 'white', 'margin-top': '200px', 'margin-left': '300px'})

