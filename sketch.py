#!/usr/bin/env python

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#
class PalindromeException(Exception):
	pass

def isPalindrome(str_text):
	n = len(str_text)
	if n <= 0:
		# is an empty string a palendrome?
		# TODO, raise exception here instead of return False
		raise PalindromeException("Empty string.")
	# integer division handles odd len strings leaving the middle letter out
	key = n/2
	logger.info("isPalindrome key: %s", key)
	# get the first half of the string
	comp_start = str_text[:key]
	# get the last half
	comp_end = str_text[-key:]
	logger.info("\t%s %s" % (comp_start, comp_end))
	# compare the two strings, reverse the second
	return str_text[:key] == str_text[-key:][::-1]


def findLargest(str_text):
	n = slot_len = len(str_text)
	logger.info("str_text len: %d" % n)
	if n <= 0:
		raise PalindromeException("Empty string.")

	while slot_len > 0:
		logger.info("slot_len: %d" % slot_len)
		n_slots = n - slot_len
		for slot in xrange(n_slots+1):
			logger.info("%d, %d, %d" % (n_slots, slot_len, slot))
			# shift the slot over the full length of the string
			pos_start = slot
			pos_end = slot_len+slot
			logger.info("%s:%s" % (pos_start, pos_end))
			token = str_text[pos_start:pos_end]
			logger.info("processing token: %s", token)
			if isPalindrome(token):
				logger.info("found: %s", token)
				return token
		slot_len-=1

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
	(x, y) = cell.address
	visited.add(cell.address)
	def _tryToAppendValue(_pos):
		_x, _y = _pos
		# pass on neg values as being outside array bounds
		if _x < 0 or _y < 0:
			return
		# walk back through parents.
		if _pos in visited:
			# exclude any neighbors that are already in attendance
			return
		try:
			value = array_2d[_x][_y]
		except IndexError as ie:
			# pass on any values outside of array bounds.
			return
		n = findNeighbors(Resident(value, (_x, _y), cell.address), array_2d, visited)
		cell.neighbors.append(n)
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

if __name__ == "__main__":
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	logger.addHandler(ch)

	logger.info("this is a test harness.")
	#print isPalindrome("ABBA")
	#print isPalindrome("ABCBA")
	#print isPalindrome("DAVE")
	
	#print findLargest("ABBAXYZZYX")

	tmp_values = [[ 'I', 'T', 'N', 'D', 'O' ],
				  [ 'S', 'A', 'K', 'X', 'N' ],
				  [ 'L', 'B', 'Z', 'M', 'E' ],
				  [ 'P', 'E', 'L', 'M', 'E' ],
				  [ 'O', 'P', 'L', 'S', 'T' ]]
	
	#print findNeighbors((2,2), tmp_values)
	#print walkTheSet(tmp_values)

	import dictionary
	import locate
	import locate2d

	dictionary.loadDict()
	foundWords = list()
	results = locate2d.walkTheSet(tmp_values)
	for str_text in results:
		foundWords.append(locate.findLargest(str_text, dictionary.isWord))

	print foundWords
