"""
author : @jerinisready
description: interview @ incubyte
dated: Sept 5, 2024
"""
import re


# expected in exceptions.py

class AddHandlerException(Exception):
    """
     Used to raise when things are out of handle in add method. 
    """


def add(string):
    """ Get sum of comma seperated digits in the string  """

    match = re.search(r'//(.*?)\n(.*)', string)
    if match:
        delimiters = match.group(1)
        number_input = match.group(2)

    else:
        raise AddHandlerException('Improply created input pattern')

    numbers = re.split('[{}]'.format(delimiters), number_input)

    out = 0
    for item in numbers:
       if item.isdigit():
           out += int(item)

    return out
