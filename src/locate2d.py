"""
.. sectionauthor:: Dave Kujawski

Here are a few functions for processing a 2 dimensional array or a set of
nested lists like::

	array_2d = [['A','B','C'],
				['D','E','F'],
				['G','H','I'],]

This module uses the :class:`node.Node` class.

"""
from networkx.algorithms import simple_paths as nxasp
import networkx as nx

from profilehooks import profile

#@profile
def build_graph(array_2d):
	"""
	Using the values from the :param:`array_2d` buid a graph/tree data .  
	This uses the :meth:`get_neighbors` to build node  edges for the graph.

	:param array_2d: A list of lists containing strings. 
	"""
	nx_graph = nx.DiGraph()
	for x, values in enumerate(array_2d):
		for y, value in enumerate(values):
			pos = (x,y)
			if not nx_graph.has_node(pos):
				nx_graph.add_node(pos, value=value)
			# go get the neighbors, these are edges in the graph
			neighbors = get_neighbors(array_2d, pos)
			for neighbor in neighbors:
				if not nx_graph.has_node(neighbor):
					_x,_y = neighbor
					nx_graph.add_node(neighbor, value=array_2d[_x][_y])
				if not nx_graph.has_edge(pos, neighbor):
					nx_graph.add_edge(pos, neighbor)
	return nx_graph

#@profile
def get_neighbors(array_2d, root_pos):
	""" 
	Starting from the element at :param:`root_pos` find all adjacent elements
	in the :param:`array_2d`, create a :class:`node.Node` for each, add them to 
	the :param:`nodes` dict and return a list which represent edges between the
	:param:`root_pos` node.

	:param array_2d: This is the list of lists passed in from 
		:meth:`build_graph` to search for neighbors.
	:param root_pos: This is the element (x,y) that we are using as the point
		of origin to search for valid edges.
	:returns: List of (x,y) tuples that are adjacent to the 
		:param:`root_pos` in the :param:`array_2d` lists.

	"""
	x,y = root_pos
	# build address search map
	addresses = ((x-1,y), (x+1,y),		# horiz
				 (x,y-1), (x,y+1),		# vert
				 (x+1,y-1), (x+1,y+1),	# right corners
				 (x-1,y-1), (x-1,y+1))	# left corners
	neighbors = list()
	for pos in addresses:
		_x,_y = pos
		if _x < 0 or _y < 0:
			# pass on negative coords
			continue
		try:
			_v = array_2d[_x][_y]
		except IndexError as ie:
			# pass on any values outside of array bounds.
			continue
		neighbors.append(pos)
	return neighbors

#@profile
def traverse(graph):
	"""
	Use the :networkx.algorithms.simple_paths:`all_simple_paths` function to 
	traverse the graph across all combinations of possible source to targets.
	O(n!)

	"""
	value = nx.get_node_attributes(graph, 'value')
	func = nxasp.all_simple_paths
	results = list()
	for src_node in graph.nodes():
		for tgt_node in graph.nodes():
			if src_node is tgt_node:
				continue
			for path in func(graph, src_node, tgt_node):
				char_str = ''.join([value[n] for n in path])
				if char_str:
					results.append(char_str)
	return results

@profile
def find_larger_words(array_2d, min_len=3):
	""" 
	This is the main entry point into what could be a game.  This will build up
	a word list using :module:`dictionary` and search through all possible
	string combinations in :param:`array_2d` and return a list of all words of
	at least :param:`min_len` in length.

	:param array_2d: This is the set of letters in the form of a 2 dimensional
		array, or list of lists of the form::

				array_2d = [['A','B','C'],
							['D','E','F'],
							['G','H','I'],]
	:param min_len: Minimum lenghth of words set in the word list built by 
		:module:`dictionary`
	:returns: list of words found.

	"""
	import dictionary 
	# load up the dictionary
	dictionary.load_dict(min_len)
	
	node_graph = build_graph(array_2d)

	results = list()
	for path in traverse(node_graph):
		if dictionary.is_word(path):
			results.append(path)
	return results
	