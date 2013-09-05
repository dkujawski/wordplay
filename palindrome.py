
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
	# get the first half of the string
	comp_start = str_text[:key]
	# get the last half
	comp_end = str_text[-key:]
	# compare the two strings, reverse the second
	return comp_start == comp_end[::-1]

