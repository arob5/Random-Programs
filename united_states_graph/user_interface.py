#
# user_interface.py
# A simple interface to search for shortest paths between two states
# Last Modified: 8/17/2017
# Modified By: Andrew Roberts
#

import pandas as pd
import numpy as np
import search_algs

# TODO - catch exception when trying to make a path to Hawaii/Alaska
def main():
	START = "Illinois"
	state_df = pd.read_pickle("state_df.pickle")
	#search_algs.shortest_path_bfs(state_df, START)
	#search_algs.shortest_path_wrapper(state_df, START, "New Hampshire")

	search_algs.path_exists(state_df, "Illinois", "New Hampshire")	
	

main()
