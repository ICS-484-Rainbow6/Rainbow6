import dash
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# part of the 1G
# for df in pd.read_csv("s1.csv", chunksize = 4000000):
#     break
# print(df.shape)

# df = pd.read_csv("s1.csv")
