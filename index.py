import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from pages import page1, page2, page3


app.layout = html.Div([
    html.Div([
        html.Nav([
            html.Img(src=app.get_asset_url('logo4.png'), style={'height': '80px', 'padding-left': '30px'}),
            html.Ul([
                html.Li([
                    html.A('Home', href='index.html'),
                    html.A('Page1', href='/pages/page1'),
                    html.A('Page2', href='/pages/page2'),
                    html.A('Page3', href='/pages/page3'),
                    html.A('About', href='#')
                ])
            ])
        ])
    ]),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
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
    else:
        return html.Img(src=app.get_asset_url('bg2.jpg'))

if __name__ == '__main__':
    app.run_server(debug=True)
