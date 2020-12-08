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
    ], style={'margin-left': '15%', 'margin-bottom': '5%'}),

    html.Div([
        html.P("We are using the official Rainbow Six Siege data peek from Ubisoft. This dataset contains 31 attributes from more than 20 million ranked games."),
        html.P("We provide the most flexibility in each topic, you can either look the overall situation or check them based on your own desire."),
        html.P("All you need to do in each topic is:"),
        html.P("Select Parameters on several dropdown menu, and results will be automatically displayed.", style={'font-weight': 'bold'}),
        html.Hr(),

    ], className='nine columns', style={'font-size': '150%', 'margin-left': '10%'}),

    html.Div([
], style={'background': '#8b8471'}),


    html.Div([
        html.Div([
            html.A([
                html.Div([
                    html.P('hahahaha', style={'color': 'black'}),
                    html.P('hahahaha'),
                    html.P('hahahaha'),
                    html.P('hahahaha'),
                ])

            ], href='#')
        ], className='hah three columns', style={'margin-left': '5%'}),
        html.Div([
            html.A([
                html.Div([
                    html.P('hahahaha', style={'color': 'black'}),
                    html.P('hahahaha'),
                    html.P('hahahaha'),
                    html.P('hahahaha'),
                ])
            ], href='#')
        ], className='hah three columns'),
        html.Div([
            html.A([
                html.Img(src=app.get_asset_url('ug_5.png'), style={'height': '90%', 'width': '90%'})
            ], href='#')
        ], className='three columns'),
        html.Div([
            html.A([
                html.Img(src=app.get_asset_url('ug_3.png'), style={'height': '90%', 'width': '90%'})
            ], href='#')
        ], className='three columns'),
    ], className='row', style={'background': '#8b8471'})

], style={'background': 'rgba(255, 255, 255, 0.9)'})
