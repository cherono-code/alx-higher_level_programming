#!/usr/bin/python3
"""Checks whether object is an instance of a class"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the
    class, else return false
    """
    return (type(obj) == a_class)
