import dash
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

df = pd.read_csv("result.csv")
combodf = pd.read_csv("combo.csv")
weapondf = pd.read_csv("result_weapon.csv")
