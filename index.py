import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from pages import page1, page2, page3, page4, homepage



app.layout = html.Div([
    html.Div([
        html.Nav([
            html.A(
                html.Img(src=app.get_asset_url('logo4.png'), style={'height': '80px', 'padding-left': '30px'}),
                href='/pages/homepage'
            ),
            html.Ul([
                html.Li([
                    html.A('Page1', href='/pages/page1'),
                    html.A('Page2', href='/pages/page2'),
                    html.A('Page3', href='/pages/page3'),
                    html.A('Page4', href='/pages/page4'),
                    html.A('About', href='#')
                ])
            ])
        ])
    ]),
    dcc.Location(id='url', refresh=False),

    html.Div(id='page-content'),

])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/page1':
        return page1.layout
    elif pathname == '/pages/page2':
        return page1.layout
    elif pathname == '/pages/page3':
        return page3.layout
    elif pathname == '/pages/page4':
        return page4.layout
    elif pathname == '/pages/homepage':
        return homepage.layout
    else:
        return

if __name__ == '__main__':
    app.run_server(debug=True)
