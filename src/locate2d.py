
class Resident(object):
	def __init__(self, value, address, prev=None):
		self.prev = prev
		self.value = value
		self.address = address
		self.neighbors = list()

	def traverse(self, func=None, results_ref=None, trail=None, history=None):
		""" walk the tree building a string characters from each 
		value.
		"""
		if results_ref is None:
			results_ref = list()

		if history is None:
			history = list()
		history.append(self.address)

		if trail is None:
			trail = list()
		trail.append(self.value)
		
		for neighbor in self.neighbors:
			if neighbor.address in history:
				continue
			# recurse for all neighbors
			results_ref = neighbor.traverse(func, results_ref, 
											list(trail), list(history))
		trail_str = ''.join(trail)
	   	if not results_ref or not results_ref[-1].startswith(trail_str):
			if func is None or func(trail_str):
				# add all trails to results
				results_ref.append(trail_str)
		return results_ref

	def walk(self, func=None, history=None):		
		if not history:
			history = set()
		history.add(self.address)
		#print self.value, history
		results = self.traverse(func)
		for neighbor in self.neighbors:
			if neighbor.address in history:
				continue
			results.extend(neighbor.walk(func, history))
		return results

	def getHistory(self):
		history = dict()
		cell = self.prev
		while cell and (cell not in history and 
						cell.address != self.address):
			history[cell.address] = cell
			cell = cell.prev			
		return history


def build_graph(array_2d, pos=(0,0), nodes=None):
	if nodes is None:
		nodes = dict()
	x,y = pos
	if pos in nodes:
		node = nodes[pos]
	else:
		value = array_2d[x][y]
		node = Resident(value, pos)
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
			node = Resident(value, pos)
			nodes[pos] = node
		neighbors.append(node)
	return neighbors


def findLargerWords(array_2d, min_len=3):
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
	