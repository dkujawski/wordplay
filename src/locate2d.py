
# http://www.skymind.com/~ocrow/python_string/
from cStringIO import StringIO

class Resident(object):
	def __init__(self, value, address, prev=None):
		self.prev = prev
		self.value = value
		self.address = address
		self.neighbors = list()
	
	def traverse(self, func=None, results=None, trail="", history=None):
		""" walk the tree building a string characters from each 
		value.
		"""
		if not results:
			results = list()
		if not history:
			history = list()
		history.append(self.address)

		# http://www.skymind.com/~ocrow/python_string/
		trail += self.value
		
		#print "\t", self.value, trail, [n.value for n in self.neighbors], [h for h in history]
		for neighbor in self.neighbors:
			if neighbor.address in history:
				#results.append(trail)
				#print "\t  -skipping:", neighbor.value
				continue
			# recurse for all neighbors
			#print "\t  ", neighbor.value, "->", results
			results = neighbor.traverse(func, results, trail, list(history))
			# print "\t  ", results
		# when we hit a leaf node set the string
		if self.address == history[-1] and \
		   (not results or not results[-1].startswith(trail)):
			if func is None:
				# add all trails to results
				results.append(trail)
			elif func(trail):
				# only add trails that provide a true return value
				#print "\t", func.__name__, trail
				results.append(trail)
		return results

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



def findNeighbors(cell, array_2d):
	""" for the given starting location :cell: collect adjacent cells
	from the :array_2d:. 	

	TODO: any reason why this isn't part of the Resident class?
	"""
	(x, y) = cell.address
	history = cell.getHistory()
	def _tryToAppendValue(_pos):
		_x, _y = _pos
		if _pos in history:
			# include neighnbors in history but don't recurse
			cell.neighbors.append(history[_pos])
			return
		# ignore neg values as being outside array bounds
		if _x < 0 or _y < 0:
			return
		try:
			value = array_2d[_x][_y]
		except IndexError as ie:
			# pass on any values outside of array bounds.
			return
		n = findNeighbors(Resident(value, _pos, cell), array_2d)
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
	value = array_2d[0][0]
	address = (0,0)
	cell = findNeighbors(Resident(value, address), array_2d)
	return cell.walk()

def findLargerWords(array_2d, min_len=3):
	""" generate list of larger words with 3 chars or more found in the set
	"""
	import dictionary # load up the dictionary
	dictionary.loadDict(min_len)

	value = array_2d[0][0]
	address = (0,0)
	cell = findNeighbors(Resident(value, address), array_2d)
	return cell.walk(func=dictionary.isWord)