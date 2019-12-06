# COMP 202 A3 Part 1
# Name: Shaista Asmi
# Student ID: 260682464

import doctest
import random

def flatten_lists(nested):
    '''
    >>> flatten_lists([[0], [1, 2], 3])
    [0, 1, 2, 3]
    '''
    output = []
    for maybe_list in nested:
        # if maybe_list is a list, convert list to values 
        if type(maybe_list) == list:
            for element in maybe_list:
                output.append(element)
        # keep maybe_list as is 
        else: 
            output.append(maybe_list)
    return output 

def flatten_dict(d):
    '''
    >>> flatten_dict({'LIBERAL': 5, 'NDP':2})
    ['LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'LIBERAL', 'NDP', 'NDP']
    '''
    output = []
    for key in d.keys():
        for i in range(d[key]):
            output.append(key)
    return output

def add_dicts(d1, d2):
    '''
    >>> add_dicts({'a': 5, 'b': 2, 'd': -1}, {'a': 7, 'b': 1, 'c': 5})
    {'a': 12, 'b': 3, 'd': -1, 'c': 5}
    '''
    d = {}
    for key in d1.keys():
        d[key] = d1[key]
    for key in d2.keys():
        if key in d1.keys():
            d[key] = d[key] + d2[key]
        else:
            d[key] = d2[key]
    return d

def get_all_candidates(ballots):
    '''
    >>> get_all_candidates([{'GREEN':3, 'NDP':5}, {'NDP':2, 'LIBERAL':4}, ['CPC','NDP'],'BLOC'])
    ['GREEN', 'NDP', 'LIBERAL', 'CPC', 'BLOC']
    '''
    all_candidates = []
    for sublist in ballots:
        if type(sublist) == list:
            all_candidates += flatten_lists(sublist)
        elif type(sublist) == dict:
            all_candidates += flatten_dict(sublist)
        elif type(sublist) == str:
            all_candidates.append(sublist)
    output = []
    for candidate in all_candidates:
        if candidate not in output:
            output.append(candidate)
    return output


###################################################### winner/loser

def get_candidate_by_place(result, func):
    '''
    >>> result = {'LIBERAL':4, 'NDP':6, 'CPC':6, 'GREEN':4}
    >>> random.seed(0)
    >>> get_candidate_by_place(result, min)
    'GREEN'
    >>> random.seed(1)
    >>> get_candidate_by_place(result, min)
    'LIBERAL'
    '''
    # if dictionary is empty, there can be no min/max
    if len(result.values()) == 0:
        return None
    else:
        # note either min(votes) or max(votes)
        votes = func(result.values())
        # note all candidates tied at the above value of votes
        candidates = []
        for candidate in result.keys():
            if result[candidate] == votes:
                candidates.append(candidate)
        # randomly select one candidate from the tied candidates
        return random.choice(candidates)


def get_winner(result):
    '''
    >>> get_winner({'NDP': 2, 'GREEN': 1, 'LIBERAL': 0, 'BLOC': 0})
    'NDP'
    '''
    return get_candidate_by_place(result, max)


def last_place(result, seed = None):
    '''
    >>> last_place({'NDP': 3, 'GREEN': 2, 'LIBERAL': 0, 'BLOC': 1})
    'LIBERAL'
    '''
    return get_candidate_by_place(result, min)


###################################################### testing help

def pr_dict(d):
    '''(dict) -> None
    Print d in a consistent fashion (sorted by key).
    Provided to students. Do not edit.
    >>> pr_dict({'a':1, 'b':2, 'c':3})
    {'a': 1, 'b': 2, 'c': 3}
    '''
    l = []
    for k in sorted(d):
        l.append( "'" + k + "'" + ": " + str(d[k]) )
    print('{' + ", ".join(l) + '}')


if __name__ == '__main__':
    doctest.testmod()
