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
		#TODO: make this a list to join instead of += ??
		trail += self.value
		history = self.getHistory()
		for neighbor in self.neighbors:
			if neighbor.address in history:
				# we have been here before
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
	history = cell.getHistory()
	def _tryToAppendValue(_pos):
		_x, _y = _pos
		# pass on neg values as being outside array bounds
		if _x < 0 or _y < 0:
			return
		# walk back through parents.
		if _pos in history:
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
	Would be nice to implement a more elegant algorithm here.
	"""
	# get vert neighbors
	_tryToAppendValue((x-1, y))
	_tryToAppendValue((x+1, y))
	# get horiz neighbors
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
		for y, _ in enumerate(x_val):
			# recursively dig to build the graph
			cell = findNeighbors(Resident(array_2d[x][y], (x,y)), array_2d)
			cell.traverse(results)
	return results

def findLargerWords(array_2d, min_len=3):
	""" generate list of larger words with 3 chars or more found in the set
	"""
	import dictionary # load up the dictionary
	import locate
	results = list()
	for x, x_val in enumerate(array_2d):
		for y, _ in enumerate(x_val):
			# recursively dig to build the graph
			cell = findNeighbors(Resident(array_2d[x][y], (x,y)), array_2d)
			strings = list()
			cell.traverse(strings)
			while strings:
				trail = strings.pop()
				# locate the largest dictionary word at least min_len 
				# in each trail
				found = locate.findLargest(trail, dictionary.isWord)
				if found and len(found) >= min_len:
					results.append(found)
	return results