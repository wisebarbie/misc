
import doctest


def which_delimiter(string):
    '''
    (str) -> str
    Return the most commonly used delimiter (space/comma/tab) in the input string
    >>> which_delimiter('0 1 2,3')
    ' '
    >>> which_delimiter('0,1,2,3')
    ','
    >>> which_delimiter('0\\t1\\t2\\t3')
    '\\t'
    >>> which_delimiter('0123')
    Traceback (most recent call last):
    AssertionError: Must contain at least one delimiter (space/comma/tab)
    '''
    # note acceptable delimiters (space/comma/tab)
    delimiters = [' ', ',', '\t']
    # initialize variables to note most common delimiter and its count 
    most_common = None
    max_count = 0
    # check for all acceptable delimiters
    for delimiter in delimiters:
        # update most common delimiter and its count if necessary
        if string.count(delimiter) > max_count:
            most_common = delimiter
            max_count = string.count(delimiter)
    # return most common delimiter if this exists
    if most_common:
        return most_common
    # otherwise raise error
    raise AssertionError('Must contain at least one delimiter (space/comma/tab)')


if __name__ == '__main__':
    doctest.testmod()