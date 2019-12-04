
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
    
    #initialize a dictionary of (count of delimiters:int, delimter:str)
    delimiters_count  = {}
    
    # check for all acceptable delimiters
    for delimiter in delimiters:
        if string.count(delimiter) > 0:
            delimiters_count[string.count(delimiter)] = delimiter
    #your key will be an integer, so it can be ordered; we will do 
    # delimiters_count[max_count], which is the delimiter with most occurences
    if delimiters_count:
        biggest_count = max(delimiters_count.keys())
        return delimiters_count[biggest_count]
    # otherwise raise error
    raise AssertionError('Must contain at least one delimiter (space/comma/tab)')


def stage_one(input_filename, output_filename):
    '''
    (str, str) -> int
    Read input_filename and write to output_filename after making the following changes: 
    1. Change the most common delimiter to tab (if it is not already tab-delimited) 
    2. Change all text to be upper case
    3. Change any / or . in the dates to hyphens (-) 
    Return the number of lines written to output_filename
    >>> stage_one('stage1.txt', 'stage1.tsv')
    4
    '''
    #helper
    def replace_to_hyphen(line):
        # change the most common delimiter to tab 
        # split line by tab into list to specifically target dates
        # change all text to be upper case
        ln_lst = line.replace(which_delimiter(line), '\t').upper().split('\t')
        for i in range(2, 4):
            ln_lst[i] = ln_lst[i].replace('.', '-').replace('/', '-')
        line_modified = '\t'.join(ln_lst)
        return line_modified
         
        
    # open input files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store lines from input_filename as a list
    input_lines = input_file.readlines()
    # initialize variable to count number of lines written to output_filename
    line_count = 0
    # do for all lines
    for line in input_lines:
        #use helper here
        line_cleaned = replace_to_hyphen(line)
        # write line to output_filename and increment line count
        output_file.write(line_cleaned)
        line_count += 1 
    # close relevant files
    input_file.close()
    output_file.close()
    # return line count
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
    #helper function
    def get_columns_straight(t_lst):
        t = t_lst[0]
        for i in range(1, len(t_lst)):
                if any(char.isdigit() for char in t_lst[i]):
                    t = t + '.' + t_lst[i].replace(' ', '')
                else:
                    t = t + t_lst[i].replace(' ', '')
        return t
        
    # open input files
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    # store lines from input_filename as a list
    input_lines = input_file.readlines()
    # initialize variable to count number of lines written to output_filename
    line_count = 0
    # do for all lines
    for line in input_lines:
        # split line by delimiter into list
        line_lst = line.split('\t')
        line_lst[5] = line_lst[5].replace(' ', '')
        #make sure the postal code is in the correct format
        if any(char.isdigit() for char in line_lst[6]):
            new_lst = line_lst[:5]
            new_lst.append(line_lst[5]+line_lst[6])
            new_lst.extend(line_lst[7:])
            line_lst = new_lst

        # make changes if there are more than 9 columns
        if len(line_lst) > 9:
            temperature_lst = line_lst[7:-1]
            temperature = get_columns_straight(temperature_lst)
        
            line = '\t'.join(line_lst[:7]) + '\t' + temperature + '\t' + line_lst[-1]
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