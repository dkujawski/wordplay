
class PalindromeException(Exception):
	pass

def isPalindrome(str_text):
	n = len(str_text)
	if n <= 0:
		raise PalindromeException("Empty string.")
	# integer division handles odd len strings leaving the middle letter out
	key = n/2
	# compare the first half of the string with the reverse of the second
	return str_text[:key] == str_text[-key:][::-1]

def findLargest(str_text):
	n = len(str_text)
	if n <= 0:
		raise PalindromeException("Empty string.")
	# first slot to check is the full string
	slot_len = n
	while slot_len > 0:
		n_slots = n - slot_len + 1 # zero counts as a slot
		for pos in xrange(n_slots):
			# shift the slot over the full length of the string
			pos_end = slot_len+pos
			token = str_text[pos:pos_end]
			if isPalindrome(token):
				return token
		# shrink the slot for the next iteration
		slot_len-=1		
