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
    >>> date_diff('2020-1-1', '2020-1-30') 
    29
    >>> date_diff('2018-10-31', '2000-11-2') 
    -6572
    '''
    # convert date from string to integer given its specified ISO format 
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    # compute difference between dates
    time_delta = date2 - date1
    # return difference as number of days
    return time_delta.days


def get_age(date1, date2):
    """
    (str, str) -> int
    Take dates formatted in ISO format (%Y-%m-%d)
    Assume 1 year = 365.2425 days
    Return number of years apart the two dates are
    Note that date can be positive/negative:
    - if the first date is earlier than the second date, the number should be positive;
    - if the second date is earlier than the first date, the number should be positive;
    >>> get_age('2018-10-31', '2019-11-2')
    1
    >>> get_age('2018-10-31', '2000-11-2')
    -17
    >>> get_age("2016-12-31", "2019-11-2") 
    2
    """
    # assume 1 year = 365.2425 days 
    one_year = 365.2425
    # compute number of years 
    years = date_diff(date1, date2) / one_year
    # return number of years as an integer (rounded down)
    return int(years)


if __name__ == '__main__':
    doctest.testmod()