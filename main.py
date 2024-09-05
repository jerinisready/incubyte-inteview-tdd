"""
author : @jerinisready
description: interview @ incubyte
dated: Sept 5, 2024
"""


def add(string):
    """ Get sum of comma seperated digits in the string  """

    delimiters = ','

    numbers = string.split(delimiters)
    out = 0
    for item in numbers:
       if item.isdigit():
           out += int(item)

    return out
