import dash_html_components as html
from app import app

layout = html.Div([
    html.Div([
        #title
        html.H1('WELCOME TO R6 DATA ANALYSIS', style={'font-weight': 'bold'}),
    ], style={'margin-left': '15%', 'padding-top': '5%'}),
    html.Div([
        #title
        html.H1('HOW CAN WE HELP?', style={'font-weight': 'bold'}),
    ], style={'margin-left': '15%'}),

    html.Div([
        html.Div([
            html.A([
                html.Img(src=app.get_asset_url('ug_2.jpg'), style={'height': '60%', 'width': '80%'})
            ], href='#')
        ], className='three columns', style={'margin-left': '5%'}),
        html.Div([
            html.A([
                html.Img(src=app.get_asset_url('ug_2.jpg'), style={'height': '60%', 'width': '100%'})
            ], href='#')
        ], className='three columns'),
        html.Div([
            html.A([
                html.Img(src=app.get_asset_url('ug_1.jpg'), style={'height': '60%', 'width': '100%'})
            ], href='#')
        ], className='three columns'),
        html.Div([
            html.A([
                html.Img(src=app.get_asset_url('ug_1.jpg'), style={'height': '60%', 'width': '100%'})
            ], href='#')
        ], className='three columns'),
    ], className='row')
], style={'background': 'rgba(255, 255, 255, 0.9)'})
