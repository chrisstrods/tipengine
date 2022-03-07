
from os.path import dirname, abspath
import pandas as pd


def load():
    d = dirname(dirname(abspath(__file__)))
    results = pd.read_csv(d+'/data/results.csv', low_memory=False)
    odds = pd.read_csv(d+'/data/odds_full.csv', low_memory=False)
    player_stats = pd.read_csv(d+'/data/playerstats.csv', low_memory=False)
    player_details = pd.read_csv(d+'/data/playerdetails.csv', low_memory=False)

    return results, odds, player_stats, player_details


def main():
    results, fixtures, odds, player_details, player_stats = load()


if __name__ == "__main__":
    main()
