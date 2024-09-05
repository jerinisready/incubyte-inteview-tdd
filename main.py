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

    match = re.search(r'//\[(.*?)\]\n(.*)', string, re.DOTALL)

    if match:
        delimiters = match.group(1).split('][')
        number_input = match.group(2)
        print(f'{delimiters=}, {number_input=}')
    else:
        raise AddHandlerException('Improply created input pattern')

    numbers = re.split('[{}]'.format(''.join(delimiters)), number_input)

    out = 0
    processed_numbers = []
    negative_numbers = []

    for item in numbers:

       if not item:
          continue

       elif item.startswith('-') and item[1:].isdigit():
           negative_numbers.append(item)

       elif item.isdigit():

           if len(item) > 3:
               continue
           processed_numbers.append(int(item))


    if negative_numbers:
        raise AddHandlerException('negative numbers not allowed {}'.format(','.join(negative_numbers)))

    return sum(processed_numbers)





if __name__ == "__main__":
    print(add('//[;][,]\n1;2,3'))
