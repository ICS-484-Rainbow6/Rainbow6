# Load DataFrame
import pandas as pd

group = ["gamemode", "mapname", "skillrank", "operator", "platform", "secondarygadget", "primaryweapon", "secondaryweapon"]
number = ["haswon","nbkills", "isdead", "count"]

# Empty dataframe
df_file = pd.DataFrame(columns = group + number)

for df in pd.read_csv("r6.csv", chunksize=4000000, encoding='unicode_escape',delimiter=';'):
        
    # get a matchid & roundnumber dataframe or rounds with exactly 10 players
    round_df = df.groupby(["matchid", "roundnumber"]).count().apply(lambda x:x).reset_index()
    round_df = round_df[round_df["platform"] == 10]
    round_df = round_df[["matchid", "roundnumber"]]

    df = pd.merge(round_df, df, on=["matchid", "roundnumber"], how='inner')


    # get the summation form of all needed data
    def getMode(x):
        return x.split(' ')[2].strip()

    sdf = df.groupby(group).sum()[["haswon","nbkills", "isdead"]].apply(lambda x:x).reset_index()
    cdf = df.groupby(group).count()["endroundreason"].apply(lambda x:x).reset_index()
    sdf["count"] = cdf["endroundreason"]
    sdf["gamemode"] = sdf["gamemode"].apply(lambda x: getMode(x))
    print(df_file.shape)
    df_file = pd.concat([df_file, sdf])

# sum up and output
df_file = df_file.groupby(group).sum()[number].apply(lambda x:x).reset_index()
df_file.to_csv("result.csv")
df_file.shape