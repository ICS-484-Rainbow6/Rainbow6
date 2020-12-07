import dash_core_components as dcc
import dash_html_components as html
from app import app
layout = html.Div([

    html.Div([
        html.H1("About Team", style={'font-family': 'Helvetica',
                                                             "margin-top": "0",
                                                             "margin-bottom": "0"}, className='eight columns'),
    ], className='row'),
    html.P("We are the Team 666 doing data visualization for the Video game Rainbow six siege."),
    html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('dandyy.png'), style={'height': '100%', 'width': '100%'})

        ], className='four columns', style={'margin-right': '20px', 'margin-left': '20px'}),
        html.Div([
            html.H3('Captain Dandy !', style={'font-family': 'sans-serif', 'line-height': '60%'}),
            html.P('I am a very long very long very very very long sentence'),
            html.P('Please put you personal information at here here here here...'),
            html.A([
                html.Img(src=app.get_asset_url('github.png'), style={'height': '11%', 'width': '11%'})
            ], href="#"),
            html.A([
                html.Img(src=app.get_asset_url('linkedin.png'), style={'height': '11%', 'width': '11%', 'margin-left':'10px'})
            ], href="#")
        ], className='six columns', style={})
    ], className='row'),
    ], className='seven columns', style={'background': 'rgba(43, 43, 43, 0.8)', 'padding-top': '20px', 'padding-bottom':'20px'}),

    html.Div([
    html.Div([
        html.Div([
            html.H3('Tianhui Zhou', style={'font-family': 'sans-serif', 'line-height': '60%'}),
            html.P('I am a very long very long very very very long sentence'),
            html.P('Please put you personal information at here here here here...'),
            html.A([
                html.Img(src=app.get_asset_url('github.png'), style={'height': '11%', 'width': '11%'})
            ], href='https://tianhuizhou.github.io/'),
            html.A([
                html.Img(src=app.get_asset_url('linkedin.png'),
                         style={'height': '11%', 'width': '11%', 'margin-left': '10px'})
            ], href="#")
        ], className='six columns', style={'margin-right': '20px', 'margin-left': '20px'}),
        html.Div([
            html.Img(src=app.get_asset_url('Bobbyy.png'), style={'height': '100%', 'width': '100%'})

        ], className='four columns')
    ], className='row')
    ], className='seven columns', style={'background': 'rgba(43, 43, 43, 0.8)', 'padding-top': '20px', 'padding-bottom':'20px', 'margin-left':'440px','margin-top':'20px'}),

    html.Div([
        html.Div([
            html.Div([
                html.Img(src=app.get_asset_url('mybad.png'), style={'height': '100%', 'width': '100%'})

            ], className='four columns', style={'margin-right': '20px', 'margin-left': '20px'}),
            html.Div([
                html.H3('Ray Tang', style={'font-family': 'sans-serif', 'line-height': '60%'}),
                html.P('Hi guys, I am Jui-Chen Tang, feel free to call me Ray. '),
                html.P('Currently I am UH student working on my second degree major in computer science focus on data science.'),
                html.A([
                    html.Img(src=app.get_asset_url('github.png'), style={'height': '11%', 'width': '11%'})
                ], href="https://github.com/mybad812/mybad812.github.io"),
                html.A([
                    html.Img(src=app.get_asset_url('linkedin.png'),
                             style={'height': '11%', 'width': '11%', 'margin-left': '10px'})
                ], href="#")
            ], className='six columns', style={})
        ], className='row'),
    ], className='seven columns',
        style={'background': 'rgba(43, 43, 43, 0.8)', 'padding-top': '20px', 'padding-bottom': '20px', 'margin-top':'20px'})

],  className='ten columns offset-by-one', style={'background': 'rgba(43, 43, 43, 0)', 'color': 'white'})
