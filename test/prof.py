#
import cProfile
import datetime
import os
import pstats

def do_profile(cmd_str, nstats=20, sortby='cumulative'):
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
    stats = stats.sort_stats(sortby)
    stats.print_stats(nstats)

    os.unlink(statfn)

    return