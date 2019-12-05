# COMP 202 Assignment 4
# Name: Kayra Aker
# Student ID: 260837168


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
        - if the second date is earlier than the first date, the number should be negative;
    >>> date_diff('2019-10-31', '2019-11-2') 
    2
    >>> date_diff('2020-7-1', '2020-7-30') 
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
    Take 1 year = 365.2425 days
    Return number of years apart the two dates are
    Note that date can be positive/negative:
        - if the first date is earlier than the second date, the number should be positive;
        - if the second date is earlier than the first date, the number should be negative;
    >>> get_age('2018-10-31', '2019-11-2')
    1
    >>> get_age('2018-10-31', '2000-11-2')
    -17
    >>> get_age('2016-10-31', '2019-9-2') 
    2
    '''
    # take 1 year = 365.2425 days 
    one_year = 365.2425
    # compute number of years 
    years = date_diff(date1, date2) / one_year
    # return number of years as an integer (rounded down)
    return int(years)


def stage_three(input_filename, output_filename):
    '''
    (str, str) -> dict
    Read input_filename.
    Determine the index date (i.e. first date in the first line of the file).
    Write to output_filename after making the following changes: 
        1. Replace the date of each record with the date_diff of that date and the index date.
        2. Replace the date of birth with age at the time of the index date.
        3. Replace the status with one of 
            - I (Infected, infecté(e)) 
            - R (Recovered, récupéré(e))  
            - D (Dead, mort(e))
    Return a dictionary, where:
        - the keys are each day of the pandemic (integer)
        - the values are a dictionary, where:
            - the keys are the state
            - the values are number of people in that state that day
    >>> stage_three('stage2.tsv', 'stage3.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}}
    '''
    # open relevant files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store lines from input_filename as a list
    input_lines = input_file.readlines()
    # initialize dictionary
    day_dict = {}
    # note index date
    index_date = input_lines[0].split('\t')[2]
    # do for all lines
    for line in input_lines:
        # split line by delimiter into list
        line_list = line.split('\t')
        # replace date with difference in days from index date
        line_list[2] = str(date_diff(index_date, line_list[2]))
        # replace DOB with age at index date
        line_list[3] = str(get_age(line_list[3], index_date))
        # standardize status labels
        line_list[6] = line_list[6][0].upper()
        if line_list[6] == 'M':
            line_list[6] = 'D'
        # update dictionary
        if int(line_list[2]) not in day_dict.keys():
            day_dict[int(line_list[2])] = {'I': 0, 'D': 0, 'R': 0}
        day_dict[int(line_list[2])][line_list[6]] += 1
        # join list by delimiter back into a string
        line = '\t'.join(line_list)
        # write line to output_filename
        output_file.write(line)
    # return dictionary in desired format
    return day_dict


def plot_time_series(day_dict):
    '''
    dict -> list
    Return a list of lists, where each sublist represents each day of the pandemic 
    i.e. [how many people infected, how many people recovered, how many people dead]
    >>> day_dict = stage_three('stage2.tsv', 'stage3.tsv')
    >>> plot_time_series(day_dict)
    [[1, 0, 0], [2, 0, 1]]
    '''
    # initialize variables
    day_list = []
    days = []
    I = []
    R = []
    D = []
    # do for every (key, value) pair in dictionary
    for day, status_dict in sorted(day_dict.items()):
        days.append(day)
        I.append(status_dict['I'])
        R.append(status_dict['R'])
        D.append(status_dict['D'])
        day_list.append([status_dict['I'], status_dict['R'], status_dict['D']])
    # plot points per status
    plt.plot(days, I)
    plt.plot(days, R)
    plt.plot(days, D)
    # add title, axis labels, legend
    plt.title('Time series of early pandemic, by Kayra Aker')
    plt.xlabel('Days into Pandemic')
    plt.ylabel('Number of People')
    plt.legend(['Infected', 'Recovered', 'Dead'])
    # save figure
    plt.savefig('time_series.png')
    # return list in desired format
    return day_list


if __name__ == '__main__':
    doctest.testmod()