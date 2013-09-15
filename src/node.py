"""
.. sectionauthor:: Dave Kujawski

Node class used to construct a graph of a 2d array where each element has edges
connecting it to each adjacent element.

* :class:`Node`: Node used to constructing a graph stucture.

"""

class Node(object):
	"""
	This is a simple node class used for constructing a graph or tree data 
	structure.
	"""
	def __init__(self, value, address):
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

