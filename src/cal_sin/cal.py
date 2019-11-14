'''
calculating sin
'''

import logging
import math
def sin_cal(angle):
    '''
    Function to calculate Sin value
    '''
    logging.basicConfig(filename="confile.log", level=logging.ERROR, format='%(message)s',filemode='w')
    try:
        value = float(angle)
        if value:
            return math.sin(float(angle))
        else:
            raise ValueError
    except ValueError as e:
        logging.error(e.message)
        return "It is not number"
