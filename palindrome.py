
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
	
