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

	Example usage::

		a = node.Node('A', (0,0))
		b = node.Node('B', (0,1))
		c = node.Node('C', (1,0))
		a.neighbors.append(b)
		b.neighbors.append(c)
		results = a.traverse()

	"""
	def __init__(self, value, address):
		self.value = value
		self.address = address
		self.neighbors = list()

	def traverse(self, func=None, results_ref=None, trail=None, history=None):
		""" 
		Traverse the graph building a trail of values as each node is visited.
		Update the result list with the concatonated string values when a leaf
		node is reached.

		:param func: a function pointer to a function that returns True or
			False and accepts a string as a the single parameter.  If present
			this function will be called using the concatonated string
			found at the leaf node. If the result is True the string will be 
			added to the result list.
		:param result_ref: This is initialized internally at the start of a 
			traversal.  This is the main container passed by ref through the
			recursive calls and returned at the end.
		:param trail: This is initialized internally at the start of the
			traversal.  This is the main list used to collect the node values
			from each node as they are visited.  When a leaf node is reached
			the list is joined to build a string of values and added to the 
			:param:``result_ref``.
		:param history: This is an internal value used during recursive
			traversals to track where we have already been to avoid
			duplicate values and infinite loops.
		:returns: list containing the collected concatonated strings found
			during the traversal.

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
			# building copy of these lists to pass by value, we want each 
			# iteration of the loop to use its own history.  if passed by
			# ref subsequent loop iterations' history would be contaminated
			# with history from an unrelated traversal.
			t_val = list(trail)
			h_val = list(history)
			# recurse for all neighbors
			results_ref = neighbor.traverse(func, results_ref, t_val, h_val)

		trail_str = ''.join(trail)
	   	if not results_ref or not results_ref[-1].startswith(trail_str):
			if func is None or func(trail_str):
				# add all trails to results
				results_ref.append(trail_str)
		return results_ref

