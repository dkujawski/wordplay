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

import locate

def test_findLargest_abba():
	assert_equal( locate.findLargest("ABBA", palindrome.isPalindrome), "ABBA" )

def test_findLargest_abcba():
	assert_equal( locate.findLargest("ABCBA", palindrome.isPalindrome), "ABCBA" )

def test_findLargest_dave():
	assert_equal( locate.findLargest("DAVE", palindrome.isPalindrome), None )

@raises(locate.LocateException)
def test_findLargest_empty():
	assert_false( locate.findLargest("", palindrome.isPalindrome) )

# --

def test_findLargest_abbaxyzzyx():
	assert_equal( locate.findLargest("ABBAXYZZYX", palindrome.isPalindrome), "XYZZYX" )

def test_findLargest_abcdefghijklmnopo():
	assert_equal( locate.findLargest("ABCDEFGHIJKLMNOPO", palindrome.isPalindrome), "OPO" )

def test_findLargest_abcdefghijklmnopqrstuvwxyz():
	assert_equal( locate.findLargest("ABCDEFGHIJKLMNOPQRSTUVWXYZ", palindrome.isPalindrome), None )

def test_findLargest_aabcdefghijklmnopqrstuvwxyz():
	assert_equal( locate.findLargest("AABCDEFGHIJKLMNOPQRSTUVWXYZ", palindrome.isPalindrome), "AA" )

def test_findLargest_example():
	value = "GHDUFNEICJSODLFJGHFYDNDJSKDNCHFGEJDBDJEGFHCNDKYATRSMZPLOBSRQNSB"
	assert_equal( locate.findLargest(value, palindrome.isPalindrome), "KDNCHFGEJDBDJEGFHCNDK" )

# --

def test_findMultipleLargest_abba():
	assert_equal( locate.findMultipleLargest("ABBA", palindrome.isPalindrome), ["ABBA"] )

def test_findMultipleLargest_abcba():
	assert_equal( locate.findMultipleLargest("ABCBA", palindrome.isPalindrome), ["ABCBA"] )

def test_findMultipleLargest_abbacddc():
	assert_equal( locate.findMultipleLargest("ABBACDDC", palindrome.isPalindrome), ["ABBA", "CDDC"] )

def test_findMultipleLargest_abcbadefgfedhijkjih():
	assert_equal( locate.findMultipleLargest("ABCBADEFGFEDHIJKJIH", palindrome.isPalindrome), ["DEFGFED","HIJKJIH"] )

def test_findMultipleLargest_dave():
	assert_equal( locate.findMultipleLargest("DAVE", palindrome.isPalindrome), [] )

@raises(locate.LocateException)
def test_findMultipleLargest_empty():
	assert_false( locate.findMultipleLargest("", palindrome.isPalindrome) )

# --

def test_findAll_abcbadefgfedhijkjih():
	assert_equal( locate.findAll("ABCBADEFGFEDHIJKJIH", palindrome.isPalindrome), ['DEFGFED', 'HIJKJIH', 'ABCBA', 'EFGFE', 'IJKJI', 'BCB', 'FGF', 'JKJ'] )

