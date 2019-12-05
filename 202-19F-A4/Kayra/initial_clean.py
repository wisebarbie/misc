# COMP 202 Assignment 4
# Name: Kayra Aker
# Student ID: 260837168

import doctest

def which_delimiter(string):
    '''
    (str)->str
    Return the most commonly used delimiter (space, comma, tab) in the input string
    >>> which_delimiter('0 1 2,3')
    ' '
    >>> which_delimiter('4 5,6,7')
    ','
    >>> which_delimiter('8\\t9\\t10\\t 11')
    '\\t'
    >>> which_delimiter('1234')
    Traceback (most recent call last):
    AssertionError: Must contain at least one delimiter (space, comma, tab)
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
    raise AssertionError('Must contain at least one delimiter (space, comma, tab)')

def stage_one(input_filename, output_filename):
    '''
    (str,str)->int
    Read input_filename and write to output_filename after making the following changes: 
    1. Change the most common delimiter to tab (if it is not already tab-delimited) 
    2. Change all text to be upper case
    3. Change any / or . in the dates to hyphens (-) 
    Return the number of lines written to output_filename
    >>> stage_one('stage1.txt', 'stage1.tsv')
    4
    '''
    # open relevant files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store lines from input_filename as a list
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
        # write line to output_filename and increment line count
        output_file.write(line)
        line_count += 1 
    # close relevant files
    input_file.close()
    output_file.close()
    # return line count
    return line_count

def stage_two(input_filename, output_filename):
    '''
    (str,str)->int
    Read input_filename and write to output_filename after ensuring the following: 
    1. All lines should have 9 clean columns
    2. Any lines with more than 9 columns should be cleaned so that the line has 9 columns. 
    Return the number of lines written to output_filename
    >>> stage_two('stage1.tsv', 'stage2.tsv')
    4
    '''
    # open relevant files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store lines from input_filename as a list
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
        # write line to output_filename and increment line count
        output_file.write(line)
        line_count += 1 
    # close relevant files
    input_file.close()
    output_file.close()
    # return line count
    return line_count

if __name__ == '__main__':
    doctest.testmod()