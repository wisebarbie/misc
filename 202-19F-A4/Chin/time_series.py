# COMP 202: A4
# NAME: Chin Yiap Ong
# ID: 260823566


import doctest
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def date_diff(date1, date2):
    '''
    (str, str) -> int
    Take dates formatted in ISO format (%Y-%m-%d)
    Return number of days apart the two dates are
    Note that date can be positive/negative:
    - if the first date is earlier than the second date, the number should be positive;
    - if the second date is earlier than the first date, the number should be positive;
    >>> date_diff('2019-10-31', '2019-11-2') 
    2
    >>> date_diff('2019-10-31', '2015-11-2') 
    -1459
    >>> date_diff('2020-4-1', '2020-4-26') 
    25
    '''

    # convert date from string to integer given its specified ISO format 
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')

    # compute difference between dates and convert to days
    days = (date2 - date1).days

    return days


def get_age(date1, date2):
    '''
    (str, str) -> int
    Take dates formatted in ISO format (%Y-%m-%d)
    Assume 1 year = 365.2425 days
    Return number of years apart the two dates are
    Note that date can be positive/negative:
    - if the first date is earlier than the second date, the number should be positive;
    - if the second date is earlier than the first date, the number should be positive;
    >>> get_age('2019-10-31', '2019-11-2') 
    0
    >>> get_age('2019-10-31', '2015-11-2') 
    -3
    >>> get_age('2019-4-1', '2020-4-26') 
    1
    '''

    # 1 year = 365.2425 days 
    year_to_days = 365.2425

    # compute number of years as an integer (rounded down)
    years = int(date_diff(date1, date2) / year_to_days)

    return years


if __name__ == '__main__':

    doctest.testmod()