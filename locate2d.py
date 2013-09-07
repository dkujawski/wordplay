class Resident(object):
	def __init__(self, value, address):
		self.value = value
		self.address = address
		self.neighbors = list()
	
	def traverse(self, results, trail=""):
		trail += self.value
		for neighbor in self.neighbors:
			neighbor.traverse(results, trail)
		if len(self.neighbors) == 0:
			results.append(trail)

def findNeighbors(cell, array_2d, visited):
	""" for the given starting location :cell: collect adjacent cells
	from the :array_2d:. 	

	TODO: any reason why this isn't part of the Resident class?
	"""
	(x, y) = cell.address
	visited.add(cell.address)
	def _tryToAppendValue(_pos):
		_x, _y = _pos
		# pass on neg values as being outside array bounds
		if _x < 0 or _y < 0:
			return
		# walk back through parents.
		"""	TODO: revisit the use of the :visited: list... feels like there is a
		bug in there that needs to be confirmed.  The visited list needs to be
		reset for each traversal?
		"""		
		if _pos in visited:
			# exclude any neighbors that are already in attendance
			return
		try:
			value = array_2d[_x][_y]
		except IndexError as ie:
			# pass on any values outside of array bounds.
			return
		n = findNeighbors(Resident(value, (_x, _y)), array_2d, visited)
		cell.neighbors.append(n)
	
	""" This is a brute force approach to digging out neighbors 
	Would be nice to implement a more elegant algorythm here.
	"""
	# get horiz neighbors
	_tryToAppendValue((x-1, y))
	_tryToAppendValue((x+1, y))
	# get vert neighbors
	_tryToAppendValue((x, y-1))
	_tryToAppendValue((x, y+1))
	# get diags
	_tryToAppendValue((x+1, y-1))
	_tryToAppendValue((x+1, y+1))
	_tryToAppendValue((x-1, y-1))
	_tryToAppendValue((x-1, y+1))

	return cell

def walkTheSet(array_2d):
	""" generate list of traversals
	"""
	results = list()
	for x, x_val in enumerate(array_2d):
		for y, y_val in enumerate(x_val):
			# recursively dig to build the graph
			cell = findNeighbors(Resident(array_2d[x][y], (x,y)), array_2d, set())
			cell.traverse(results)
	return results
