import numpy as np
import pandas as pd

'''
PARAMS
'''
ELO_BASE = 1500
K_FACTOR = 40


def update_score(home_pre, away_pre, result):

    if result == 1:
        home_win, away_win = 1, 0
    elif result == 0.5:
        home_win, away_win = 0.5, 0.5
    else:
        home_win, away_win = 0, 1

    home_expected = (1 / (1 + 10 ** ((away_pre - home_pre) / 400)))
    away_expected = (1 / (1 + 10 ** ((home_pre - away_pre) / 400)))

    home_new = round(home_pre + (K_FACTOR * (home_win - home_expected)))
    away_new = round(away_pre + (K_FACTOR * (away_win - away_expected)))

    return home_new, away_new



def get_winner(match):
    if match['hscore'] > match['ascore']:
        return 1
    elif match['hscore'] < match['ascore']:
        return 0
    else:
        return 0.5

def season_flatten(score):
    balance = score - 1500
    if balance > 0:
        return score - (balance * .1)
    elif balance < 0:
        return score - (balance * .1)

def initialise_elo(df):

    # create df columns
    df['home_pre_elo'] = 0
    df['home_post_elo'] = 0
    df['away_pre_elo'] = 0
    df['away_post_elo'] = 0

    # find first match for each team and initialise to 1500
    teams = (df['hteam'].append(df['ateam'])).unique()
    for team in teams:
        for index, row in df.iterrows():
            if row['hteam'] == team :
                df.at[index, 'home_pre_elo'] = ELO_BASE
                break
            elif row['ateam'] == team:
                df.at[index, 'away_pre_elo'] = ELO_BASE
                break


def calculate_elo(df):
    for index, row in df.iterrows():
        if row['home_pre_elo'] == 0:
            for x in reversed(range(0,index)):
                if df.at[x, 'hteam'] == row['hteam']:
                    df.at[index, 'home_pre_elo'] = df.at[x, 'home_post_elo']
                    break
                if df.at[x, 'ateam'] == row['hteam']:
                    df.at[index, 'home_pre_elo'] = df.at[x, 'away_post_elo']
                    break

        if(row['away_pre_elo']) == 0:
            for x in reversed(range(0,index)):
                if df.at[x, 'hteam'] == row['ateam']:
                    df.at[index, 'away_pre_elo'] = df.at[x, 'home_post_elo']
                    break
                if df.at[x, 'ateam'] == row['ateam']:
                    df.at[index, 'away_pre_elo'] = df.at[x, 'away_post_elo']
                    break

        if row['roundnumber'] == 1:
            df.at[index, 'home_pre_elo'] = df.at[index, 'home_pre_elo'] - ((df.at[index, 'home_pre_elo'] - 1500) * .1)
            df.at[index, 'away_pre_elo'] = df.at[index, 'away_pre_elo'] - ((df.at[index, 'away_pre_elo'] - 1500) * .1)

        df.at[index, 'home_post_elo'], df.at[index, 'away_post_elo'] = \
            update_score(df.at[index, 'home_pre_elo'], df.at[index, 'away_pre_elo'], get_winner(row))




