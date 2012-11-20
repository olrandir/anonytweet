# This snippet uses os.urandom, so it's pretty well random

import os
import string

def generate_random_string(length, stringset=string.ascii_letters+string.digits+string.punctuation):
    '''
    Returns a string with `length` characters chosen from `stringset`
    >>> len(generate_random_string(20) == 20 
    '''
    return ''.join([stringset[i%len(stringset)] \
        for i in [ord(x) for x in os.urandom(length)]])