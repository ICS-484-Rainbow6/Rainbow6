import dash_core_components as dcc
import dash_html_components as html


from app import app
#'font': '60px R6S-Light, sans-serif',
layout = html.Div([

    html.Div([
        html.H1("About Us", style={'font-family': 'Helvetica',
                                                             "margin-top": "25",
                                                             "margin-bottom": "0"}, className='eight columns'),
    ], className='row'),
    html.P("I don't know what to say but we have to say something here.")
],  className='ten columns offset-by-one', style={'opacity': '0.955'})
