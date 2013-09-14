
WORDS_FILE="/usr/share/dict/words"
WORDS_SET = set()

def loadDict(min_len=1):
	global WORDS_SET
	WORDS_SET = set()
	try:
		with open(WORDS_FILE, 'r') as fh:
			line = fh.readline()
			while line:
				w = line.strip()
				if len(w) >= min_len:
					WORDS_SET.add(w.upper())
				line = fh.readline()
	except IOError as ioe:
		print ioe
		print "Unable to locate the words file on your system: %s" % (WORDS_FILE,)
		print "Please update the %s module to use the appropriate path for your system." % (__file__,)
	# debug --
	#print "loaded words:", len(WORDS_SET)

def isWord(str_text):
	return str_text in WORDS_SET

def browseWords(str_text):
	for word in WORDS_SET:
		if word.startswith(str_text.upper()):
			print word

# load it up on import
# this can be controversial.. choose your imports wisely.
loadDict()
