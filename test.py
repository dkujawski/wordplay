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
