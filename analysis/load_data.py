
from os.path import dirname, abspath
import os, sys
import pandas as pd
sys.path.append(os.path.abspath(os.getcwd()))
from elo import initialise_elo

def load():
    results = pd.read_csv('../data/results.csv', low_memory=False)
    odds = pd.read_csv('../data/odds_full.csv', low_memory=False)
    player_stats = pd.read_csv('../data/playerstats.csv', low_memory=False)
    player_details = pd.read_csv('../data/playerdetails.csv', low_memory=False)

    #import elo from initialise_elo
    return results, odds, player_stats, player_details


def main():
    results, odds, player_stats, player_details = load()

    elo_results = initialise_elo(results)


if __name__ == "__main__":
    main()

#%%
