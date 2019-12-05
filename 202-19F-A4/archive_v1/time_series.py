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
    '''
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
    >>> get_age('2016-10-31', '2019-9-2') 
    2
    '''
    # assume 1 year = 365.2425 days 
    one_year = 365.2425
    # compute number of years 
    years = date_diff(date1, date2) / one_year
    # return number of years as an integer (rounded down)
    return int(years)

def stage_three(input_filename, output_filename):
    '''
    (str, str) -> dict(dict(str:int))

    First, determine the index date: the fi
rst date in the fi
rst line of the fi
le (2022-11-28 in our
    running example)
    The changes to make to the data:
        1. Replace the date of each record with the date_diff of that date and the index date
        2. Replace the date of birth with age at the time of the index date
        3. Replace the status with one of I, R and D. (Representing Infected, Recovered, and Dead;
        the French words are infecté(e), récupéré(e) and mort(e).)
    >>> stage_three('stage2.tsv', 'stage3.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}}
    
    Return: a dictionary. The keys are each day of the pandemic (integer). The values are a
    dictionary, with how many people are in each state on that day. Example:

    '''
    #Store a list of possible status: I - infected; R - recovered; D- dead 
    
    possible_status = {'I':'I', 'M':'D', 'R':'R'}
    #helper function to clean up status
    def clean_status(token):
        for status in possible_status.keys():
            if status in token.upper():
                return possible_status[status]
        
    # open input files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store lines from input_filename as a list
    input_lines = input_file.readlines()
    # fetch the index date
    index_date = input_lines[0].split('\t')[2]
    #store possible days passed since the index; 
    # will filter duplicates later
    days =  []
    #list of tuples to keep track of (days since the index date, status)
    days_status_tuples = []
    #dictionary to return
    
    for line in input_lines:
        ln_lst = line.split('\t')
        #get date_diagnosed
        date_diagnosed = ln_lst[2]
        #take the date_diff to count the days since the index date
        ln_lst[2] = str(date_diff(index_date, date_diagnosed))
        
        days.append(ln_lst[2])
        #get date of birth
        birthdate =  ln_lst[3]
        #take get_age to calculate the age
        ln_lst[3] = str(get_age(birth_date, index_date))
        #clean up the status now
        status_raw = ln_lst[6]
        ln_lst[6] = str(clean_status(status_raw))
        days_status_tuples.append((int(ln_lst[2]), ln_lst[6]))
        line_modified = '\t'.join(ln_lst)
        # write line to output_filename and increment line count
        output_file.write(line_modified)
    
    #now let's append what was needed in a dictionary
    days_status = {} 
    for day in np.unique(days):
        days_status[int(day)] = {}
        for status in possible_status.values():
            days_status[int(day)][status] = 0
            
    for (days, status) in days_status_tuples:
        days_status[days][status] += 1
    return days_status

if __name__ == '__main__':
    doctest.testmod()