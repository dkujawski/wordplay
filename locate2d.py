class Resident(object):
	def __init__(self, value, address, prev=None):
		self.prev = prev
		self.value = value
		self.address = address
		self.neighbors = list()
	
	def traverse(self, results, trail=""):
		""" walk the tree building a string characters from each 
		value.
		"""
		#TODO: make this a list to join instead of +=
		trail += self.value
		history = self.getHistory()
		for neighbor in self.neighbors:
			if neighbor.address in history:
				results.append(trail)
				continue
			# recurse for all neighbors
			neighbor.traverse(results, trail)
		# when we hit a leaf node set the string
		if len(self.neighbors) == 0:
			results.append(trail)

	def getHistory(self):
		history = set()
		cell = self.prev
		while cell and (cell.address not in history and 
						cell.address != self.address):
			history.add(cell.address)
			cell = cell.prev			
		return history

def findNeighbors(cell, array_2d):
	""" for the given starting location :cell: collect adjacent cells
	from the :array_2d:. 	

	TODO: any reason why this isn't part of the Resident class?
	"""
	(x, y) = cell.address
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
		if _pos in cell.getHistory():
			# exclude any neighbors that are already in attendence
			return
		try:
			value = array_2d[_x][_y]
		except IndexError as ie:
			# pass on any values outside of array bounds.
			return
		n = findNeighbors(Resident(value, (_x, _y), cell), array_2d)
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
			cell = findNeighbors(Resident(array_2d[x][y], (x,y)), array_2d)
			cell.traverse(results)
	return results
