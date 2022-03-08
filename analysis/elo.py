def get_elo(team, opponent):
    return 1 / (1 + 10 ** ((opponent - team) / 400))

def initialise_elo(df):

    # create df columns
    df['home_pre_elo'] = 0
    df['home_post_elo'] = 0
    df['away_pre_elo'] = 0
    df['away_post_elo'] = 0

    # find first match for each team and initialise to 1500
    teams = (df['hteam'].append(df['ateam'])).unique()
    for team in teams:
        
