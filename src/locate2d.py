"""
.. sectionauthor:: Dave Kujawski

Here are a few functions for processing a 2 dimensional array or a set of
nested lists like::

	array_2d = [['A','B','C'],
				['D','E','F'],
				['G','H','I'],]

This module uses the :class:`node.Node` class.

"""

from node import Node

def build_graph(array_2d, pos=(0,0), nodes=None):
	"""
	Using the values from the :param:`array_2d` buid a graph/tree data 
	structure and build a dict containing a :class:`node.Node` for each element 
	of :param:`array_2d`.  This uses the :meth:`get_neighbors` to build node 
	edges for the graph.

	:param array_2d: A list of lists containing strings. 
	:param pos: This is an internal parameter used in the recursive calls
		to know which element of the :param:`array_2d` to start processing 
		next.
	:param nodes: This is a dict of :class:`node.Node` objects used internally
		to keep track of which elements have already been processed and to 
		prevent infinite loops in the recursion.  It takes the form::

			{(x,y):node.Node, ...}

		It is also an opportunity to get a list containing a :class:`node.Node` 
		for each element in the :param:`array_2d` when an initialized dict is 
		passed in.

	"""
	if nodes is None:
		nodes = dict()
	x,y = pos
	if pos in nodes:
		# if the node has already be built, reuse it
		# no need for duplicate objects
		node = nodes[pos]
	else:
		# this is the first time visiting this element
		# create a node and add it to the dict.
		value = array_2d[x][y]
		node = Node(value, pos)
		nodes[pos] = node
	# go get the neighbors, these are edges in the graph
	neighbors = get_neighbors(nodes, array_2d, pos)
	# visit each neighbor to ensure it is a valid edge.
	for neighbor in neighbors:
		if neighbor in node.neighbors:
			# we have already have this edge
			continue
		node.neighbors.append(neighbor)
		if node in neighbor.neighbors:
			# avoid infinite loops, we are an edge of this neighbor
			continue
		else:
			# recurse
			build_graph(array_2d, neighbor.address, nodes)

def get_neighbors(nodes, array_2d, root_pos):
	""" 
	Starting from the element at :param:`root_pos` find all adjacent elements
	in the :param:`array_2d`, create a :class:`node.Node` for each, add them to 
	the :param:`nodes` dict and return a list which represent edges between the
	:param:`root_pos` node.

	:param nodes: This is the passed by ref nodes dict from :meth:`build_graph`.  
		This is passed in to avoid creating dupliecate :class:`node.Node` 
		objects.  If they already exist in the :param:`nodes` dict we will
		resuse them.
	:param array_2d: This is the list of lists passed in from 
		:meth:`build_graph` to search for neighbors.
	:param root_pos: This is the element (x,y) that we are using as the point
		of origin to search for valid edges.
	:returns: List of :class:`node.Node` objects that are adjacent to the 
		:param:`root_pos` in the :param:`array_2d` lists.

	"""
	x,y = root_pos	
	# build address search map
	addresses = ((x-1,y), (x+1,y),
				 (x,y-1), (x,y+1),
				 (x+1,y-1), (x+1,y+1),
				 (x-1,y-1), (x-1,y+1))
	neighbors = list()
	for pos in addresses:
		_x,_y = pos
		if _x < 0 or _y < 0:
			# pass on negative coords
			continue
		if pos in nodes:
			# if a node.Node already exists use it
			node = nodes[pos]
		else:
			try:
				value = array_2d[_x][_y]
			except IndexError as ie:
				# pass on any values outside of array bounds.
				continue
			node = Node(value, pos)
			# new nodes get added to the nodes dict for use later
			nodes[pos] = node
		# collect edges
		neighbors.append(node)
	return neighbors


def find_larger_words(array_2d, min_len=3):
	""" generate list of larger words with 3 chars or more found in the set
	"""
	import dictionary # load up the dictionary
	dictionary.load_dict(min_len)

	nodes = dict()
	build_graph(array_2d, nodes=nodes)
	results = list()
	for pos, node in nodes.items():
		results.extend(node.traverse(func=dictionary.is_word))
	return results
	