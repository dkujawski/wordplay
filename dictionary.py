
WORDS_FILE="/usr/share/dict/words"
WORDS_SET = set()

def loadDict():
	global WORDS_SET
	WORDS_SET = set()
	with open(WORDS_FILE, 'r') as fh:
		line = fh.readline()
		while line:
			WORDS_SET.add(line.upper().strip())
			line = fh.readline()
	print "loaded words:", len(WORDS_SET)

def isWord(str_text):
	return str_text.upper() in WORDS_SET

def browseWords(str_text):
	for word in WORDS_SET:
		if word.startswith(str_text.upper()):
			print word