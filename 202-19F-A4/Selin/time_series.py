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
    # compute difference between dates
    # return difference as number of days
    return (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(date1, '%Y-%m-%d')).days


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
    (str, str) -> ( (str, int) dict ) dict

    First, determine the index date: the first date in the first line of the file (2022-11-28 in our
    running example)
    The changes to make to the data:
        1. Replace the date of each record with the date_diff of that date and the index date
        2. Replace the date of birth with age at the time of the index date
        3. Replace the status with one of I, R and D. (Representing Infected, Recovered, and Dead;
        the French words are infecté(e), récupéré(e) and mort(e).)
    >>> stage_three('260823521_2.tsv', '260823521_3.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 3, 'D': 0, 'R': 0}, 10: {'I': 576, 'D': 69, 'R': 1}, 2: {'I': 7, 'D': 0, 'R': 0}, 3: {'I': 14, 'D': 1, 'R': 0}, 4: {'I': 30, 'D': 2, 'R': 0}, 5: {'I': 50, 'D': 17, 'R': 1}, 6: {'I': 118, 'D': 13, 'R': 0}, 7: {'I': 217, 'D': 74, 'R': 0}, 8: {'I': 430, 'D': 157, 'R': 0}, 9: {'I': 857, 'D': 361, 'R': 1}}
    
    Return: a dictionary. The keys are each day of the pandemic (integer). The values are a
    dictionary, with how many people are in each state on that day. Example:

    '''
    #Store a list of possible status: I - infected; R - recovered; D- dead 
    
    possible_status = {'I':'I', 'M':'D', 'R':'R', 'D':'D'}
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
    days_spanned =  []
    #list of tuples to keep track of (days since the index date, status)
    days_status_tuples = []
    #dictionary to return
      #another helper function to process lines
    def process_line(new_line, days_spanned, days_status_tuples):
        
        ln_lst = new_line.split('\t')
        if any(char.isdigit() for char in ln_lst[6]) and len(ln_lst) > 9:
            new_lst = ln_lst[:5]
            new_lst.append(ln_lst[5]+ln_lst[6])
            new_lst.extend(ln_lst[7:])
            ln_lst = new_lst
        #take the date_diff to count the days since the index date
        ln_lst[2] = str(date_diff(index_date, ln_lst[2]))
          #take get_age to calculate the age
        ln_lst[3] = str(get_age(ln_lst[3], index_date))
          #clean up the status now
        ln_lst[6] = str(clean_status(ln_lst[6]))
        days_spanned.append(ln_lst[2])
        days_status_tuples.append((int(ln_lst[2]), ln_lst[6]))
        # write line to output_filename and increment line count
        output_file.write('\t'.join(ln_lst))
        
    for line in input_lines:
        process_line(line, days_spanned, days_status_tuples)
    # close relevant files
    input_file.close()
    output_file.close()
    #now let's append what was needed in a dictionary
    #dictionary comprehension - referred to python 3 documentation attached to the syllabus
    #https://docs.python.org/3/search.html?q=dictionary+comprehension&check_keywords=yes&area=default
    days_status =  {int(day_spanned):{status:0 for status in possible_status.values()} for day_spanned in np.unique(days_spanned) if days_spanned}
    for (days, status) in days_status_tuples:
        if (status in possible_status.values()) and (days is not None):
            days_status[days][status] += 1
    return days_status
        
def plot_time_series(d):
    '''
    d : ( (str, int) dict ) dict -> (int list) list
    >>> d = stage_three('260823521_2.tsv', '260823521_3.tsv')
    >>> plot_time_series(d)
    [[1, 0, 0], [3, 0, 0], [576, 1, 69], [7, 0, 0], [14, 0, 1], [30, 0, 2], [50, 1, 17], [118, 0, 13], [217, 0, 74], [430, 0, 157], [857, 1, 361]]
    '''
    def comprehend_with_order(sd):
        return [sd['I'], sd['R'], sd['D']]
    
    #list comprehension - referred to the addenda in the textbook mentioned in the syllabus
    #and python 3 documentation
    #https://docs.python.org/3/search.html?q=dictionary+comprehension&check_keywords=yes&area=default
    result =  [comprehend_with_order(subdict) for subdict in d.values()]
    
    fig, ax = plt.subplots()
   
    ax.plot(np.arange(len(result)), [sublist[0] for sublist in result])
    ax.plot(np.arange(len(result)), [sublist[1] for sublist in result])
    ax.plot(np.arange(len(result)),[sublist[2] for sublist in result])
    
    plt.legend(('Infected', 'Recovered', 'Dead'))
    ax.set(title='Time series of early pandemic', xlabel = "Days into Pandemic", ylabel = "Number of People" )
    plt.savefig("time_series.png")

    return result


if __name__ == '__main__':
    doctest.testmod()