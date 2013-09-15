
def generate_large_random_string(str_len=1024):
    # http://stackoverflow.com/questions/785058/random-strings-in-python-2-6-is-this-ok
    import string    
    import random    
    return ''.join(random.choice(string.ascii_uppercase) for i in xrange(str_len))

def generate_2d_array(a_size=4):
    import string
    import random
    a = list()
    for i in xrange(a_size):
        b = list()
        for j in xrange(a_size):
            b.append(random.choice(string.ascii_uppercase))
        a.append(b)
    return a

def prof_findLargest_01():
    rand_str = generate_large_random_string()
    cmd_str = "locate.findLargest('%s', palindrome.isPalindrome)" % rand_str
    do_profile(cmd_str)

def prof_findLargerWords_01():
    cmd_str = "locate2d.findLargerWords(generate_2d_array())"
    do_profile(cmd_str) #, sort_by='pcalls')#, sort_by='time')

# -----------
import cProfile
import datetime
import os
import pstats

def do_profile(cmd_str, nstats=20, sort_by='cumulative'):
    ''' use cProfile to run a function

        :param cmd_str: string to be evaled
        :param nstats: number of stats lines to print
        :param sortby: which stats column to sort by, calls, cumulative, file,
            module, pcalls, line, name, nfl, stdname, time

    '''
    stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%s")
    statfn = "%s.stats" % (stamp)

    cProfile.run(cmd_str, statfn)

    stats = pstats.Stats(statfn)
    stats = stats.strip_dirs()
    stats = stats.sort_stats(sort_by)
    stats.print_stats(nstats)

    os.unlink(statfn)

    return

if __name__ == "__main__":
    import os
    import sys
    # find the src dir and add it to the sys.path
    src = os.path.join(os.path.join(os.path.dirname(__file__), "../"), "src")
    sys.path.append(os.path.abspath(src))

    import locate
    import locate2d
    import palindrome

    #prof_findLargest_01()
    prof_findLargerWords_01()
    #locate2d.findLargerWords(generate_2d_array(2))
