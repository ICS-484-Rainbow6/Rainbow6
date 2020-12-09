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

    ], style={'font-size': '150%', 'margin-left': '10%', 'margin-right': '10%'}),


    html.Div([
        html.Div('.', className='two columns'),
        # page 1
        html.Div([
            html.Div([
                html.P('Page 1', style={'background':'#333333', 'color':'white', 'text-align':'center', 'padding-top': '1%', 'padding-bottom': '1%'}),
            ], className='row', style={'background':'white'}),
            html.Div([
                html.Div([
                    html.H3('Overall Intensity', style={'font-family': 'sans-serif', 'font-weight': '500'}),
                    html.P('See the Operator Tier List in the current season and get basic understanding about each operator in the version.'),
                    html.A('See Details ...', href='/pages/page1', className='button',
                           style={'margin': '18px', 'color': 'white', 'background':'#4462a8'})
                ], style={'padding-left': '20px'})
            ], className='row', style={'background':'#ffffff', 'color': 'black', 'padding-top': '1px'})
        ], className='three columns'),

        html.Div('.', className='two columns'),
        # page 2
        html.Div([
            html.Div([
                html.P('Page 2', style={'background':'#333333', 'color':'white', 'text-align':'center', 'padding-top': '1%', 'padding-bottom': '1%'}),
            ], className='row', style={'background':'white'}),
            html.Div([
                html.Div([
                    html.H3('Popular Teams', style={'font-family': 'sans-serif', 'font-weight': '500'}),
                    html.P('See the most popular team in this season, and find the best team with high win rate for you and your friends.'),
                    html.A('See Details ...', href='/pages/page2', className='button',
                           style={'margin': '18px', 'color': 'white', 'background': '#4462a8'})

                ], style={'padding-left': '20px'})
            ], className='row', style={'background':'#ffffff', 'color': 'black', 'padding-top': '1px'})
        ], className='three columns'),
        html.Div('`', className='two columns'),


    ], className='row', style={'background': '#8b8471', 'padding-top': '40px'}),

    html.Div([

        html.Div('.', className='two columns'),
        # page 3
        html.Div([
            html.Div([
                html.P('Page 3',
                       style={'background': '#333333', 'color': 'white', 'text-align': 'center', 'padding-top': '1%',
                              'padding-bottom': '1%'}),
            ], className='row', style={'background': 'white'}),
            html.Div([
                html.Div([
                    html.H3('Operator Details', style={'font-family': 'sans-serif', 'font-weight': '500'}),
                    html.P('Explore details deeply for your favorite Operators, and understand their power and weakness.'),
                    html.A('See Details ...', href='/pages/page3', className='button',
                           style={'margin': '18px', 'color': 'white', 'background': '#4462a8'})
                ], style={'padding-left': '20px'})
            ], className='row', style={'background': '#ffffff', 'color': 'black', 'padding-top': '1px'})
        ], className='three columns'),

        html.Div('.', className='two columns'),

        # page 4
        html.Div([
            html.Div([
                html.P('Page 4',
                       style={'background': '#333333', 'color': 'white', 'text-align': 'center', 'padding-top': '1%',
                              'padding-bottom': '1%'}),
            ], className='row', style={'background': 'white'}),
            html.Div([
                html.Div([
                    html.H3('More ...', style={'font-family': 'sans-serif', 'font-weight': '500'}),
                    html.P('More interesting facts you can find about the game that they have influence to your win rate.'),
                    html.A('See Details ...', href='/pages/page4', className='button',
                           style={'margin': '18px', 'color': 'white', 'background': '#4462a8'})
                ], style={'padding-left': '20px'})
            ], className='row', style={'background': '#ffffff', 'color': 'black', 'padding-top': '1px'}),
        ], className='three columns'),

        html.Div('.', className='two columns'),

    ], className='row', style={'background': '#8b8471', 'padding-top': '20px', 'padding-bottom': '40px'})
], style={'background': 'rgba(255, 255, 255, 0.9)'})
