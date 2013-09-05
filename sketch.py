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
	logger.info(key)
	# get the first half of the string
	comp_start = str_text[:key]
	logger.info(comp_start)
	# get the last half
	comp_end = str_text[-key:]
	logger.info(comp_end)
	# compare the two strings, reverse the second
	return comp_start == comp_end[::-1]

if __name__ == "__main__":
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	logger.addHandler(ch)

	logger.info("this is a test harness.")
	print isPalindrome("ABBA")
	print isPalindrome("CDC")
	print isPalindrome("DAVE")
	

