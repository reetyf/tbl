from fastapi import FastAPI
import player_data

app = FastAPI()

@app.get("/stats")
def read_stats():
    df = player_data.read_data().to_json(orient = 'records')
    return df

@app.get("/stats/player/top_{x}_{stat}")
def top_player_stats(x:int,stat:str):
    # FIX PROBLEM INTERACTIONS with URL
    if(stat == 'FOW'):
        stat = "FOW%"
    elif (stat == '+'):
        stat = "+/-"
    elif (stat == 'SP'):
        stat = "S%"
    df = player_data.top_player_stats(x,stat).to_json(orient = 'records')
    return df

@app.get("/stats/team/top_{x}_{stat}")
def top_team_stats(x:int,stat:str):
    # FIX PROBLEM INTERACTIONS with URL
    if(stat == 'FOW'):
        stat = "FOW%"
    elif (stat == '+'):
        stat = "+/-"
    elif (stat == 'SP'):
        stat = "S%"
    df = player_data.top_team_stats(x,stat).to_json(orient = 'records')
    return df

