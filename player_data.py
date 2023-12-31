import pandas as pd
import numpy as np


def read_data():
    '''
    reads and slightly preprocesses to serve as helper function
    :return: the full dataset
    '''
    # read
    df = pd.read_csv('data.csv')

    # remove empty cols
    df.drop(['Unnamed: 13', 'Unnamed: 18'], axis=1, inplace=True)

    return df


def top_player_stats(x, stat):
    '''
    Returns the top {x} results of the {stat} column for the 20222023 NHL season PER PLAYER.
    Call using http://127.0.0.1:8000/stats/player/top_{x}_{stat}
    '''
    df = read_data()

    # assert variables are valid
    assert x in range(1, len(df.index))
    assert stat in df.columns

    # query of top  stat obtainer, with all relevant col labels
    return df.sort_values(by=stat, ascending=False).iloc[:x]


def top_team_stats(x, stat):
    '''
    Returns the top {x} results of the {stat} column for the 20222023 NHL season PER TEAM.
    Call using http://127.0.0.1:8000/stats/team/top_{x}_{stat}
    '''
    df = read_data()
    # remove multi team players for simplicity. Will be handled later.
    df = df[~(df['Team'].str.contains('/', regex=False))]

    # assert variables are valid
    assert stat in df.columns
    assert x in range(1, len(df.groupby('Team').count().index)+1)

    # separate non_sum cols for grouping (i.e. avg or mult needed)
    non_sum = pd.DataFrame(df.pop(col) for col in ['S%', 'FOW%', 'SecPerGP', 'MinPerGP']).T
    non_sum['Team'] = df['Team']
    non_sum.replace("None", np.NaN, inplace=True)
    non_sum[['S%', 'FOW%']] = non_sum[['S%', 'FOW%']].astype(float)

    # drop useless fields for teams remaining (i.e. Plyaer ID)
    df.drop(['playerId', 'Shifts/GP', 'Pos', 'Season'], axis=1, inplace=True)

    # group
    df = df.groupby('Team').sum().reset_index()
    non_sum = non_sum.groupby('Team').mean(numeric_only=True).reset_index()
    non_sum = non_sum.round(3)

    # and combine...inner join on Team
    return_df = pd.merge(left=df, right=non_sum, how='inner', on='Team')

    # query of top  stat obtainer, with all relevant col labels
    return return_df.sort_values(by=stat, ascending=False).iloc[:x]

def team_roster(team):
    '''
    Current roster of the team including traded and acquired players
    :param team: team name
    :return: name and stats of roster players
    '''
    df = read_data()
    roster = df.loc[df['Team'].str.contains(team)]
    return roster

def most_travelled():
    '''
    :return: the player(s) who appears on the most teams in 2022-2023
    '''

    # read
    df = read_data()

    # copy team Series to split on / and find lengths
    to_split = df['Team']
    to_split = to_split.str.split('/')
    teams_played_for = to_split.str.len()

    # return and search original df in the indeces of where the values for the number of teams played for equals the max
    return df.loc[teams_played_for.loc[teams_played_for.values == teams_played_for.max()].index]