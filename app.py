  
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

# test purpose, 1M rows only
for toprow in pd.read_csv("s1.csv", chunksize = 1000000):
    df = pd.DataFrame(columns = toprow.columns)
    break

print(toprow.iloc[0])


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Win Delta Per Operator VS Presence", style={'text-align': 'center'}),
    
    html.H3("Platform:"),   
    dcc.Dropdown(id="platform_select",
                 options=[
                     {"label": "All", "value": "None"},
                     {"label": "PC", "value": "PC"},
                     {"label": "PS4", "value": "PS4"},
                     {"label": "XONE", "value": "XONE"}],
                 multi=False,
                 value="None",
                 style={'width': "40%"}
                 ),
    
    html.H3("Role:"),
    dcc.Dropdown(id="role_select",
                 options=[
                     {"label": "Both", "value": "None"},
                     {"label": "Attacker", "value": "Attacker"},
                     {"label": "Defender", "value": "Defender"}],
                 multi=False,
                 value="None",
                 style={'width': "40%"}
                 ),
    

    html.Div(id='output_container', children=[]),
    dcc.Graph(id='windelta_figure', figure={})
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='windelta_figure', component_property='figure')],
    [Input(component_id='platform_select', component_property='value'),
     Input(component_id='role_select', component_property='value')]
)

def update_graph(platform, role):
    container = "The chose role was: {}".format(role)
    
    dff = toprow.copy()
    if platform != "None":
        dff = dff[dff["platform"] == platform]
    if role != "None":
        dff = dff[dff["role"] == role]
    
    rdf = dff.groupby(["operator"]).mean()["haswon"].apply(lambda x:x).reset_index()
    rdf.rename(columns={"haswon": "WinDelta"}, inplace=True)
    rdf["WinDelta"] = rdf["WinDelta"] - 0.5
    fig = px.bar(rdf, x="operator", y="WinDelta")
    
    
    
    return container, fig









# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)