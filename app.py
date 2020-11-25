import dash
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server
df = pd.read_csv("s1.csv")
