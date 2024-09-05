"""
author : @jerinisready
description: interview @ incubyte
dated: Sept 5, 2024
"""
import re


def add(string):
    """ Get sum of comma seperated digits in the string  """

    delimiters = [',', '\n']
    delimiters_regex = '[{}]'.format(''.join(delimiters))

    numbers = re.split(delimiters_regex, string)
    out = 0
    for item in numbers:
       if item.isdigit():
           out += int(item)

    return out
