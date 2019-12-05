# COMP 202 A4
# Name: Chin Yiap Ong
# Student ID: 260823566


import doctest


def which_delimiter(string):
    '''
    (str)-> str

    Return the most commonly used delimiter (i.e. space, comma, tab) in the input string 

    >>> which_delimiter('0 1 2,3')
    ' '

    >>> which_delimiter('4\\t5\\t6\\t7')
    '\\t'

    >>> which_delimiter('8,9,10,11')
    ','

    >>> which_delimiter('12-13-14-15')
    Traceback (most recent call last):
    AssertionError: Does not contain at least one delimiter (i.e. space, comma, tab)
    
    >>> which_delimiter('0123')
    Traceback (most recent call last):
    AssertionError: Does not contain at least one delimiter (i.e. space, comma, tab)
    '''

    # initialize variables
    delimiters = [' ', ',', '\t']
    max_delimiter = ''
    max_count = 0

    # count frequency of all delimiters in input string
    for delimiter in delimiters:
        count = string.count(delimiter)
        # store most frequent delimiter and its count
        if count > max_count:
            max_delimiter = delimiter
            max_count = string.count(delimiter)

    # return most frequent delimiter if at least one delimiter exists
    if max_count != 0:
        return max_delimiter
    else:
        raise AssertionError('Does not contain at least one delimiter (i.e. space, comma, tab)')


def stage_one(input_filename, output_filename):
    '''
    (str, str) -> int

    Read input_filename and write to output_filename after making the following changes: 
    1. Change the most common delimiter to tab (if it is not already tab-delimited) 
    2. Change all text to be upper case
    3. Change any / or . in the dates to hyphens (-) 
    Return the number of lines written to output_filename

    >>> stage_one('stage1-example.txt', 'stage1.tsv')
    4
    '''

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        with open(input_filename, 'r', encoding='utf-8') as input_file:

            # store lines from input file as a list
            input_lines = input_file.readlines()

            # initialize variable to count number of lines written to output_filename
            line_count = 0

            # do for all lines
            for line in input_lines:
                # change the most common delimiter to tab 
                line = line.replace(which_delimiter(line), '\t')
                # change all text to be upper case
                line = line.upper()
                # split line by delimiter into list to specifically target dates
                line_list = line.split('\t')
                # change any / or . in the dates to hyphens (-) 
                line_list[2] = line_list[2].replace('.', '-')
                line_list[2] = line_list[2].replace('/', '-')
                line_list[3] = line_list[3].replace('/', '-')
                line_list[3] = line_list[3].replace('.', '-')
                # join list by delimiter back into a string
                line = '\t'.join(line_list)
                # write line to output file
                output_file.write(line)
                # increment line count
                line_count += 1 

    return line_count


def stage_two(input_filename, output_filename):
    '''
    (str, str) -> int
    
    Read input_filename and write to output_filename after ensuring the following: 
    1. All lines should have 9 clean columns
    2. Any lines with more than 9 columns should be cleaned so that the line has 9 columns. 
    Return the number of lines written to output_filename
    
    >>> stage_two('stage1.tsv', 'stage2.tsv')
    4
    '''

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        with open(input_filename, 'r', encoding='utf-8') as input_file:

            # store lines from input file as a list
            input_lines = input_file.readlines()

            # initialize variable to count number of lines written to output_filename
            line_count = 0

            # do for all lines
            for line in input_lines:
                # split line by delimiter into list
                line_list = line.split('\t')
                # make changes if there are more than 9 columns
                if len(line_list) > 9:
                    temperature_list = line_list[7:-1]
                    temperature = temperature_list[0]
                    for i in range(1, len(temperature_list)):
                        if any(char.isdigit() for char in temperature_list[i]):
                            temperature = temperature + '.' + temperature_list[i].replace(' ', '')
                        else:
                            temperature = temperature + temperature_list[i].replace(' ', '')
                    line = '\t'.join(line_list[:7]) + '\t' + temperature + '\t' + line_list[-1]
                # write line to output file
                output_file.write(line)
                # increment line count
                line_count += 1 

    return line_count


if __name__ == '__main__':

    doctest.testmod()