import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from pages import page1, page2, page3, page4, homepage, about, userguide



app.layout = html.Div([
    html.Div([
        html.Nav([
            html.A(
                html.Img(src=app.get_asset_url('logo4.png'), style={'height': '80px', 'padding-left': '30px'}),
                href='/pages/homepage'
            ),
            html.Ul([
                html.Li([
                    html.A('Overall', href='/pages/page1'),
                    html.A('Team', href='/pages/page2'),
                    html.A('Operator', href='/pages/page3'),
                    html.A('More', href='/pages/page4'),
                    html.A('About', href='/pages/about')
                ])
            ])
        ])
    ]),
    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content'),

    html.Div([
        html.Div([
            html.P('2020 Rainbow Six Siege Data Visualization'),
            html.P('Web Created by Team 666'),
            html.P('Power by Dash, Pandas, Plotly'),
            html.A([
                html.Img(src=app.get_asset_url('github.png'), style={'height': '3%', 'width': '3%'})
            ], href="https://github.com/ICS-484-Rainbow6/Rainbow6", target="_blank")
        ], className='two column offset-by-five.column',
            style={'text-align': 'center',
                   'background': 'rgba(28, 28, 28, 0.95)',
                   'margin-top': '250px', 'color': 'white', 'padding-top': '30px', 'padding-bottom': '20px'})
    ], className='row')

])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/page1':
        return page1.layout
    elif pathname == '/pages/page2':
        return page2.layout
    elif pathname == '/pages/page3':
        return page3.layout
    elif pathname == '/pages/page4':
        return page4.layout
    elif pathname == '/pages/homepage':
        return homepage.layout
    elif pathname == '/pages/about':
        return about.layout
    elif pathname == '/pages/userguide':
        return userguide.layout
    else:
        return homepage.layout

if __name__ == '__main__':
    app.run_server(debug=True)
