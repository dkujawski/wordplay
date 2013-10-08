#!/usr/bin/env python

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	logger.addHandler(ch)

	logger.info("this is a test harness.")
	#print isPalindrome("ABBA")
	#print isPalindrome("ABCBA")
	#print isPalindrome("DAVE")
	
	#print findLargest("ABBAXYZZYX")

	tmp_values_01 = [[ 'I', 'T', 'N', 'D', 'O' ],
				 	 [ 'S', 'A', 'K', 'X', 'N' ],
				     [ 'L', 'B', 'Z', 'M', 'E' ],
				  	 [ 'P', 'E', 'L', 'M', 'E' ],
				  	 [ 'O', 'P', 'L', 'S', 'T' ]]
	
	tmp_values_02 = [[ 'I', 'T', 'N', 'D' ],
				  	 [ 'S', 'A', 'K', 'X' ],
				     [ 'L', 'B', 'Z', 'M' ],
				  	 [ 'P', 'E', 'L', 'M' ]]

	tmp_values_03 = [[ 'I', 'T', 'N' ],
				  	 [ 'S', 'A', 'K' ],
				     [ 'L', 'B', 'Z' ]]

	tmp_values_04 = [[ 'I', 'T' ],
				  	 [ 'S', 'A' ]]

	from src import locate2d
	from src import render
	import pylab as p
	import networkx as nx

	node_graph = locate2d.build_graph(tmp_values_03)
	print len(node_graph.nodes()), len(node_graph.edges())	
	render.draw_traverse(node_graph)

	#found_words = locate2d.find_larger_words(tmp_values_02)
	#print len(found_words), found_words
	