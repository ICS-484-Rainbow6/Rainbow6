import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('HomePage'),
        dcc.Dropdown(
        id='app-3-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-3-display-value'),
    dcc.Link('Go to page 1', href='/pages/page1')
])


@app.callback(
    Output('app-3-display-value', 'children'),
    Input('app-3-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)

