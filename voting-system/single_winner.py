from a3_helpers import *


def count_plurality(ballots):
    '''
    >>> count_plurality(['LIBERAL', 'LIBERAL', 'NDP', 'LIBERAL'])
    {'LIBERAL': 3, 'NDP': 1}
    '''
    output = {}
    for candidate in ballots:
        # if candidate yet to exist in dictionary 
        if candidate not in output.keys():
            # initialize candidate in dictionary
            output[candidate] = 1
        # if candidate exists in dictionary
        else:
            # increment vote count for that candidate
            output[candidate] +=1
    return output
    

def count_approval(ballots):
    '''
    >>> count_approval([['LIBERAL', 'NDP'], ['NDP'], ['NDP', 'GREEN', 'BLOC']])
    {'LIBERAL': 1, 'NDP': 3, 'GREEN': 1, 'BLOC': 1}
    '''
    # flatten list of lists
    ballots = flatten_lists(ballots)
    # count votes each candidate got
    output = count_plurality(ballots)
    return output


def count_rated(ballots):
    '''
    >>> count_rated([{'LIBERAL': 5, 'NDP':2}, {'NDP':4, 'GREEN':5}])
    {'LIBERAL': 5, 'NDP': 6, 'GREEN': 5}
    '''
    output = {}
    # sum votes each candidate got into one dictionary
    for ballot in ballots:
        output = add_dicts(output, ballot)
    return output
    

def count_first_choices(ballots):
    ''''
    >>> count_first_choices([['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']])
    {'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0}
    '''
    # list all candidates
    all_candidates = flatten_lists(ballots)
    # create new list with only first choices
    first_choices = []
    for ballot in ballots:
        if len(ballot) != 0:
            first_choices.append(ballot[0])
    # count first choice votes each candidate got
    output = count_plurality(first_choices)
    # account for candidates without any first choice votes
    for candidate in all_candidates:
        if candidate not in first_choices: 
            output[candidate] = 0
    return output


if __name__ == '__main__':
    doctest.testmod()
