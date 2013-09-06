from nose.tools import *

import palindrome

def test_isPalindrome_abba():
	assert_true( palindrome.isPalindrome("ABBA") )

def test_isPalindrome_abcba():
	assert_true( palindrome.isPalindrome("ABCBA") )

def test_isPalindrome_dave():
	assert_false( palindrome.isPalindrome("DAVE") )

@raises(palindrome.PalindromeException)
def test_isPalindrome_empty():
	assert_false( palindrome.isPalindrome("") )

# -- 

def test_findLargest_abba():
	assert_equal( palindrome.findLargest("ABBA"), "ABBA" )

def test_findLargest_abcba():
	assert_equal( palindrome.findLargest("ABCBA"), "ABCBA" )

def test_findLargest_dave():
	assert_equal( palindrome.findLargest("DAVE"), None )

@raises(palindrome.PalindromeException)
def test_findLargest_empty():
	assert_false( palindrome.findLargest("") )

# --

def test_findLargest_abbaxyzzyx():
	assert_equal( palindrome.findLargest("ABBAXYZZYX"), "XYZZYX" )

def test_findLargest_abcdefghijklmnopo():
	assert_equal( palindrome.findLargest("ABCDEFGHIJKLMNOPO"), "OPO" )

def test_findLargest_abcdefghijklmnopqrstuvwxyz():
	assert_equal( palindrome.findLargest("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), None )

def test_findLargest_aabcdefghijklmnopqrstuvwxyz():
	assert_equal( palindrome.findLargest("AABCDEFGHIJKLMNOPQRSTUVWXYZ"), "AA" )

def test_findLargest_example():
	value = "GHDUFNEICJSODLFJGHFYDNDJSKDNCHFGEJDBDJEGFHCNDKYATRSMZPLOBSRQNSB"
	assert_equal( palindrome.findLargest(value), "KDNCHFGEJDBDJEGFHCNDK" )

