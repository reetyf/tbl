from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import player_data

app = FastAPI()

@app.get("/stats")
def read_stats():
    df = player_data.read_data()
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=nhl_com_stats.csv"})

@app.get("/stats/player/top_{x}_{stat}")
def top_player_stats(x:int,stat:str):
    # FIX PROBLEM INTERACTIONS with URL
    if(stat == 'FOW'):
        stat = "FOW%"
    elif (stat == '+'):
        stat = "+/-"
    elif (stat == 'SP'):
        stat = "S%"
    df = player_data.top_player_stats(x,stat)
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=top_{x}_{stat}_players_20222023.csv"})


@app.get("/stats/team/top_{x}_{stat}")
def top_team_stats(x:int,stat:str):
    # FIX PROBLEM INTERACTIONS with URL
    if(stat == 'FOW'):
        stat = "FOW%"
    elif (stat == '+'):
        stat = "+/-"
    elif (stat == 'SP'):
        stat = "S%"
    df = player_data.top_team_stats(x,stat)
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=top_{x}_{stat}_teams_20222023.csv"})

@app.get("/roster/{team}")
def team_roster(team:str):
    df = player_data.team_roster(team)
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={team}_roster_20222023.csv"})


@app.get("/multi_team_player")
def most_travelled_player():
    df = player_data.most_travelled()
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=most_travelled_player.csv"})