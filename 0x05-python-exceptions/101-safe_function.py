#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: function to execute.
        args: arguments passed for fct.

    Returns:
        If an error occurs - None.
        else - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
