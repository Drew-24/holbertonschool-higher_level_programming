#!/usr/bin/python3
""" Module has function that checks for object instance """


def is_kind_of_class(obj, a_class):
    """ returns True/False for object instance """
    if isinstance(obj, a_class):
        return True
    else:
        return False
