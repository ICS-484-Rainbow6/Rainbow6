import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from pages import page1, page_test, homepage


app.layout = html.Div([
    html.H3('HomePage'),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/page1':
        return page1.layout
    elif pathname == '/pages/page_test':
        return page_test.layout
    else:
        return 'Welcome homepage'

if __name__ == '__main__':
    app.run_server(debug=True)
