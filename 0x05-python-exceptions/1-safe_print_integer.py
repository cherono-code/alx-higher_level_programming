#!/usr/bin/python3


def safe_print_integer(value):
    """Printing integer with "{:d}".format().

    Args:
        value (int): integer to be print.

    Returns:
        If a TypeError or ValueError occurs - False.
        else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
