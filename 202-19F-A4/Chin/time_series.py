# COMP 202: A4
# NAME: Chin Yiap Ong
# ID: 260823566


import doctest
import datetime
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
    >>> date_diff('2019-10-29', '2019-11-2') 
    4
    >>> date_diff('2019-8-30', '2015-9-1') 
    -1459
    >>> date_diff('2021-5-1', '2021-5-26') 
    25
    '''

    # convert date from string to integer given its specified ISO format 
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')

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
    >>> get_age('1970-10-31', '1970-11-2') 
    0
    >>> get_age('2020-10-31', '2016-11-2') 
    -3
    >>> get_age('2018-4-1', '2019-4-26') 
    1
    '''

    # 1 year = 365.2425 days 
    year_to_days = 365.2425

    # compute number of years as an integer (rounded down)
    years = int(date_diff(date1, date2) / year_to_days)

    return years

def stage_three(input_filename, output_filename):
    '''
    (str, str) -> ( (str, int) dict ) dict

    Given the index date, 

        1. Replace the date of each record with the date_diff of that date and the index date
        2. Replace the date of birth with age at the time of the index date
        3. Replace the status with one of I, R and D. (Representing Infected, Recovered, and Dead;
        the French words are infecté(e), récupéré(e) and mort(e).)

    Return: a dictionary. The keys are each day of the pandemic (integer). The values are a
    dictionary, with how many people are in each state on that day. Example:

    >>> stage_three('example_2.tsv', 'example_3.tsv')
    {0: {'I': 1, 'R': 0, 'D': 0}, 1: {'I': 2, 'R': 0, 'D': 1}}
        
    '''
    
    #helper function to clean up status
    def correct_status(token):
        if 'I' in token:
            return 'I'
        if 'M' in token or 'D' in token:
            return 'D'
        if 'R' in token:
            return 'R'
        
    #parse input files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store the input as a list
    input_lines = input_file.readlines()
    # fetch the index date
    index_date = input_lines[0].split('\t')[2]
    #store possible days passed since the index; 
    # will filter duplicates later
    days_spanned =  []
    #list of tuples to keep track of (days since the index date, status)
    days_status_item = []
    
    
    
    for line in input_lines:
       ln_l = line.split('\t')
       if any(char.isdigit() for char in ln_l[6]) and len(ln_l) > 9:
           new_l = ln_l[:5]
           new_l.append(ln_l[5]+ln_l[6])
           new_l.extend(ln_l[7:])
           ln_l = new_l
        #count the days since the index date
       ln_l[2] = str(date_diff(index_date, ln_l[2]))
          #take get_age to calculate the age
       ln_l[3] = str(get_age(ln_l[3], index_date))
          #clean up the status now
       ln_l[6] = str(correct_status(ln_l[6]))
       days_spanned.append(ln_l[2])
       days_status_item.append((int(ln_l[2]), ln_l[6]))
       # write line to output_filename and increment line count
       output_file.write('\t'.join(ln_l))
    # close relevant files
    input_file.close()
    output_file.close()
    #now let's append what was needed in a dictionary
   
    days_status = {}
    for day_spanned in np.unique(days_spanned):
        if day_spanned:
            days_status[int(day_spanned)] = {}
            for status in ['I', 'R', 'D']:
                days_status[int(day_spanned)][status]=0
                
    for (days, status) in days_status_item:
        if (status in ['I', 'R', 'D'] ) and (days is not None):
            days_status[days][status] += 1
    return days_status
        
def plot_time_series(d):
    '''
    d : ( (str, int) dict ) dict -> (int list) list

    '''
    def convert_to_list_of_lists(sd):
        return [sd['I'], sd['R'], sd['D']]
    
    
    result =  []
    for subdict in d.values():
        result.append(convert_to_list_of_lists(subdict))
    
    fig, ax = plt.subplots()
    
    infected = []
    recovered = []
    dead = []
    for sublist in result:
        infected.append(sublist[0])
        recovered.append(sublist[1])
        dead.append(sublist[2])
   
    ax.plot(range(len(result)), infected)
    ax.plot(range(len(result)), recovered)
    ax.plot(range(len(result)), dead)
    
    plt.legend(('Infected', 'Recovered', 'Dead'))
    ax.set(title='Time series of early pandemic', xlabel = "Days into Pandemic", ylabel = "Number of People" )
    plt.savefig("time_series.png")

    return result

if __name__ == '__main__':

    doctest.testmod()