from node import Node

def build_graph(array_2d, pos=(0,0), nodes=None):
	if nodes is None:
		nodes = dict()
	x,y = pos
	if pos in nodes:
		node = nodes[pos]
	else:
		value = array_2d[x][y]
		node = Node(value, pos)
		nodes[pos] = node
	neighbors = get_neighbors(nodes, array_2d, pos)
	for neighbor in neighbors:
		if neighbor in node.neighbors:
			# we have already have this neighbor
			continue
		node.neighbors.append(neighbor)
		if node in neighbor.neighbors:
			# avoid infinite loops
			continue
		else:
			build_graph(array_2d, neighbor.address, nodes)

def get_neighbors(nodes, array_2d, root_pos):
	x,y = root_pos	
	# build address map
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
			node = nodes[pos]
		else:
			try:
				value = array_2d[_x][_y]
			except IndexError as ie:
				# pass on any values outside of array bounds.
				continue
			node = Node(value, pos)
			nodes[pos] = node
		neighbors.append(node)
	return neighbors


def find_larger_words(array_2d, min_len=3):
	""" generate list of larger words with 3 chars or more found in the set
	"""
	import dictionary # load up the dictionary
	dictionary.loadDict(min_len)

	nodes = dict()
	build_graph(array_2d, nodes=nodes)
	results = list()
	for pos, node in nodes.items():
		results.extend(node.traverse(func=dictionary.isWord))
	return results
	