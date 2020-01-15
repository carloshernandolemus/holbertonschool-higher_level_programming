#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        var1 = fct(*args)
        return(var1)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
