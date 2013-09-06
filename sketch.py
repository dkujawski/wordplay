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

if __name__ == "__main__":
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	logger.addHandler(ch)

	logger.info("this is a test harness.")
	#print isPalindrome("ABBA")
	#print isPalindrome("ABCBA")
	#print isPalindrome("DAVE")
	
	print findLargest("ABBAXYZZYX")


