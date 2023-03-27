#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as er:
        import sys
        print("Exception: {}".format(er), file=sys.stderr)
        return None
