
class LocateException(Exception):
	pass

def findLargest(str_text, func):
	""" using the passed in function pointer func
	iterate over the string and return the first largest 
	token  to get a True result from func.
	"""
	n = len(str_text)
	if n <= 0:
		raise LocateException("Empty string.")
	# first slot to check is the full string
	slot_len = n
	while slot_len > 0:
		n_slots = n - slot_len + 1 # zero counts as a slot
		for pos in xrange(n_slots):
			# shift the slot over the full length of the string
			pos_end = slot_len+pos
			token = str_text[pos:pos_end]
			if func(token):
				return token
		# shrink the slot for the next iteration
		slot_len-=1	

def findMultipleLargest(str_text, func):
	""" using the passed in function pointer func
	iterate over the string and return a list of the
	largest tokens to get a True result from func.
	"""
	n = len(str_text)
	if n <= 0:
		raise LocateException("Empty string.")
	# first slot to check is the full string
	results = list()
	isMatch = False
	slot_len = n
	while slot_len > 0:
		n_slots = n - slot_len + 1 # zero counts as a slot
		for pos in xrange(n_slots):
			# shift the slot over the full length of the string
			pos_end = slot_len+pos
			token = str_text[pos:pos_end]
			if func(token):
				results.append(token)
				isMatch = True
		if isMatch:
			# if we found something for this slot length 
			# break out to stop processing, all others will
			# be smaller
			return results
		# shrink the slot for the next iteration
		slot_len-=1
	# return an empty list if none found	
	return results

def findMultipleLargest(str_text, func):
	""" using the passed in function pointer func
	iterate over the string and return a list of the
	largest tokens to get a True result from func.
	"""
	n = len(str_text)
	if n <= 0:
		raise LocateException("Empty string.")
	# first slot to check is the full string
	results = list()
	isMatch = False
	slot_len = n
	while slot_len > 0:
		n_slots = n - slot_len + 1 # zero counts as a slot
		for pos in xrange(n_slots):
			# shift the slot over the full length of the string
			pos_end = slot_len+pos
			token = str_text[pos:pos_end]
			if func(token):
				results.append(token)
				isMatch = True
		if isMatch:
			# if we found something for this slot length 
			# break out to stop processing, all others will
			# be smaller
			return results
		# shrink the slot for the next iteration
		slot_len-=1
	# return an empty list if none found	
	return results

def findAll(str_text, func):
	""" using the passed in function pointer func
	iterate over the string and return a list of the
	tokens that get a True result from func.
	"""
	n = len(str_text)
	if n <= 0:
		raise LocateException("Empty string.")
	# first slot to check is the full string
	results = list()
	slot_len = n
	while slot_len > 0:
		n_slots = n - slot_len + 1 # zero counts as a slot
		for pos in xrange(n_slots):
			# shift the slot over the full length of the string
			pos_end = slot_len+pos
			token = str_text[pos:pos_end]
			if func(token):
				results.append(token)
		# shrink the slot for the next iteration
		slot_len-=1
	# return an empty list if none found	
	return results
