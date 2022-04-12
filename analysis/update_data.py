import sys
import os
sys.path.append(os.path.abspath(os.getcwd()))
from load_data import load
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

# Make this false unless you're running it for the first time
INSTALL_FITZROY = False

if INSTALL_FITZROY:
    utils = importr("utils")
    install = utils.install_packages
    install("fitzRoy")

fitzroy = importr("fitzRoy")

# Load existing data files
results, odds, player_details, player_stats = load()

new_results = fitzroy.get_fryzigg_stats(start = 2022, end = 2022)



